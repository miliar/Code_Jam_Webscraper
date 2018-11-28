#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;
const int N = 1000;
int sz = 0;
int to[N];
int go[N][26];

void clear() {
	sz = 1;
	memset(go[0], -1, sizeof(int) * 26);
}

void add_string(const string& s) {
	int at = 0;
	int id = 0;
	while (id < s.size() && go[at][s[id] - 'A'] != -1) {
		at = go[at][s[id] - 'A'];
		++id;
	}

	while (id < s.size()) {
		memset(go[sz], -1, sizeof(int) * 26);
		go[at][s[id] - 'A'] = sz;
		at = sz;
		++sz;
		++id;
	}
}

pair<int, int> solve(const vector<string>& s, int n) {
	int m = s.size();
	vector<int> to(m, 0);

	int best = -INF;
	int ways = 0;

	while (true) {

		

		int current = 0;
		for (int trie_id = 0; trie_id < n; ++trie_id) {
			clear();
			int size = 0;
			for (int z = 0; z < to.size(); ++z) {
				if (to[z] == trie_id) {
					add_string(s[z]);
					++size;
				}
			}

			if (size == 0) {
				goto end;
			}

			current += sz;
		}

		if (current == best) {
			++ways;
		}

		if (current > best) {
			best = current;
			ways = 1;
		}

		end:;

		int i = 0;
		while (i < to.size() && to[i] == n - 1) {
			to[i] = 0;
			++i;
		}

		if (i >= to.size()) break;
		++to[i];
	}

	return make_pair(best, ways);
}

int main() {


    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);


	int T; cin >> T;

	for (int test = 1; test <= T; ++test) {
		int n, m;
		cin >> m >> n;
		vector<string> s(m);
		for (int i = 0; i < m; ++i) cin >> s[i];
		pair<int, int> r = solve(s, n);
		cout << "Case #" << test << ": " << r.first << " " << r.second << endl;
	}


	
    return 0;
}