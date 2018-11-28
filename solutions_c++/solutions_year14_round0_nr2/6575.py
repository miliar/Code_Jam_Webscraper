#include <stdio.h>
#include <iostream>
using namespace std;

int main(void)
{


	int test;
	int i, j, k;
	long double C, F, X;
	long double time;
	scanf("%d", &test);

	for(k=1; k<=test; k++)
	{
		scanf("%lf %lf %lf", &C, &F, &X);

		//안사면 cur*time=x
		//하나 사면 cur+F

		int much;
		int many;

		for(much=0; ; much++)
		{
			long double temp_time=0;
			if(much==0)
				time=X/2;
			else
			{
				for(many=0; many<much; many++)
				{
					temp_time+=C/(2+F*many);
				}
				temp_time+=X/(2+F*much);

				if(temp_time<time)
				{
					time=temp_time;
					
				}
				else if(temp_time>time)
				{
					break;
				}




			}


		}

		printf("Case #%d: %.7f\n", k, time);

	}

	return 0;
}