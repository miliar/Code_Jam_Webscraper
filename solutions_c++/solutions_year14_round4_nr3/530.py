#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <omp.h>
using namespace std;

#define dump(...) //(cerr<<#__VA_ARGS__<<" = "<<(DUMP(),__VA_ARGS__).str()<<endl)

struct DUMP : ostringstream {
	template<class T> DUMP &operator,(const T &t) {
		if(this->tellp()) *this << ", ";
		*this << t;
		return *this;
	}
};

template<class T> inline void chmax(T &a, const T &b) { if(b > a) a = b; }
template<class T> inline void chmin(T &a, const T &b) { if(b < a) a = b; }

template<class T, class U>
ostream &operator<<(ostream &os, const pair<T, U> &p) {
	return os << '(' << p.first << ", " << p.second << ')';
}

template<class Tuple, unsigned Index>
void print_tuple(ostream &os, const Tuple &t) {}

template<class Tuple, unsigned Index, class Type, class... Types>
void print_tuple(ostream &os, const Tuple &t) {
	if(Index) os << ", ";
	os << get<Index>(t);
	print_tuple<Tuple, Index + 1, Types...>(os, t);
}

template<class... Types>
ostream &operator<<(ostream &os, const tuple<Types...> &t) {
	os << '(';
	print_tuple<tuple<Types...>, 0, Types...>(os, t);
	return os << ')';
}

template<class Iterator>
ostream &dump_range(ostream &, Iterator, const Iterator &);

template<class T>
ostream &operator<<(ostream &os, const vector<T> &c) {
	return dump_range(os, c.cbegin(), c.cend());
}

template<class Iterator>
ostream &dump_range(ostream &os, Iterator first, const Iterator &last) {
	os << '[';
	for(int i = 0; first != last; ++i, ++first) {
		if(i) os << ", ";
		os << *first;
	}
	return os << ']';
}

typedef int weight;

struct edge {
	int to;
	weight cap;
	int rev;
	edge(int to_, weight cap_, int rev_):to(to_), cap(cap_), rev(rev_){}
};

constexpr weight INF = (1 << 29);
constexpr weight EPS = 1e-8;

vector<vector<edge> > G;
vector<int> level;
vector<int> iter;

void init(int V) {
	G.assign(V, vector<edge>());
	level.resize(V);
	iter.resize(V);
}

void add_edge(int from, int to, weight cap) {
	G[from].emplace_back(to, cap, G[to].size());
	G[to].emplace_back(from, 0, G[from].size() - 1);
}

void bfs(int s) {
	fill(level.begin(), level.end(), -1);
	queue<int> que;
	level[s] = 0;
	que.push(s);

	while(!que.empty()) {
		const int v = que.front();
		que.pop();

		for(const auto &e : G[v]) {
			if(e.cap > EPS && level[e.to] < 0) {
				level[e.to] = level[v] + 1;
				que.push(e.to);
			}
		}
	}
}

weight dfs(int v, int t, weight f) {
	if(v == t) return f;

	for(int& i = iter[v]; i < static_cast<int>(G[v].size()); ++i) {
		edge& e = G[v][i];
		if(e.cap > EPS && level[v] < level[e.to]) {
			const weight d = dfs(e.to, t, min(f, e.cap));
			if(d > EPS) {
				e.cap -= d;
				G[e.to][e.rev].cap += d;
				return d;
			}
		}
	}

	return 0;
}

weight max_flow(int s, int t) {
	weight flow = 0;
	dump("start");

	for(;;) {
		bfs(s);
		if(level[t] < 0) {
			dump("end");
			dump(flow);
			return flow;
		}

		fill(iter.begin(), iter.end(), 0);
		for(weight f; (f = dfs(s, t, INF)) > 0; flow += f);
	}
}

#define idx(x, y) ((x) + (y) * w)

string solve() {
	int w, h, b;
	cin >> w >> h >> b;

	vector<vector<int>> field(h, vector<int>(w, 1));
	for(int i = 0; i < b; ++i) {
		int x0, y0, x1, y1;
		cin >> x0 >> y0 >> x1 >> y1;

		for(int y = y0; y <= y1; ++y) {
			for(int x = x0; x <= x1; ++x) {
				field[y][x] = 0;
			}
		}
	}

	const int n = w * h;
	const int source = 2 * n;
	const int sink = source + 1;
	init(sink + 1);

	for(int x = 0; x < w; ++x) {
		if(field[0][x]) add_edge(source, idx(x, 0), 1);
		if(field[h - 1][x]) add_edge(idx(x, h - 1) + n, sink, 1);
	}

	for(int y = 0; y < h; ++y) {
		for(int x = 0; x < w; ++x) {
			if(field[y][x]) {
				add_edge(idx(x, y), idx(x, y) + n, 1);
				if(x && field[y][x - 1]) add_edge(idx(x, y) + n, idx(x - 1, y), 1);
				if(x < w - 1 && field[y][x + 1]) add_edge(idx(x, y) + n, idx(x + 1, y), 1);
				if(y && field[y - 1][x]) add_edge(idx(x, y) + n, idx(x, y - 1), 1);
				if(y < h - 1 && field[y + 1][x]) add_edge(idx(x, y) + n, idx(x, y + 1), 1);
			}
		}
	}
	const int ans = max_flow(source, sink);
	const string res = to_string(ans);

	return res;
}

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": " << solve() << "\n";
		dump("hoge");
	}

	return EXIT_SUCCESS;
}
