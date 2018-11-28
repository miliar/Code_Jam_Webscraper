#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int t;
	double c,f,x,r,totaltime,r2;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		totaltime=0;
		scanf("%lf%lf%lf",&c,&f,&x);
		r=2;
		while(true)
		{
			if(c/r + x/(r+f)>(x/r))
			{
				totaltime+=(x/r);
				break;
			}
			else
			{
				totaltime+=(c/r);
			}
			r = r+f;
		}
		printf("Case #%d: %0.7f\n",(i+1),totaltime);
	}
	return 0;
}