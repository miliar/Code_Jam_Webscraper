#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <sstream>
#include <tuple>
#include <iostream>
#include <map>
#include <bitset>
#include <cstring>
#define ch(c) (c - 'A')

using namespace std;

const int mod = int(1e9) + 7;
const int nmax = 4;
int m, n;
int X;
int ways;
struct Trie {
	Trie* next[26];
	bitset<100> use;
	Trie() {
		memset(next, 0, sizeof(next));
	}
};

void clear(Trie* node) {
	for (int k = 0; k < 26; k++) {
		if (node->next[k] != NULL) {
			clear(node->next[k]);
		}
	}
	delete node;
}

void insert(Trie *node, const string& s) {
	vector<int> serverCount(n);
	Trie* aux = node;
	for (int k = 0; k < n; k++) {
		if (!node->use[k]) {
			serverCount[k]++;
		}
	}

	for (auto& c : s) {
		if (node->next[ch(c)] == NULL) {
			node->next[ch(c)] = new Trie();
		}

		node = node->next[ch(c)];
		for (int k = 0; k < n; k++) {
			if (!node->use[k]) {
				serverCount[k]++;
			}
		}
	}
	
	int server = 0;
	int sc = 1;
	for (int k = 1; k < n; k++) {
		if (serverCount[k] > serverCount[server]) 
			server = k, sc = 1;
		else
		if (serverCount[k] == serverCount[server]) sc++;
	}
	cout << sc << "\n";
	X += serverCount[server];
	ways = 1LL * ways * sc % mod;
	node = aux;
	node->use[server] = true;
	for (auto& c : s) {
		node = node->next[ch(c)];
		node->use[server] = true;
	}
}


void insert(Trie *node, const string& s, int serv) {
	node->use[serv] = 1;
	for (auto& c : s) {
		if (node->next[ch(c)] == NULL) {
			node->next[ch(c)] = new Trie();
		}

		node = node->next[ch(c)];
		node->use[serv] = 1;
	}

}

int nodeCount(Trie *node) {
	int ret = node->use.count();
	for (int k = 0; k < 26; k++) {
		if (node->next[k] != NULL) {
			ret += nodeCount(node->next[k]);
		}
	}
	delete node;
	return ret;
}


pair<int,int> brute(int m,int n,vector<string>& s) {
	pair<int, int> ret = { 0, 0 };
	int x;
	if (n == 1) {
		Trie* t = new Trie();
		for (int z = 0; z < m; z++) {
			insert(t, s[z], 0);
		}
		x = nodeCount(t);
		if (x > ret.first) ret = { x, 1 };
		else
			ret.second++;
		return ret;
	}
	for (int i = 0; i < (1 << m); i++) {
		if (n == 2) {
			int j = ((1 << m) - 1) ^ i;
			Trie* t = new Trie();
			for (int z = 0; z < m; z++) {
				if ((i >> z) & 1)  insert(t, s[z], 0);
				else
					insert(t, s[z], 1);
			}
			x = nodeCount(t);
			if (x > ret.first) ret = { x, 1 };
			else 
			if (x == ret.first){
				ret.second++;
			}
			continue;
		}
		for (int j = 0; j < (1 << m); j++) {
			if ((i & j) == 0) {
				if (n == 3) {
					
					Trie* t = new Trie();
					for (int z = 0; z < m; z++) {
						if ((i >> z) & 1)  insert(t, s[z], 0);
						else
						if ((j >> z) & 1) insert(t, s[z], 1);
						else
						insert(t, s[z], 2);
					}
					x = nodeCount(t);
					if (x > ret.first) ret = { x, 1 };
					else
					if (x == ret.first){
						ret.second++;
					}
					continue;
				}
				for (int k = 0; k < (1 << m); k++) {
					if ((i & k) == 0 && (j & k) == 0) {
						Trie* t = new Trie();
						for (int z = 0; z < m; z++) {
							if ((i >> z) & 1)  insert(t, s[z], 0);
							else
							if ((j >> z) & 1) insert(t, s[z], 1);
							else
							if ((k >> z) & 1)  insert(t, s[z], 2);
							else
							insert(t, s[z], 3);
						}
						x = nodeCount(t);
						if (x > ret.first) ret = { x, 1 };
						else
						if (x == ret.first){
							ret.second++;
						}
					}
				}
			}
		}
	}
	return ret;
}

int main() {
	ifstream cin("test.in");
	ofstream cout("test.out");
	int testCount;
	cin >> testCount;
	for (int t = 1; t <= testCount; t++) {
		cin >> m >> n;
		vector<string> a(m);
		X = 0;	ways = 1;
		cin.get();
		for (int i = 0; i < m; i++) {
			getline(cin, a[i]);
		}
		pair<int, int> ans = brute(m, n, a);
		cout << "Case #" << t << ": " << ans.first << " " << ans.second << "\n";
		
	}
	return 0;
}