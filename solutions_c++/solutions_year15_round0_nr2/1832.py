#include <cstdio>
#include <algorithm>

using namespace std;

int pancakes[1000];

int main()
{
	int t;
	scanf("%d", &t);
	for (int c=1; c<=t; ++c)
	{
		int dinerCount;
		scanf("%d", &dinerCount);

		for (int i=0; i<dinerCount; ++i)
		{
			scanf("%d", &pancakes[i]);
		}

		int minMinutes = 1000;
		for (int maxPancakeCount = 1000; maxPancakeCount >= 1; --maxPancakeCount)
		{
			int specialMinutes = 0;
			for (int j=0; j<dinerCount; ++j)
			{
				if (pancakes[j] > maxPancakeCount)
				{
					specialMinutes += (pancakes[j] + maxPancakeCount - 1) / maxPancakeCount - 1;
				}
			}

			int maxPancakeCountAfterSpecialMinutes = min(maxPancakeCount, *max_element(pancakes, pancakes + dinerCount));
			int minutes = specialMinutes + maxPancakeCountAfterSpecialMinutes;

			if (minutes < minMinutes)
			{
				minMinutes = minutes;
			}
		}
		
		printf("Case #%d: %d\n", c, minMinutes);
	}
	
	return 0;
}