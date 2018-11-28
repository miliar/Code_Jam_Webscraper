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
#define RL(a) scanf("%lld", &(a))
#define RLL(a, b) scanf("%lld%lld", &(a), &(b))
#define RLLL(a, b, c) scanf("%lld%lld%lld", &(a), &(b), &(c)) 
#define PI(r) printf("%d\n", (r))
#define PL(r) printf("%lld\n", (r))
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
#pragma warning (disable : 4996)
//#pragma comment(linker, "/STACK:102400000,102400000")
#define EPS 1e-8
#define INF 2000000000
#define LIM (1ll << 60)
#define MOD 1000000007
#define N 1111

using namespace std;

int n, m;
int tr[4][N * 100][26], fl[N], ma, cnt, tot[4];
char s[N][111];

void insert(char *s, int ty) {
	int i = 0, x, now = 0;
	while (1) {
		x = s[i] - 'A';
		if (tr[ty][now][x] == 0) {
			++tot[ty];
			mem(tr[ty][tot[ty]]);
			tr[ty][now][x] = tot[ty];
		}
		now = tr[ty][now][x];
		i++;
		if (s[i] == 0) break;
	}
}


void bld(int ty) {
	mem(tr[ty][0]), tot[ty] = 0;
	REPP(i, 1, m) if (fl[i] == ty) insert(s[i], ty);
}

void dfs(int x) {
	if (x > m) {
		REP(i, n) bld(i);
		int tt = 0;
		REP(i, n) tt += tot[i] + (tot[i] ? 1 : 0);
		if (tt > ma) ma = tt, cnt = 1;
		else if (tt == ma) cnt++;
	}
	else {
		REP(i, n) fl[x] = i, dfs(x + 1);
	}
}


int main(){
	int t, x, y, z, ca = 1;
	freopen("D:/Contest/1.in", "r", stdin);
	freopen("1.ans", "w", stdout);
	//ios :: sync_with_stdio(false);
	RI(t);
	while (t--) {
		RII(m, n);
		REPP(i, 1, m) RS(s[i]);
		dfs(1);
		printf("Case #%d: %d %d\n", ca++, ma, cnt);
		ma = cnt = 0;
	}


	return 0;
}
