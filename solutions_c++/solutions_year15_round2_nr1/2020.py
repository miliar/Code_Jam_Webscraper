#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
typedef long long int ll;
using namespace std;
int dp[1000043];
int reverse(int n) 
{
	int a[15];
	int t = n;
	int len = 0;
	int in = 0;
	//cout << t << endl;
	while(t != 0) {
		a[in] = t % 10;
		in++;
		t = t/10;
		//cout << t << endl;
	}
	int pow = 1;
	int re = 0;
	int t1 = in-1;
	//cout << in << endl;
	while(t1 >= 0) {
		re += a[t1] * pow;
		pow = pow * 10;
		t1--;
	}
	return re;
}
ll solve()
{
	dp[1] = 1;
	//memset(dp, -1, sizeof(dp));
	for(int i = 2;i <= 1000002;i++) {

		if(i % 10 == 0) {
			dp[i] = dp[i-1] + 1;
			continue;
		}
		int t1 = reverse(i);
		if(t1 >= i) {
			dp[i] = dp[i-1] + 1;
			continue;
		}else {
			dp[i] = min(dp[i-1] + 1, dp[t1] + 1);
		}
		
	}
	return 0;
	//ll ans = min(ans1, ans2);
	//return ans;
}
int main()
{
	int i;
	//freopen();
	int cases;
	cin >> cases;
	solve();
	for(int i1 = 1;i1 <= cases;i1++) {
		int n;
		cin >> n;
		printf("Case #%d: %d\n", i1, dp[n]);
	}
	return 0;
}
