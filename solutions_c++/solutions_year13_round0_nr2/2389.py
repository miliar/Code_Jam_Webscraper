
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

int ary[200][200];
int ary2[200][200];

int n, m;
int cnt = 0;
int dx[4] = { 1, -1, 0, 0};
int dy[4] = { 0, 0, -1, 1};
void bfs (int i, int j, int old) {
	if (!(i >= 0 && i < n && j >= 0 && j < m)) return;
	if (ary[i][j] == -1) return;
	if (ary[i][j] > old) return;
	ary[i][j] = -1;
	cnt++;

	rep (d, 4) {
		int nx = i + dx[d];
		int ny = j + dy[d];
		bfs(nx, ny, old);
	}
}

void solve() {
	cnt = 0;
	scanf("%d%d", &n, &m);
	rep (i, n) rep (j, m) {
		scanf("%d", &ary[i][j]);
		ary2[i][j] = ary[i][j];
	}
	bool ok = true;
		rep (i, n) rep (j, m) {
			int dd = ary[i][j];
			// same i
			bool can1 = true, can2 = true;
			{ 
				rep (j2, m) if (ary2[i][j2] > dd) can1 = false;
			}
			{ 
				rep (i2, n) if (ary2[i2][j] > dd) can2 = false;
			}
			
			if (!(can1 || can2)) { printf("NO"); return; }
		}
	printf("YES");
}

int main(int argc, char ** argv) {
	//  freopen("../1.in","r",stdin); 
	//  freopen("../2.in","r",stdin); 
	//  freopen("../3.in","r",stdin); 
	//  freopen("../A-small.in","r",stdin); freopen("../A-small.out","w",stdout);
	//  freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
	//  freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
	//  freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);
	//  freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout)

	cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
	int t;
	scanf("%d", &t);
	fo (i, 1, t) {
		printf("Case #%d: ", i);
		solve();
		printf("\n");
		fflush(stdout);
		cerr.flush();
	}
	return 0;
}


