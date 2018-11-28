#include <cstdio>
#include <set>
#include <algorithm>

using namespace std;

int tab[2000][2000];
int main()
{
	int t;
	scanf("%d", &t);
	int z = t;
	
	
	
	for (int i = 1; i <= 1000; i++)
	for (int j = 1; j <= 1000; j++)
	tab[i][j] = -1;
	
	for (int i = 1; i <= 1000; i++)
	{
		for (int k = 1; k <= i; k++)
		{
			if (tab[i][(i + k - 1) / k] == -1)
			  tab[i][(i + k - 1) / k] = k - 1;
		   else
		    tab[i][(i + k - 1) / k] = min(tab[i][(i + k - 1) / k], k - 1);
		}
		for (int k = 2; k <= i; k++)
		{
			if (tab[i][k] == -1) tab[i][k] = tab[i][k - 1];
		}
		
	}

	while (t--)
	{
		set<int> S;
		int d, p;
		int pan[2000];
		scanf("%d", &d);
		for (int i = 0; i < d; i++)
		{
			scanf("%d", pan + i);
			S.insert(pan[i]);
		}
		
		int best = 1000;
		for (int i = 1; i <= *S.rbegin(); i++)
		{
			int m = *S.rbegin();
			int s = 0;
			for (int j = 0; j < d; j++)
			{
        if (pan[j] > i)  
				  s += tab[pan[j]][i];
			}
			s += i;
			best = min(best, s);
		}
		printf("Case #%d: %d\n", z - t, best);
	}
	
	return 0;
}
