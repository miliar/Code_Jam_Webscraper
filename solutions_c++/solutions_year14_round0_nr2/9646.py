#include<stdio.h>

int main()
{
	long double c,f,x,time,denom,temp_time;
	int t,count,i;
	scanf("%d",&t);
	while(t--)
	{
		count=1;
		
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		time=x/2;
		
		while(1)
		{
			denom=2;
			temp_time=0;
			for(i=0;i<count;i++)
			{
				temp_time+=c/denom;
				denom+=f;
			}
			
			temp_time+=x/denom;
			
			if(time>temp_time)
			time=temp_time;
			
			else
			break;
			
			count++;
		}
		
		printf("%.7Lf\n",time);
	}
	return 0;
}
