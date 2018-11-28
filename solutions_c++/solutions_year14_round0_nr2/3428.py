#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		double c,f,x,ans=0.0;
		cin>>c>>f>>x;
		double r=2.0;
		while(1)
		{
			if(x/r < ((c/r) + (x/(r+f))) )
			{
				ans+=x/r;
				break;
			}
			ans+=c/r;
			r+=f;	
		}
		cout<<"Case #"<<k<<": ";
		printf("%.7f\n",ans);
	}
	return 0;
}