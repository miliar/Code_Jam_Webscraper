#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		double c,f,x,time=2.0,ans=0.0;
		cin>>c>>f>>x;
		while((x/time) > (c/time)+(x/(f+time)))
		{
			ans+=c/time;
			time+=f;
		}
		ans+=x/time;
		printf("Case #%d: %lf\n",i,ans);
	}
	return 0;
}
