#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int kase = 1, t;
	scanf("%d",&t);
	while(t--)
	{
		double c,f,x,m;
		scanf("%lf %lf %lf",&c,&f,&x);
		m = (x/c) - (2/f);
		int farms = (int)(m+1.0000000) - 1;
		farms = farms<0?0:farms;
		double time = 0.0000000;
		for(int i=0; i< farms; i++)
		{
			time+= c/(2.0000000 + i*f);
		}
		time += x/(2.0000000 + farms*f);
		printf("Case #%d: ",kase);
		printf("%.7lf\n",time);
		kase++;
	}
	return 0;
}
