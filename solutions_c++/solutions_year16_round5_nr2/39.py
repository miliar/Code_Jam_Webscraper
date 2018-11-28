#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <iterator>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define add(x,y) ((ll)(x)+(y))%mod
#define F(i,n) for(int i = 0; i < n; i++)
#define FF(i,n) for(int i = 1; i <= n; i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//


const int N = 100;

vector<int> adj[N];
char C[N+1];
char cool[5][N];
int par[N];
int cnt[N];
vector<int> roots;
char curch[N + 1];

void cnt_dfs(int i) {
	cnt[i] = 1;
	for (auto &x : adj[i]) {
		if (x == par[i]) continue;
		cnt_dfs(x);
		cnt[i] += cnt[x];
	}
}

vector<int> gen_dfs(int u) {
	vector<int> togo(1, u);
	vector<int> curpos(adj[u].size());
	vector<vector<int> > ress(adj[u].size());
	F(i, (int)adj[u].size()) {
		int x = adj[u][i];
		F(j, cnt[x]) togo.push_back(i);
		ress[i] = gen_dfs(x);
	}
	random_shuffle(togo.begin() + 1, togo.end());
	FF(i, (int)togo.size() - 1) {
		int x = togo[i];
		togo[i] = ress[x][curpos[x]++];
	}
	return togo;
}

int main() {
#ifndef __GNUG__
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	srand((unsigned int)time(0));
	int T; ni(T);
	FF(tt, T) {
		printf("Case #%d: ", tt);
		//-----------------------Your code goes here------------------------//
		int n; ni(n);
		roots.clear();
		F(i, n)par[i] = -1;
		F(i, n) cnt[i] = 0, adj[i].clear();
		F(i, n) {
			int p; ni(p);
			if (!p) {
				roots.push_back(i); continue;

			}
			p--;
			par[i] = p;
			adj[p].push_back(i);
		}
		scanf("%s", C);
		int m; ni(m);
		F(i, m) {
			scanf("%s", cool[i]);
		}
		for (auto &x : roots) cnt_dfs(x);
		int TOT_ATT = 10000;
		vector<int> goodcnt(5);
		F(att, TOT_ATT) {
			vector<int> togo;
			vector<vector<int> > ress(roots.size());
			vector<int> curpos(roots.size());
			F(i, (int)roots.size()) {
				int x = roots[i];
				F(j, cnt[x]) togo.push_back(i);
				ress[i] = gen_dfs(x);
			}
			random_shuffle(togo.begin(), togo.end());
			F(i, (int)togo.size()) {
				int x = togo[i];
				togo[i] = ress[x][curpos[x]++];
			}
			F(i, n) {
				curch[i] = C[togo[i]];
			}
			curch[n] = 0;
			F(i, m) {
				if (strstr(curch, cool[i])) goodcnt[i]++;
			}
		
		}
		F(i, m) {
			printf("%.2f ", (double)goodcnt[i] / TOT_ATT);
		}
		puts("");

		//------------------------------------------------------------------//
		fprintf(stderr, "Case %d complete\n", tt);
	}
	return 0;
}
