//#define LOCAL
#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std; 
int main()
{
	#ifdef LOCAL
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		double c,x,f,sum=0.0000000;
		cin>>c>>f>>x;
		int n=int(floor((x*f-2.0*c)/c/f));
		if(n<=0)sum+=x/2.0;
		else
		{
			for(int j=0;j<n;j++)
				sum+=c/(2.0+j*f);
			sum+=x/(2.0+n*f);
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<setiosflags(ios::fixed)<<setprecision(7)<<sum<<endl;
	}
	return 0;
}
