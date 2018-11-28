#include <bits/stdc++.h>

using namespace std;


double min_time(double c, double f, double x)
	{
		double ans = 0;
		int found = 0;
		double current_speed = 2;

		while(found == 0 )
		{
			if(x/current_speed>(c/current_speed + x/(current_speed+f)))
			{
				ans = ans+(c/current_speed);
				current_speed = current_speed+f;
				
			}

			else
				found = 1;
		}
		
		ans = ans+(x/current_speed);

		return ans;

	}



int main(void)
	{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
		


		int i,t;

		cin >> t;
	
		double c,f,x;

		for(i=0;i<t;i++)
		{
			scanf("%lf %lf %lf",&c,&f,&x);

			printf("Case #%d: %f\n",i+1,min_time(c,f,x));
		}


	}
