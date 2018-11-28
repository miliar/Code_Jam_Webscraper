#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<cstring>
#include<cmath>
using namespace std;


int main()
{
int T;
double C,F,X;
double time,cur,a,b,c,rate;
freopen("cookie.in","r",stdin);
freopen("cookie.out","w",stdout);
cin>>T;
for(int t=1;t<=T;t++)
	{
	cin>>C>>F>>X;
	time=0;
	cur=0;
	rate=2;
	while(1)
		{
		a=X/rate;
		b=(C)/rate+(X)/(F+rate);
		if(b<a)
			{
			time+=(C/rate);
			rate=F+rate;
			}
		else
			{
			time+=a;
			break;
			}
		}
	printf("Case #%d: %0.7lf\n",t,time);
	}
return 0;
}
