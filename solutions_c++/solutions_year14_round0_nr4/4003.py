#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int smallest_larger_than(vector<float> &haystack, float needle)
{
	int pos = 0;
	for(vector<float>::iterator it = haystack.begin(); it != haystack.end(); ++it)
	{
		if (*it > needle) return pos;
		++pos;
	}
	return -1;
}

int main()
{
    int T;
	int n,i,j;
	float block,block2;
	int war_points,dwar_points;
    scanf("%i", &T);
    for(int t=1; t<=T; t++)
    {
		vector<float> naomi,naomi2;
		vector<float> ken,ken2;
		scanf("%i",&n);
		for(i = 0; i < n; i++)
		{
			scanf("%f", &block);
			naomi.push_back(block);
		}

		for(i = 0; i < n; i++)
		{
			scanf("%f", &block);
			ken.push_back(block);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		naomi2 = naomi;
		ken2 = ken;
		war_points = 0;
		for(i = 0; i < n; i++)
		{
			block = naomi2[0];
			naomi2.erase(naomi2.begin());
			j = smallest_larger_than(ken2, block);
			if (j == -1)
			{
				ken2.erase(ken2.begin());
				war_points++;
			}
			else
				ken2.erase(ken2.begin()+j);
		}

		naomi2 = naomi;
		ken2 = ken;
		dwar_points = 0;
		for(i = 0; i < n; i++)
		{
			if (naomi2[0] < ken2[0])
			{
				ken2.pop_back();
			}
			else
			{
				ken2.erase(ken2.begin());
				dwar_points++;			
			}
			naomi2.erase(naomi2.begin());
		}

		printf("Case #%i: %i %i\n", t, dwar_points, war_points);
	}
}

