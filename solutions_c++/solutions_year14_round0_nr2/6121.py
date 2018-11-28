#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	double c,f,x;

	int kase;

	scanf("%d",&kase);

	for(int k=1;k<=kase;k++)
	{
		double current_time=0,current_speed=2;
		scanf("%lf %lf %lf",&c,&f,&x);
		double reach_x_time=x/current_speed;
		double add_x_time=(c/current_speed)+(x/(current_speed+f));
		while(reach_x_time>add_x_time)
		{
			current_time+=c/current_speed;
			current_speed+=f;
			reach_x_time=x/current_speed;
			add_x_time=(c/current_speed)+(x/(current_speed+f));
		}
		current_time+=reach_x_time;
		printf("Case #%d: %.7lf\n",k,current_time);

	}

	return 0;
}
