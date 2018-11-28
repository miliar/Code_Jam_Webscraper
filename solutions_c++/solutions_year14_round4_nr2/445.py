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
int a[N], b[N], c[N];


int main(){
	int t, x, y, z, ca = 1;
	freopen("D:/Contest/1.in", "r", stdin);
	freopen("1.ans", "w", stdout);
	//ios :: sync_with_stdio(false);
	RI(t);
	while (t--) {
		RI(n);
		REPP(i, 1, n) RI(a[i]), b[i] = a[i];
		sort(a + 1, a + n + 1);
		REPP(i, 1, n) {
			REPP(j, 1, n) if (b[j] == a[i]) c[j] = i;
		}
		REPP(i, 1, n) a[i] = c[i];
		int st = 1, en = n;
		int cnt = 0, pos;
		REPP(i, 1, n) {
			REPP(j, 1, n) if (a[j] == i) pos = j;
			if (abs(pos - st) < abs(pos - en)) {
				cnt += abs(pos - st);
				while (pos > st) swap(a[pos - 1], a[pos]), pos--;
				st++;
			}
			else {
				cnt += abs(pos - en);
				while (pos < en) swap(a[pos], a[pos + 1]), pos++;
				en--;
			}
		}
		printf("Case #%d: %d\n", ca++, cnt);
	}


	return 0;
}
