#include <cassert>
#include <iostream>
#include <algorithm>


struct game;

struct chest
{
	int t, K;
	int *keys;
	bool opened;

	friend std::istream &operator>>(std::istream &is, chest &c);

	chest() : keys(0), opened(false) {}
	~chest() { deallocate(); }

private:
	void deallocate()
	{
		delete [] keys;
	}

};

struct key_type
{
	key_type() : remaining_keys(0) {}
	~key_type() { deallocate(); }
	int count;
	int remaining_chests;
	int *remaining_keys; // keys accessibles from the chest of this key type
	bool mark;

	void deallocate()
	{
		delete [] remaining_keys;
	}
};

struct game
{
	int K, N, T;
	int *initial_keys;
	key_type *keys;
	int *solution;
	chest *chests;

	friend std::istream &operator>>(std::istream &is, game &g);

	game() : initial_keys(0), keys(0), chests(0), steps(0) {}
	~game() { deallocate(); }

	bool can_be_opened(int n);
	void open(int n);
	void close(int n);
	int *solve();

private:
	int *steps;

	bool solve(int s);
	bool is_graph_connected();
	void mark_accessible_nodes(int t);
	void deallocate();
	void allocate_keys();
};


// Game methods

bool game::can_be_opened(int n)
{
	assert(n < N);
	chest &c = chests[n];
	return !c.opened && keys[c.t].count > 0;
}

void game::open(int n)
{
	chest &c = chests[n];
	assert(can_be_opened(n));

	c.opened = true;
	keys[c.t].count--;
	keys[c.t].remaining_chests--;

	for (int k = 0 ; k < c.K ; k++) {
		int t = c.keys[k];
		assert(t <= T);
		keys[t].count++;
		keys[c.t].remaining_keys[t]--;
	}
}

void game::close(int n)
{
	chest &c = chests[n];
    assert(c.opened);

   	c.opened = false;
	keys[c.t].count++;
	keys[c.t].remaining_chests++;

	for (int k = 0 ; k < c.K ; k++) {
		int t = c.keys[k];
		assert(t <= T);
		keys[t].count--;
		keys[c.t].remaining_keys[t]++;
	}
}

int *game::solve()
{
	// Key count initialization
	for (int t = 0 ; t < T+1 ; t++) {
		keys[t].count = 0;
		keys[t].remaining_chests = 0;
		for (int u = 0 ; u < T+1 ; u++) {
			keys[t].remaining_keys[u] = 0;
		}
	}

	for (int k = 0 ; k < K ; k++) {
		keys[initial_keys[k]].count++;
	}

	for (int n = 0 ; n < N ; n++) {
		keys[chests[n].t].remaining_chests++;
		for (int k = 0 ; k < chests[n].K ; k++) {
			assert(chests[n].t <= T && chests[n].keys[k] <= T);
			keys[chests[n].t].remaining_keys[chests[n].keys[k]]++;
		}
	}

	// Consistency check
	for (int t = 0 ; t < T+1 ; t++) {
		int s = keys[t].count;
		for (int u = 0 ; u < T+1 ; u++) {
			s += keys[u].remaining_keys[t];
		}

		if (s < keys[t].remaining_chests) {
			// There is not enough keys to open all chests
			return 0;
		}
	}


	// Recursion initialization
	if (solve(0))
		return steps;
	else
		return 0;
}

bool game::solve(int s)
{
	if (s >= N)
		return true;

	for (int n = 0 ; n < N ; n++) {
		if (can_be_opened(n)) {
			open(n);

			// Try to cut the branch
			if (is_graph_connected()) {
				steps[s] = n;
				if (solve(s+1))
					return true;
			}

			close(n);
		}
	}

	return false;
}

bool game::is_graph_connected()
{
	for (int t  = 0 ; t < T+1 ; t++) {
		keys[t].mark = false;
	}

	for (int t  = 0 ; t < T+1 ; t++) {
		if (keys[t].count > 0)
			mark_accessible_nodes(t);
	}

	for (int t  = 0 ; t < T+1 ; t++) {
		if (!keys[t].mark && keys[t].remaining_chests > 0)
			return false;
	}

	return true;
}


void game::mark_accessible_nodes(int t)
{
	if (!keys[t].mark) {
		keys[t].mark = true;
		for (int u = 0 ; u < T+1 ; u++) {
			if (keys[t].remaining_keys[u] > 0) {
				mark_accessible_nodes(u);
			}
		}
	}
}


void game::deallocate()
{
	delete [] initial_keys;
	delete [] keys;
	delete [] chests;
	delete [] steps;
}

void game::allocate_keys()
{
	// Initialize key count
	T = 0;

	for (int k = 0 ; k < K ; k++) {
		T = std::max(T, initial_keys[k]);
	}

	for (int n = 0 ; n < N ; n++) {
		T = std::max(T, chests[n].t);
		for (int k = 0 ; k < chests[n].K ; k++)
			T = std::max(T, chests[n].keys[k]);
	}

	keys = new key_type[T+1];

	for (int t = 0 ; t < T+1 ; t++) {
		keys[t].deallocate();
		keys[t].remaining_keys = new int[T+1];
	}
}


// Input

std::istream &operator>>(std::istream &is, chest &c)
{
	is >> c.t >> c.K;
	c.deallocate();
	c.keys = new int[c.K];

	for (int k = 0 ; k < c.K ; k++) {
		is >> c.keys[k];
	}

	return is;
}

std::istream &operator>>(std::istream &is, game &g)
{
	is >> g.K >> g.N;

	g.deallocate();
	g.initial_keys = new int[g.K];
	g.chests = new chest[g.N];
	g.steps = new int[g.N];

	for (int k = 0 ; k < g.K ; k++) {
		is >> g.initial_keys[k];
	}

	for (int n = 0 ; n < g.N ; n++) {
		is >> g.chests[n];
	}

	g.allocate_keys();

	return is;
}


// Main

int main()
{
	int T;
	game g;

	// Read the number of cases
	std::cin >> T;

	// For each case
	for (int t = 0 ; t < T ; t++) {
		std::cin >> g;
		int *steps = g.solve();

		std::cout << "Case #" << (t+1) << ":";
		if (steps) {
			for (int n = 0 ; n < g.N ; n++) {
				std::cout << " " << (steps[n] + 1);
			}
		}
		else {
			std::cout << " IMPOSSIBLE";
		}
		std::cout << std::endl;
	}

	return 0;
}
