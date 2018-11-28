#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int tc=t;
	while(t--)
	{
		double c,f,x,d,b,ans=0.0;
		cin>>c>>f>>x;
		double count=2.0;
		d=x/count;
		b=0.0;
		while(1)
		{
			d=x/count;
			b=c/count;
			count+=f;
			b+=x/count;
			if(d>=b)
				ans+=c/(count-f);
			else
			{
				ans+=d;
				break;
			}
		}
		printf("Case #%d: %0.7f\n",tc-t,ans);
	}
	return 0;
}