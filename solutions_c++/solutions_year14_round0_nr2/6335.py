#include<bits/stdc++.h>
using namespace std;
int main()
{
	int T,t;
	double C,F,X,ans,r;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>C>>F>>X;
		ans = 0;
		if(X <= C)
		{
			ans = X/2.0;
		}
		else
		{
			r = 2;
			while(C/r + X/(r+F) < X/r)
			{
				ans += C/r;
				r += F;
			}
			ans += X/r;
		}
		printf("Case #%d: %.7f\n",t,ans);
	}
	return 0;
}
