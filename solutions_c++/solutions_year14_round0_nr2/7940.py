#include<stdio.h>
int main()
{
	int num,test;
	double add;//每秒增加的餅乾
	double farm;//蓋工廠花多少
	double goal;
	double time;
	double c1,c2;
	double nowadd;
	double now;
	FILE *st; 
	scanf("%d",&test);
	st=fopen("b.txt","w+");
	for(num=1;num<=test;num++)
	{
		time=0.0;
		now=0.0;
		nowadd=2.0;
		scanf("%lf %lf %lf",&farm,&add,&goal);
		if(goal<farm)
		{
			time = goal/nowadd;
		}
		else
		{
			time += (farm/nowadd);
			now = farm;
			while(1)
			{
				c1=(goal-farm)/nowadd;
				c2=goal/(nowadd+add);
				if (c1<c2)
				{
					time+=c1;
					break;					
				}
				else
				{
					now=farm;
					nowadd+=add;
					time+=farm/nowadd;										
				}
			}
		}
		fprintf(st,"Case #%d: %.7lf\n",num,time);
	}
}
