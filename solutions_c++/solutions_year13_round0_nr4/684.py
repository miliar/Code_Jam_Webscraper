
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <complex>

using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

int result[1<<21];
int nextt[1<<21];

void solve() {
	int K, N;
	scanf("%d%d", &K, &N);
	vector <int> key(K);
	vector <int> t(N);
	vector <vector<int> > next(N);
	rep(i, K) scanf("%d", &key[i]);
	rep(i, N) {
		scanf("%d", &t[i]);
		int k;
		scanf("%d", &k);
		next[i].resize(k);
		rep (j, k) scanf("%d", &next[i][j]);
	}	
	rep (i, (1<<N)) result[i] = 0;
	for (int i = (1<<N) - 1; i >= 0; i--) {
		if (i == (1<<N) - 1) {
			result[i] = 1;
		}
		else
		rep (j, N) if (!(i&(1<<j)) && result[i | (1<<j)]) {
			map<int, int> klucze;
			fore (it, key) klucze[*it]++;
			bool ok = true;
			rep (k, N) if (i&(1<<k)) fore (it, next[k]) klucze[*it]++;
			rep (k, N) if (i&(1<<k)) if (--klucze[t[k]] < 0) ok == false;

			if (ok && klucze[t[j]] > 0) {
				result[i] = true;
				nextt[i] = j;
				break;
			}
		}
	}
	if (result[0] == 0) printf("IMPOSSIBLE");
	else {
		int mask = 0;
		while (mask != (1<<N) - 1) {
			int i = nextt[mask];
			mask |= 1 << i;
			//cerr << "mask " <<  mask << endl;
			printf("%d", i + 1);
			if (mask != (1<<N) - 1) printf(" ");
		}
	}
}

int main(int argc, char ** argv) {
	cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
	int t;
	scanf("%d", &t);
	fo (i, 1, t) {
		cerr << __LINE__ << " " << i << endl;
		printf("Case #%d: ", i);
		solve();
		printf("\n");
		fflush(stdout);
		cerr.flush();
	}
	return 0;
}


