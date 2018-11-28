/*
	iafir
*/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int tc,t,n;
double x,c,f,time;

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&tc); t=1;
	while(t<=tc)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		time = 0.0; n = 0;
		while(x*f>c*(2+(n+1)*f))
		{
			time += c/(2+n*f);
			n++;
		}
		time += x/(2+n*f);
		printf("Case #%d: %.7lf\n",t,time);
		t++;
	}
	return 0;
}
