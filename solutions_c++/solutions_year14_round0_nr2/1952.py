#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;
int main()
{
long double c,f,x;
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
	cin>>c>>f>>x;
	long double ans=0.0000000,curd=2.000000,xx;
	xx=x/(curd+f)-(x-c)/curd;
	while(xx<0)
	{
		ans=ans+c/curd;
		curd=curd+f;
		xx=x/(curd+f)-(x-c)/curd;
	}
	ans=ans+x/curd;
	cout<<"Case #"<<i<<": ";
	int yy=0;
	while(pow(10,yy)<=ans)
	{
		yy++;
	}
	std::cout<<std::setprecision(yy+7)<<ans<<endl;
}
return 0;
}
