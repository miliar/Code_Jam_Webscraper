#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

typedef long long ll;
const int M = 10000002;

ll dp[M] , a, b;

bool judge(ll n)
{
	int tmp[30], len = 0;
	while(n)
	{
		tmp[len ++] = n%10;
		n /= 10;
	}
	for(int i=0;i*2<len;i++)
		if(tmp[i] != tmp[len-i-1])
			return false;
	return true;
}

void init(int n)
{
	memset(dp, 0, sizeof(dp));
	ll cot = 0;
	for(ll i=1;i<=n;i++)
	{
		if(judge(i) && judge(i*i))
			cot = dp[i] = cot + 1;
		else
			dp[i] = cot;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	init(M);
	for(int cas=1;cas<=T;cas++)
	{
		scanf("%lld %lld", &a, &b);
		if(a > b)
			swap(a, b);
		int t1 = sqrt(a), t2 = sqrt(b);
		if(t1 * t1 == a)
			t1 --;
		printf("Case #%d: %lld\n",cas,dp[t2]-dp[t1]);
	}
	return 0;
}
