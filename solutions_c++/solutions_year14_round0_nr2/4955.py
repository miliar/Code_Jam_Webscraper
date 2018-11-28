#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int t,j=1,flag;
	double c,f,x,rate,ans,t1,t2,t3;
	cin>>t;
	while(j<=t)
	{
		rate=2.;ans=0.;flag=1;
		cin>>c>>f>>x;
		while(flag)
		{
			t1=x/rate;
			t2=c/rate;
			t3=x/(rate+f);
			if(t1>t2+t3)
			{
				ans+=t2;
				rate+=f;
			}
			else
			{
				ans+=t1;
				flag=0;
			}
		}
		cout<<"Case #"<<j<<": ";
		std::cout << std::fixed << std::setprecision(7) << ans<<"\n";
		j++;
	}
	return 0;
}
