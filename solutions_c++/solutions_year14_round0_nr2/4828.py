#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <bitset>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#define dou double
#define mem(a) memset(a, 0, sizeof(a))
#define memm(a) memset(a, -1, sizeof(a))
#define LL long long
#define PB push_back
#define MP make_pair
#define PII pair<int, int>
#define FI first
#define SE second
#define RI(a) scanf("%d", &(a))
#define RII(a, b) scanf("%d%d", &(a), &(b))
#define RIII(a, b, c) scanf("%d%d%d", &(a), &(b), &(c))
#define RL(a) scanf("%I64d", &(a))
#define RLL(a, b) scanf("%I64d%I64d", &(a), &(b))
#define RLLL(a, b, c) scanf("%I64d%I64d%I64d", &(a), &(b), &(c)) 
#define PI(r) printf("%d\n", (r))
#define PL(r) printf("%I64d\n", (r))
#define RS(s) scanf("%s", (s))
#define SL(a) strlen(a)
#define REP(i, n) for (int i = 0; i < (int) (n); ++i)
#define REPP(i, a, b) for (int i = (int) (a); i <= (int) (b); ++i)
#define FOR(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
//Segment tree
#define MID ((l + r) >> 1)
#define L (x << 1)
#define R ((x << 1) | 1)
#define LC L, l, MID
#define RC R, MID + 1, r
#define LB(x) ((x) & (-(x)))
#define M (N - 1000)
#pragma warning (disable : 4996)
//#pragma comment(linker, "/STACK:102400000,102400000")
#define EPS 1e-8
#define INF 2000000000
#define LIM (1ll << 60)
#define MOD 1000000007
#define N 111111

using namespace std;

int n, m;
dou C, F, X, sum[N], tt[N];

int main(){
	int t, x, y, z, ca = 1;
	freopen("E:/Code/in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//ios :: sync_with_stdio(false);
	RI(t);
	while (t--) {
		scanf("%lf%lf%lf", &C, &F, &X);
		n = (int) (X / C) + 100000;
		tt[0] = X / 2.0;
		REPP(i, 1, n) {
			sum[i] = sum[i - 1] + C / (2.0 + 1.0 * (i - 1) * F);
			tt[i] = sum[i] + X / (2.0 + i * F);
		}
		dou mm = tt[0];
		REPP(i, 1, n) mm = min(tt[i], mm);
		printf("Case #%d: %.10lf\n", ca++, mm);
	}


	return 0;
}
