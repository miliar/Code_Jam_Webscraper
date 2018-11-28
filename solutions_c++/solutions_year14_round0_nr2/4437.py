#include <bits/stdc++.h>
using namespace std;
#define eps 1e-7
#define MAXN 1000010
double dp[MAXN];
double Calc(double C,double F,double X)
{
	dp[0] = X/2;
	double Ans = dp[0];
	for(int i = 1;i<=X;i++)
	{
		dp[i] = dp[i-1] - X/((i-1)*F + 2.0) + C/((i-1)*F + 2.0) + X/(i*F+2);
		Ans = min(Ans,dp[i]);
	}
	return Ans;
}
int main()
{
	int Tests;
	cin>>Tests;
	for(int t = 1; t <= Tests; t++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		cout<<"Case #"<<t<<": ";
		printf("%.7f\n",Calc(C,F,X));
	}
	return 0;
}