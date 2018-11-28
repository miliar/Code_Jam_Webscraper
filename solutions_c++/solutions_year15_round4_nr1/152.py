#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <limits>
#include <ctime>
#include <cassert>
#include <map>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(x) ((int)1e##x)

#pragma comment(linker,"/STACK:36777216")

template<class T> void chmax(T& l, const T r){ l = max(l, r); }
template<class T> void chmin(T& l, const T r){ l = min(l, r); }

int r, c; 
char t[100][101];
int rcnt[100], ccnt[100];
int rmn[100], rmx[100], cmn[100], cmx[100];

ll solve(){
	cin >> r >> c;
	FOR(i, r) cin >> t[i];
	memset(rcnt, 0, sizeof(rcnt));
	memset(ccnt, 0, sizeof(ccnt));
	FOR(i, r){
		FOR(j, c) if (t[i][j] != '.') rcnt[i]++, ccnt[j]++;
	}
	FOR(i, r) FOR(j, c) if (t[i][j] != '.' && rcnt[i] == 1 && ccnt[j] == 1) return -1;
	FOR(i, r) rmn[i] = 110, rmx[i] = -1;
	FOR(i, c) cmn[i] = 110, cmx[i] = -1;
	FOR(i, r){
		FOR(j, c) if (t[i][j] != '.') {
			chmin(rmn[i], j);
			chmax(rmx[i], j);
			chmin(cmn[j], i);
			chmax(cmx[j], i);
		}
	}

	int ans = 0;
	FOR(i, r) FOR(j, c) if (t[i][j] != '.') {
		if (t[i][j] == '>') {
			if (rmx[i] == j) ans++;
		} else if (t[i][j] == '<') {
			if (rmn[i] == j) ans++;
		} else if (t[i][j] == '^') {
			if (cmn[j] == i) ans++;
		} else if (t[i][j] == 'v') {
			if (cmx[j] == i) ans++;
		}
	}

	return ans;
}

int main(){
	int t; cin >> t;
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		ll ans = solve();
		if (ans == -1){
			puts("IMPOSSIBLE");
	} else {
			printf("%lld\n", ans);
	}
	}

	return 0;
}
