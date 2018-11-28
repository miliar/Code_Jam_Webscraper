/*  */
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <deque>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>
#include <functional>
#include <iterator>
#include <iomanip>
using namespace std;
//#pragma comment(linker,"/STACK:102400000,1024000")

#define sti				set<int>
#define stpii			set<pair<int, int> >
#define mpii			map<int,int>
#define vi				vector<int>
#define pii				pair<int,int>
#define vpii			vector<pair<int,int> >
#define rep(i, a, n) 	for (int i=a;i<n;++i)
#define per(i, a, n) 	for (int i=n-1;i>=a;--i)
#define clr				clear
#define pb 				push_back
#define mp 				make_pair
#define fir				first
#define sec				second
#define all(x) 			(x).begin(),(x).end()
#define SZ(x) 			((int)(x).size())
#define lson			l, mid, rt<<1
#define rson			mid+1, r, rt<<1|1

const int maxn = 30;
int g[maxn][maxn], gg[maxn][maxn];
int a[maxn];
bool visit[maxn];
int bits[1<<16];
char s[maxn];
int n, tot;

int getBits(int x) {
	int ret = 0;
	
	while (x) {
		ret += x & 1;
		x >>= 1;
	}
	
	return ret;
}

void init() {
	const int mst = 1<<16;
	rep(i, 0, mst)
		bits[i] = getBits(i);
}

bool dfs(int dep) {
	if (dep == n) return true;
	
	int u = a[dep], c = 0;
	
	rep(v, 0, n) {
		if (visit[v] || !gg[u][v]) continue;
		++c;
		visit[v] = true;
		if (!dfs(dep+1)) return false;
		visit[v] = false;
	}

	return c > 0;
}

bool judge(int st) {
	int c = 0;
	
	rep(i, 0, n) {
		rep(j, 0, n) {
			if (st & (1<<c))
				gg[i][j] = 1;
			else
				gg[i][j] = 0;
			++c;
		}
	}
	
	rep(i, 0, n) a[i] = i;
	do {
		memset(visit, false, sizeof(visit));
		if (!dfs(0))
			return false;
	} while (next_permutation(a, a+n));
	
	return true;
}

void solve() {
	int ans = n*n - tot;
	
	if (ans == 0) {
		printf("%d\n", ans);
		return ;
	}
	
	const int mst = 1<<(n * n);
	int cst = 0, c = 0;
	
	rep(i, 0, n) {
		rep(j, 0, n) {
			if (g[i][j])
				cst |= 1<<c;
			++c;
		}
	}
	
	rep(st, 0, mst) {
		if ((st & cst) != cst) continue;
		if (bits[st ^ cst] >= ans) continue;
		
		if (judge(st)) {
			ans = min(ans, bits[st ^ cst]);
		}
	}
	
	printf("%d\n", ans);
}

int main() {
	ios::sync_with_stdio(false);
	// #ifndef ONLINE_JUDGE
		// freopen("data.in", "r", stdin);
		// freopen("data.out", "w", stdout);
	// #endif
	
	int t;
	
	init();
	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%d", &n);
		tot = 0;
		rep(i, 0, n) {
			scanf("%s", s);
			rep(j, 0, n) {
				g[i][j] = s[j] - '0';
				tot += g[i][j];
			}
		}
		printf("Case #%d: ", tt);
		solve();
	}
	
	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
