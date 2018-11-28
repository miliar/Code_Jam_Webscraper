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
int k, c, s;
int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, tt = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d:", ++tt);
		for (int i = 1; i <= k; ++i)
			printf(" %d", i);
		puts("");
	}
	return 0;
}
