#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

struct Node {
	vector<Node*> children;
	vector<char> childrench;
	int count;
	bool has;
	Node() : count(0), has(false) {}
};

Node* get(Node* n, char c) {
	for (int i = 0; i < (int)n->children.size(); ++i) {
		if (n->childrench[i] == c)
			return n->children[i];
	}
	Node* ret = new Node;
	n->childrench.push_back(c);
	n->children.push_back(ret);
	return ret;
}

void add(Node* n, const string& s) {
	++n->count;
	for (char c : s) {
		n = get(n, c);
		++n->count;
	}
	n->has = true;
}

int solve1(Node* n, int N) {
	int res = min(n->count, N);
	for (Node* m : n->children)
		res += solve1(m, N);
	return res;
}

int fact(int N) {
	int res = 1;
	for (int i = 1; i <= N; ++i)
		res *= i;
	return res;
}

int choose(int n, int k) {
	return fact(n) / fact(k) / fact(n-k);
}

int pow(int a, int b) {
	int res = 1;
	for (int i = 0; i < b; ++i)
		res *= a;
	return res;
}

int dp(int N, const vector<int>& sizes, int ind, int used) {
	if (ind == (int)sizes.size()) {
		return used == N ? 1 : 0;
	}
	int sz = sizes[ind];
	int res = 0;
	for (int nused = 0; nused <= sz; ++nused) {
		int nrest = sz - nused;
		if (used + nrest > N) continue;
		res += choose(used, nused) * fact(nused) * dp(N, sizes, ind+1, used + nrest) * choose(sz, nused);
	}
	return res;
}

int solve2(Node* n, int N) {
	if (n->count <= N) {
		int res = 1;
		for (int i = 0; i < n->count; ++i)
			res *= N-i;
		return res;
	}
	bool any = (N == 1);
	int res = 1;
	vector<int> sizes;
	for (Node* m : n->children) {
		res *= solve2(m, N);
		if (m->count >= N)
			any = true;
		sizes.push_back(m->count);
	}
	if (n->has) {
		res *= N;
		sizes.push_back(1);
	}

	if (any)
		return res;

	sort(sizes.rbegin(), sizes.rend());
	return dp(N, sizes, 1, sizes.front()) * fact(N);
}

void solve() {
	int M, N;
	cin >> M >> N;
	Node* top = new Node;
	for (int i = 0; i < M; ++i) {
		string s;
		cin >> s;
		add(top, s);
	}
	cout << solve1(top, N) << ' ';
	cout << solve2(top, N) << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
