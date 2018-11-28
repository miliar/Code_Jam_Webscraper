#include <cstdio>
int main()
{
	int T,i=1;
	double C,F,X;
	double all_cookie,tot_time,new_farm,rate;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		new_farm=0;
		rate=2;
		all_cookie=X/rate;
		while(1)
		{
			new_farm+=C/rate;
			rate+=F;
			tot_time=new_farm+X/rate;
			if(all_cookie>tot_time)
			{
				all_cookie=tot_time;
			}
			else
			{
				break;
			}
		}
		printf("Case #%d: %.7lf\n",i,all_cookie);
		i++;
	}
	return 0;
}

		
