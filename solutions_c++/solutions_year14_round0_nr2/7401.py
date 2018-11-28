#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int t, i=0, j=0;
	scanf("%d",&t);
	int tt=0;
	while(t--)
	{
		tt++;
		float c, f, x, previous_time=1.0, after_time=0.0, expected;
		float  catt=0.0, rate=2.0, total_time=0.0;
		float k=0.0000000001;
		int done=0;

		scanf("%f%f%f",&c,&f,&x);
		while (previous_time>after_time)
		{
			

			if(done==0)
			{
				expected = c/rate;
				total_time = total_time + expected;
				catt = catt + c;
				done = 1;
			}
			
		
			
			if(catt>=c)
			{
				done=0;
				previous_time = total_time + ((x-c)/rate);
				after_time = total_time + ((x)/(rate+f));
			
				if (previous_time>after_time)
				{
					rate = rate + f;
					catt=0;
				}
			}
			
			//if(done==1)
			//{
			//	total_time=total_time+k;
			//	catt=catt+(k*rate);
			//}

		}
		
		printf("Case #%d: %.7f\n", tt, previous_time);
	}
	return 0;
}