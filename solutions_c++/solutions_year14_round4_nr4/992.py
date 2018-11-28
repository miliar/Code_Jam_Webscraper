#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
using namespace std;

string st[100];

int s[10000];

int const MX_TR_C = 100;
int const MAX_NODES = 1000;

struct trr {
	int nn;
	int next_go[MAX_NODES][26];

	void clear() {
		nn = 1;
		for (int i=0; i<26; i++) next_go[0][i] = -1;
	}

	void add_str(string st) {
		int v = 0;
		for (int i=0; i<(int) st.length(); i++)
			if (next_go[v][st[i]-'A'] < 0) {
				next_go[v][st[i]-'A'] = nn;
				for (int j=0; j<26; j++) next_go[nn][j] = -1;
				v = nn;
				nn++;
			}
			else
				v = next_go[v][st[i]-'A'];
	}

	int nodes() {
		return nn;
	}
} my_trie[MX_TR_C];

int used[MX_TR_C];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int q=0; q<t; q++) {
		int cnt,serv;
		cin>>cnt>>serv;
		for (int j=0; j<cnt; j++) cin>>st[j];
		
		int mx = 0, mx_cnt = 0;

		int g=1;
		for (int j=0; j<cnt; j++) g*=serv;

		for (int c=0; c<g; c++) {
			for (int j=0; j<cnt; j++) s[j] = 0;
			int x = c, ind = 0;
			while (x>0) {
				s[ind++] = x%serv;
				x/=serv;
			}

			for (int j=0; j<MX_TR_C; j++) {
				my_trie[j].clear();
				used[j] = 0;
			}
			for (int j=0; j<cnt; j++) {
				my_trie[s[j]].add_str(st[j]);
				used[s[j]] = 1;
			}

			int nodes = 0;
			for (int j=0; j<MX_TR_C; j++)
				nodes += my_trie[j].nodes() * used[j];

			int cnt_used = 0;
			for (int j=0; j<MX_TR_C; j++)
				cnt_used += used[j];
			
			if (cnt_used != serv)
				continue;

			if (nodes>mx) {
				mx = nodes;
				mx_cnt = 1;
			}
			else if (nodes == mx)
				mx_cnt++;
		}

		printf("Case #%d: %d %d\n",q+1, mx, mx_cnt);
	}

	return 0;
}