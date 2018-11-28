#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;

struct Trie {
	struct Node {
		int next[26];

		Node() {
			memset(next, -1, sizeof next);
		}
	};

	vector<Node> data;

	Trie() {
		data = vector<Node>(1);
	}

	void addString(const string &s) {
		int u = 0;
		for(int i = 0; i < (int) s.size(); ++i) {
			int c = s[i] - 'A';
			if(data[u].next[c] == -1) {
				data[u].next[c] = data.size();
				data.push_back(Node());
			}
			u = data[u].next[c];
		}
	}

	int getSize() const {
		return data.size();
	}
};

const int M = 8, N = 4;
int m, n, maxNodes, wayCount;
string s[M];
Trie trie[N];

void backtrack(int pos) {
	if(pos == m) {
		int nodeCount = 0;
		for(int i = 0; i < n; ++i) {
			nodeCount += trie[i].getSize();
			if(trie[i].getSize() == 1) return;
		}
		if(nodeCount > maxNodes) {
			maxNodes = nodeCount;
			wayCount = 0;
		}
		if(nodeCount == maxNodes) {
			++wayCount;
		}
	} else {
		for(int i = 0; i < n; ++i) {
			Trie save = trie[i];
			trie[i].addString(s[pos]);
			backtrack(pos + 1);
			trie[i] = save;
		}
	}
}

int main() {
	int nTest; cin >> nTest;
	for(int test = 0; test < nTest; ++test) {
		cin >> m >> n;
		for(int i = 0; i < m; ++i) cin >> s[i];
		maxNodes = wayCount = -1;
		backtrack(0);
		printf("Case #%d: %d %d\n", test + 1, maxNodes, wayCount);
	}
	return 0;
}
