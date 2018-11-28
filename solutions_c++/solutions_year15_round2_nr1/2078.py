/* Aniket Kumar */
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
#include <cmath>
#include <unistd.h>
#include <algorithm>
#include <vector>
#include <map>
#include <climits>
#include <set>

using namespace std;

#define V(a) vector<a>
#define pi pair<int,int>
#define ull unsigned long long
#define ill long long
#define F(i,a,n) for(i=(a);i<(n);++i)
#define RP(i,n) F(i,0,n)
#define SUM(v, s, i) RP(i, v.size()){ s += v[i];}
#define MP(a, b) make_pair(a, b)
#define fs first
#define se second
#define S(x) scanf("%d",&x)
#define SL(x) scanf("%lld",&x)
#define SZ(x) (x.size())
#define PB(a) push_back(a)
#define dbug(i,size,x) F(i,0,size){cout<<x[i]<<" ";} cout<<endl
#define tin freopen("aain.txt","r",stdin)
#define tout freopen("aaout.txt","a",stdout)

void inp() {
#ifndef ONLINE_JUDGE
    freopen("aain.txt","r",stdin);
#endif
}

const int INF = 0x7fffffff;

ill rev(ill n) {
	ill dv, ret;

	ret = 0;

	while (n > 0) {
		dv = n % 10;
		ret = ret * 10 + dv;
		n /= 10;
	}

	return ret;

}

int dp[1000001];

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t, i;

	ill n, k, ans, num, r, can1;

	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 2;

	F(i, 3, 1000001) {

		if (i % 10 == 0) {
			dp[i] = dp[i - 1] + 1;
		} else {
			can1 = rev(i);

			if (can1 < i) {
				dp[i] = min(dp[i - 1] + 1, dp[can1] + 1);
			} else {
				dp[i] = dp[i - 1] + 1;
			}
		}

		//cout << dp[i] << endl;

	}



	S(t);

	for (i = 1; i <= t; i++) {

		k = 0;

		SL(n);

		//cout << dp[n] << endl;		


		printf("Case #%d: %d\n", i , dp[n]);

	}

	return 0;
}

