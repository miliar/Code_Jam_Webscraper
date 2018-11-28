#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include <iomanip>
#include<cmath>
using namespace std;

int main()
{
	int n,k;
	double c,f,x,t1,t2,t,r,ans;
	cin>>n;
	for(k=1;k<=n;k++)
	{
		cin>>c>>f>>x;
		t=0;	t1=0;	t2=0;
		if(x>c)
		{
			r=2;
			t=0;
			while(1)
			{
				t1=(c/r)+(x/(f+r));
				t2=x/r;
				if(t2<=t1)
				{
					ans=t+t2;
					break;
				}
				t+=c/r;
				r+=f;
			}
		}
		else
			ans=x/2;
		//printf("Case #%d: %.7lf\n",k,ans);
		std::cout << std::fixed;
		cout<<setprecision(7)<<"Case #"<<k<<": "<<ans<<endl;

	}
}