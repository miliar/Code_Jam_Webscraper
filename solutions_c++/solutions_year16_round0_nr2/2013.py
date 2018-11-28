#include<stdlib.h>
#include<time.h>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<set>
#include<queue>
#include<bitset>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> vi;
typedef pair<int, int> pii;
#define sz(x) ((int)(x.size()))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
const int N = 1e2 + 7;
const int M = 1e6 + 7;
const int INF = 2e5 + 7;
const int MOD = 1e9 + 7;
const LL LINF = 1e17 + 7;
const double Pi = acos(-1.);
const double EPS = 1e-8;
int f[N][2];
char S[N];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, tt = 0;
	scanf("%d", &T);
	while (T--) {
		scanf(" %s", S);
		int n = strlen(S);
		for (int i = 1; i <= n; ++i)
			if (S[i - 1] == '-') {
				f[i][0] = min(f[i - 1][0], f[i - 1][1] + 1);
				f[i][1] = min(f[i - 1][0] + 1, f[i - 1][1] + 2);
			} else {
				f[i][0] = min(f[i - 1][0] + 2, f[i - 1][1] + 1);
				f[i][1] = min(f[i - 1][0] + 1, f[i - 1][1]);
			}
		printf("Case #%d: %d\n", ++tt, f[n][1]);
	}
	return 0;
}
