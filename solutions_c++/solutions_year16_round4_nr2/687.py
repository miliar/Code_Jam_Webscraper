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

const int maxn = 215;
double P[maxn];
double p[maxn];
double dp[maxn][maxn];
int n, K, half;

double calc() {
	memset(dp, 0, sizeof(dp));
	dp[0][half] = 1.0;
	
	rep(i, 0, K) {
		rep(j, 0, K+1) {
			if (dp[i][j] == 0) continue;
			
			// p[i] vote yes
			if (j+1 <= K)
				dp[i+1][j+1] += dp[i][j] * p[i];
			if (j-1 >= 0)
				dp[i+1][j-1] += dp[i][j] * (1.0 - p[i]);
		}
	}
	
	return dp[K][half];
}

void solve() {
	half = K / 2;
	double ans = 0, tmp;
	
	sort(P, P+n);
	
	rep(i, 0, n) {
		int id = i;
		rep(j, 0, K) {
			p[j] = P[id++];
			if (id >= n) id = 0;
		}
		
		tmp = calc();
		ans = max(ans, tmp);
	}
	// for (int j=n-1,i=0; i<half; ++i,--j) p[m++] = P[j];
	
	
	printf("%.12lf\n", ans);
}

int main() {
	ios::sync_with_stdio(false);
	// #ifndef ONLINE_JUDGE
		// freopen("data.in", "r", stdin);
		// freopen("data.out", "w", stdout);
	// #endif
	
	int t;
	
	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%d%d", &n,&K);
		rep(i, 0, n) {
			scanf("%lf", &P[i]);
		}
		printf("Case #%d: ", tt);
		solve();
	}
	
	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
