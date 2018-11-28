/* Vipul Jain */

#include <bits/stdc++.h>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FB(i,a,n) for(int i=(a);i>=(n);--i)
#define FI(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define Su(x) scanf("%llu",&x)
#define Sf(x) scanf("%f",&x)
#define Sd(x) scanf("%lf",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define fi first
#define se second

int dp[1000010];

int reverse_num(int number)
{
	int reverse = 0;
	for( ; number!= 0 ; ) {
		reverse = reverse * 10;
		reverse = reverse + number % 10;
		number = number / 10;
	}
	return reverse;
}


void pre()
{
	dp[1] = 0;
	F(i, 2, 1000010) {
		if (i % 10 == 0) {
			dp[i] = dp[i - 1] + 1;
			continue;
		}
		int reverse = reverse_num(i);
		if (reverse >= i) {
			dp[i] = dp[i - 1] + 1;
			continue;
		}
		dp[i] = min(dp[i - 1] + 1, dp[reverse] + 1);
	}
}

int main()
{
	pre();
	int t;
	S(t);
	int cases = 0;
	while (t--) {
		cases++;
		int n;
		S(n);
		printf("Case #%d: %d\n", cases, dp[n] + 1);
	}
    return 0;
}