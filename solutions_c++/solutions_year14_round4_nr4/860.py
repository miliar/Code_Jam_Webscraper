#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <math.h>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;

#define INF 0x3FFFFFFF

int m, n, best, num;

vector<string> server[5];

string s[10];

struct trie {
	trie () {
		for (int i = 0; i < 30; i++)
			next[i] = NULL;
	}
	trie *next[30];
};

void tryme(vector<vector<string> > comb) {
	int res = 0;
	for (int i = 0; i < n; i++) {
		if (comb[i].size() == 0) return;
		res++;
		trie t;
		for (int j = 0; j < comb[i].size(); j++) {
			string s = comb[i][j];
			trie *cur = &t;
			for (int k = 0; k < s.length(); k++) {
				if (cur->next[s[k] - 'A'] == NULL) {
					cur->next[s[k] - 'A'] = new trie();
					res++;
				}
				cur = cur->next[s[k] - 'A'];
			}
		}
	}

	if (res > best) {
		best = res;
		num = 1;
	} else if (res == best) {
		num++;
	}
}

void solve(int idx, vector<vector<string> > comb) {
	if (idx >= m) {
		tryme(comb);
	} else {
		for (int i = 0; i < n; i++) {
			vector<vector<string> > newcomb = comb;
			newcomb[i].push_back(s[idx]);
			solve(idx+1, newcomb);
		}
	}
}

int main() {
  int c;
  cin >> c;
  for (int cc = 1; cc <= c; cc++) {
  	cin >> m >> n;
  	for (int i =0 ;i < m; i++) {
  		cin >> s[i];
  	}

  	vector<vector<string> > comb(n);
  	best = 0;
  	num = 0;
  	solve(0, comb);
    printf("Case #%d: %d %d\n", cc,best, num);
  }
  return 0;
}
