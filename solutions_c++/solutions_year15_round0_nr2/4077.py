// #include C/C++ {
#include <bits/stdc++.h>
// }
using namespace std;
// #typedef {
typedef long long int64;
typedef unsigned long long uint64;
typedef pair <int, int> PII;
typedef pair <int64, int64> PLL;
typedef pair <double, double> PDD;
// }

// #parameter{
#define LEN 2
#ifdef DEBUG_MODE

#define TYPE decltype
#define RF(filename) {freopen((filename), "r", stdin);}
#define WF(filename) {freopen((filename), "w", stdout);}
#define DEBUG printf

#else

#define TYPE __typeof
#define RF(filename) {;}
#define WF(filename) {;}
#define DEBUG(...)

#endif

// #define {
#define SZ(a) ((int)(a).size())
#define X first
#define Y second
#define MP make_pair
#define L(x) ((x)<<1)
#define R(x) ((x)<<1 | 1)
#define max3(x, y, z) (max(max((x), (y)), (z)))
#define min3(x, y, z) (min(min((x), (y)), (z)))
#define BIT(x, i) (((x) >> (i)) & 1)
#define ALL(it) (it).begin(), (it).end()
#define FOR(it, c) for( TYPE((c).begin()) it = (c).begin(); it != (c).end(); it++)
/////////////////////////////////////////////////////////////
const double PI = acos(-1.0);
const double EPS = 1e-6;

#define MAX_N 1005
#define MAX_M 5005
#define MAXX 0x3f
#define UPPER 2147483647LL
#define INF ((1 << 30) - 1)
#define BINF ((1LL << 62) - 1LL)
#define NONE -1
#define NIL 0
// }

/////////////////////////////////////////////////////////////
int P[MAX_N];
int cnt[MAX_N];
int dp[MAX_N][MAX_N];
void Setup(){
	memset(dp, NONE, sizeof(dp));
}
void Init(){
	memset(cnt, 0, sizeof(cnt));
}
int DFS(int n, int a){
	if (dp[n][a] != NONE)
		return dp[n][a];
	int &res = dp[n][a];
	if(n <= a)
		return res = 0;
	if (a == 1)
		return res = n - 1;
	int res2 = DFS(n - a, a) + 1;
	int res1 = 0;
	n--;
	while (n > 0){
		res1++;
		n /= a;
	}
	return res = min(res1, res2);
}
/////////////////////////////////////////////////////////////
int main(){
	RF("input.txt");
	WF("output.txt");

	Setup();
	/*
	assert(DFS(6, 2) == 2);
	assert(DFS(8, 2) == 3);
	assert(DFS(8, 3) == 2);
	assert(DFS(9, 3) == 2);
	assert(DFS(10, 3) == 3);
	*/

	int T;
	scanf("%d", &T);
	for (int _ = 1; _ <= T; _++){
		Init();
		int D;
		scanf("%d", &D);
		for (int i = 0; i < D; i++){
			scanf("%d", P + i);
			cnt[P[i]]++;
		}
		int maxx = *max_element(P, P + D);
		int res = maxx;
		for (int maxK = 2; maxK <= maxx; maxK++){
			int cost = 0;
			for (int i = maxK + 1; i <= maxx; i++)
				cost += cnt[i] * DFS(i, maxK);
			cost += maxK;
			res = min(res, cost);
		}
		printf("Case #%d: %d\n", _, res);
	}
	return 0;
}