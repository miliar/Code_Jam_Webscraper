#include<iostream>
#include<stdio.h>
using namespace std;
void program(int no)
{
	double c,f,x;
	double farm_count=0,total_farm_time=0,time_for_farm=0,best_time=0,rate=2,new_time=0;
	cin>>c>>f>>x;
/*
	best_time=x/rate;
	while(1)
	{
		time_for_farm=farm_count+(c/rate)+(x/(rate+f));
		if(time_for_farm<best_time)
		best_time=time_for_farm;
		else
		break;
	}
	*/
	best_time=x/rate;
	while(1)
	{
		time_for_farm =farm_count+(c/rate)+(x/(rate+f));
		if(best_time>time_for_farm)
		{
			farm_count+=c/rate;
			rate+=f;
			best_time=time_for_farm;
			continue;
		}
		break;
	}
	printf("Case #%d: %0.7lf\n",no,best_time);
}

      


int main()
{
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	program(i);
	return 0;
}