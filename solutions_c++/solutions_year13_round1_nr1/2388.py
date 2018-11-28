#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long i64;
double r,t;
i64 half()
{
	i64 x=0,y=2000000000000000000LL;
	while(x<y)
	{
		i64 mid=y-(y-x)/2;
		double tmp=mid;
		if(tmp*(2*r-3)+2*(tmp+1)*tmp<=t)
			x=mid;
		else
			y=mid-1;
	}
	return x;
}
int main()
{
	int tes;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>tes;
	for(int h=1;h<=tes;++h)
	{
		cin>>r>>t;
		cout<<"Case #"<<h<<": ";
		if(2*r+1>t)
            cout<<0<<endl;
        else
            cout<<half()<<endl;
	}
	return 0;
}
