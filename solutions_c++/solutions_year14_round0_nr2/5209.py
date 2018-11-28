#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		double c, x, f, rate = 2, ans=0;
		cin>>c>>f>>x;
		if(c>=x)
		{
			ans=x/2;
		}
		else
		{
			while(1)
			{
				if((c/rate)+(x/(rate+f))>=(x/rate))
				{
					ans+=(x/(rate));
					break;
				}
				ans+=(c/rate);
				rate+=f;
			}
		}
		cout<<"Case #"<<i<<": ";
		printf("%.7lf\n",ans);
	}
	return 0;
}
