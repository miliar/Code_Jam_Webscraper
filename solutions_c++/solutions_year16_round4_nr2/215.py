#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const int MAXN = 205;

R p[MAXN];
R f[MAXN][MAXN];

R solve(vector<R> p){
	int n = p.size();
	int i, j;
	memset(f, 0, sizeof f);
	f[0][0] = 1.;
	for(i = 0; i < n; i++){
		for(j = 0; j <= i; j++){
			f[i+1][j+1] += f[i][j] * p[i];
			f[i+1][j] += f[i][j] * (1-p[i]);
		}
	}
	return f[n][n/2];
}

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		int n, k;
		int i, j;
		scanf("%d%d", &n, &k);
		for(i = 0; i < n; i++)
			scanf("%lf", &p[i]);
		R ans = 0.;
		sort(p, p+n);
		for(i = 0; i <= k; i++){
			vector<R> t;
			for(j = 0; j < i; j++)
				t.pb(p[j]);
			for(j = n-k+i; j < n; j++)
				t.pb(p[j]);
			ans = max(ans, solve(t));
		}

		printf("Case #%d: %.10lf\n", i0, ans);
	}
	return 0;
}
