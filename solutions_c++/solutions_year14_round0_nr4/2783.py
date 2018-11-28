#include <cstdio>
#include <algorithm>

using namespace std;

int main(void)
{
	int casis;
	int size;
	float naomi[1000] = {0,};
	float ken[1000] = {0,};
	float kentemp[1000] = {0,};
	int fwar = 0;
	int swar = 0;
	int c, i, j, k;

	freopen("D-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	
	scanf("%d", &casis);

	for(c = 0; c < casis; c++)
	{
		fwar = 0;
		swar = 0;

		scanf("%d", &size);
	
		for(i = 0; i < size; i++)
			scanf("%f", &naomi[i]);
		for(i = 0; i < size; i++)
			scanf("%f", &ken[i]);

		sort(naomi, naomi + size);
		sort(ken, ken + size);
		for(i = 0; i < size; i++)
			kentemp[i] = ken[i];

		for(i = 0; i < size; i++)
		{
			k = false;

			for(j = 0; j < size; j++)
				if(naomi[i] < kentemp[j])
				{
					kentemp[j] = 0;
					k = true;
					break;
				}

			if(k == false)
				fwar++;
		}

		for(i = 0; i < size; i++)
			kentemp[i] = ken[i];

		for(i = 0; i < size; i++)
		{
			k = false;

			for(j = 0; j < size; j++)
				if(kentemp[j] < naomi[i])
				{
					kentemp[j] = 1;
					k = true;
					break;
				}

			if(k == true)
				swar++;
		}

		printf("Case #%d: %d %d\n", c + 1, swar, fwar);
	}
}