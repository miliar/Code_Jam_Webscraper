#include <iostream>
#include <algorithm>
#include <set>
#include <iomanip>

using namespace std;

int main()
{
	int t,a;
	cin>>t;
	for(a=1;a<=t;a++)
	{
		double c,f,x,time=0.0,r=2.0,tmp;
		cin>>c>>f>>x;;
		int n;
		tmp=((x*f-c*(r+f))/(c*f));
		n=(int)tmp;
		// cout<<"n = "<<n<<"   float = "<<((x*f-c*(r+f))/(c*f))	<<endl;
		if(tmp>=0)
		{
			for(int i=0;i<=n;i++)
				time+=c/(r+i*f);
			time+=x/(r+(n+1)*f);
		}
		else
			time=x/2.0;
			cout.setf(ios_base::fixed, ios_base::floatfield);
		cout<<setprecision(7)<<"Case #"<<a<<": "<<time<<endl;
	}
}