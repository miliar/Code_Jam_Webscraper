#include <iostream>
#include <stdio.h>
using namespace std;
int T,t;
double c,f,x,time,cc,ntime,count,btime;

int main()
{
	
	FILE * out = fopen("B-small-attempt0.out","w");
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(t=1; t<=T; t++)
	{
		cin>>c>>f>>x;
		time = 987654321;
		ntime =x/2;
		cc= 2;
		count = 1;
		btime = 0;
		while(time>ntime)
		{
			time = ntime;
			btime += c/cc;
			ntime = btime;
			count++;
			cc+=f;
			ntime += x/cc; 

		}
		printf("Case #%d: %.7lf\n",t,time);

	}

}