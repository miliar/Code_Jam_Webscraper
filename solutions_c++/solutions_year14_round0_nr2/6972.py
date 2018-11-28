#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		long double C,F,X,C2=2.0;
		cin>>C>>F>>X;
		double ans=0.0;
		while(1){
			double ans1=ans+X/C2;
			ans=ans+C/C2;
			C2=C2+F;
			if(ans+X/C2>ans1){
				ans=ans1;
				break;
			}
		}
		printf("Case #%d: %.10Lf\n",t,ans);
	}
	return 0;
}