#include <stdio.h>
#include <math.h>


int main()
{
	int t;
	int max, d, p;
	int plates[1000];

	scanf("%d\n",&t);

	for(int tt=0;tt<t;tt++)
	{
		scanf("%d",&d);
		max = 0;
		for(int i = 0;i < d; i++)
		{
			scanf(" %d",&p);
			plates[i] = p;
			if(p>max)
			{
				max = p;
			}
		}
		int result = max;
		int prevSteps = result;
		bool hasMinimum = false;
		for(int k = 2;k < max;k++)
		{
			int steps = k;
			for(int i=0;i<d;i++)
			{
				if(plates[i]>k)
				{
					steps+=plates[i]/k;
					if(plates[i]%k == 0 )
                    {
                        steps--;
                    }
				}
			}
			
			if(result > steps )
			{
				result = steps;
			}

		}
		printf("Case #%d: %d\n",tt+1,result);
	}
	return 0;
}
