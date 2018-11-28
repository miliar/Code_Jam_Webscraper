#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t,tc=1;
	double c,f,x,tm,cr;
	freopen("B-large.in","r",stdin);
	freopen("o.txt","w",stdout);
	scanf("%d",&t);
	while(tc<=t)
	{
		tm=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: ",tc);
		if(x<=c)
		{
			printf("%0.07lf\n",x/2.0);
		}
		else
		{
			cr=2.0;
			while(1)
			{
				if(x/cr<=x/(cr+f)+c/cr)
				{
					tm+=x/cr;
					printf("%0.07lf\n",tm);
					break;
				}
				else
				{
					tm+=c/cr;
					cr+=f;
				}
			}
		}
		tc++;
	}
	fclose(stdin);
	fclose(stdout);
}
