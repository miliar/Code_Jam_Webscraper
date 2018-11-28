#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
struct ime{
	double t1;
	double t2;
};
int main()
{
//  freopen("data.txt","r",stdin);
	double c,f,x;
	int n,i;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		
		double num=0,time1=0,p=2;
		ime a;
		ime b;
		cin>>c>>f>>x;
		a.t1=c/p;
		a.t2=x/p;
		b.t1=a.t1+c/(p+f);
		b.t2=a.t1+x/(p+f);
		p=p+f;
		while(b.t2<a.t2)
		{
			p=p+f;
			a.t1=b.t1;
			a.t2=b.t2;
			b.t1=a.t1+c/p;
			b.t2=a.t1+x/p;
			
		}
		
		cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<a.t2<<endl;
	}
}
