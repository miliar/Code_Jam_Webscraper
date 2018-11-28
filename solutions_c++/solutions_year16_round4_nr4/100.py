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

int bitcnt(int n) {
	int cnt = 0;
	while (n) {
		cnt++; n -= n&(-n);
	}
	return cnt;
}
int n;
int cur[4];
int chk() {
	F(i, n) {
		int ah = 0;
		int cnt = 0;
		F(j, n) {
			if (cur[j] & (1 << i)) {
				cnt++; ah |= cur[j];
			}
		}
		if (!cnt) return 0;
		if (bitcnt(ah) > cnt) return 0;
	}
	return 1;
}

int a[4];
char buf[10];
int main() {
#ifndef __GNUG__
	freopen("D-small-attempt0.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);
		
		ni(n);
		F(i, n) {
			scanf("%s", buf);
			a[i] = strtol(buf, NULL, 2);
		}
		int p2 = 1 << (n*n);
		int ans = inf;
		F(tt, p2) {
			int  t = tt;
			F(i, n) {
				cur[i] = t % (1 << n);
				t /= (1 << n);
			}
			int bad = 0;
			F(i, n) {
				if ((cur[i] & a[i]) != a[i]) {
					bad = 1; break;
				}
			}
			if (bad)continue;
			if (chk()) {
				int dif = 0;
				F(i, n) dif += bitcnt(cur[i]) - bitcnt(a[i]);
				ans = min(ans, dif);
			}
		}
		printf("%d\n", ans);
		fprintf(stderr, "Case %d complete\n", casen);
	}

	return 0;
}
