#include <iostream>
#include<iomanip>
#include<cstdio>
using namespace std;

int main()
{
	double c,f,x,t_el,mn_t,nw_t;
	long long int h,t,k,p;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>c>>f>>x;
		nw_t=x/2;
		mn_t=1000000;
		//cout<<nw_t<<" ";
		h=0;
		t_el=0;
		p=0;
		while(mn_t>=nw_t)
		{
			p++;
			//cout<<"boo";
			mn_t=nw_t;
			t_el+=c/(2+h*f);
			h++;
			nw_t=t_el+x/(2+h*f);
		}
		//cout<<p<<" ";
		cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<mn_t<<endl;
	}
	return 0;
}