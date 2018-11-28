#include<iostream>
#include<cstdio>
#include<cmath>
#include<map>
#include<cstring>
#include<string>
using namespace std;
int main()
{
	int Total_kase=0,kase=0,i=0;
	double C=0,F=0,X=0;
	double current_rate;
    double increased_rate=0,time_elapsed=0,time_wait=0,time_buy_wait=0;
	freopen("B-large.in","r",stdin);
    freopen("output_file.out","w",stdout);
	scanf("%d",&Total_kase);
	for(kase=0;kase<Total_kase;kase++)
	{
		C=0;F=0;X=0;
		scanf("%lf%lf%lf",&C,&F,&X);
		current_rate=2;
		if(X<C)
		{
			time_elapsed=X/current_rate;
			printf("Case #%d: %lf\n",kase+1,time_elapsed);
			current_rate=2;
			time_elapsed=0;
			continue;
		}

		time_wait=X/current_rate;
		time_buy_wait=(C/current_rate)+(X/(current_rate+F));
		
		for(i=0;time_wait>time_buy_wait;i++)
		{
			
				time_elapsed=time_elapsed+(C/current_rate);
				current_rate=current_rate+F;
		        time_wait=(X/current_rate);
		        time_buy_wait=(C/current_rate)+(X/(current_rate+F));

		}

		    time_elapsed=time_elapsed+(X/current_rate);
			printf("Case #%d: %lf\n",kase+1,time_elapsed);
			current_rate=2;
		    time_elapsed=0;
	
		

	}

	return 0;
}