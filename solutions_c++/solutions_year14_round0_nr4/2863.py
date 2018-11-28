#include <stdio.h>
#include <algorithm>

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		int n, countA = 0, countB = 0;
		double a[2000] = {0}, b[2000] = {0};
		
		scanf("%d", &n);
		
		for(int i = 0; i < n; i++)
			scanf("%lf", &a[i]);
		
		for(int i = 0; i < n; i++)
			scanf("%lf", &b[i]);
			
		std::sort(a, a + n);
		std::sort(b, b + n);
		
		bool isDel[2000] = {0};
		for(int i = 0; i < n; i++)
		{
			double min = 2.0, choice = -1.0;
			int min_index = -1, choice_index = -1;
			
			for(int j = 0; j < n; j++)
				if(!isDel[j])
				{
					if(min_index == -1)
					{
						min = b[j];
						min_index = j;
					}
					
					if(b[j] > a[i])
					{
						choice = b[j];
						choice_index = j;
						break;
					}
				}
			
			if(choice_index == -1)
			{
				choice = min;
				choice_index = min_index;
			}
			
			if(a[i] > choice)
				countA++;
			isDel[choice_index] = true;
			
		}
		
		int pB = 0;
		for(int i = 0; i < n; i++)
			if(a[i] > b[pB])
			{
				countB++;
				pB++;
			}
		
		printf("Case #%d: %d %d\n", t, countB, countA);
	}
	return 0;
}

