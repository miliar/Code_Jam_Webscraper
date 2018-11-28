#include <iostream>
#include <math.h>
using namespace std;

 long double pi=3.1415926;
bool is_ok(long double r,long double t)
{
	double area=2*r+1;
	if (t>=area)
		return true;
	else 
		return false;
}
int main()
{
	int T;
	cin>>T;
	long double r,t;
	int ca=0;
	while(T--)
	{
		ca++;
		cin>>r>>t;
		long long  cnt=0;
		long double rr=(-(2*r-1)+sqrt((2*r-1)*(2*r-1)+8*t))/4.0;
//		long double ll=(2*r-1)*(2*r-1)-8*t/4;
		cnt=(long long )(rr);
		long long tmp_cnt=floor(rr);
		cout<<"Case #"<<ca<<": ";
		cout<<cnt<<endl;
	}
	return 0;
}
