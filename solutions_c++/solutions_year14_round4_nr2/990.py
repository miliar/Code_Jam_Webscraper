#include <cstdio>
#include <algorithm>

using namespace std;

int n;

int tab[10005];

int przyp()
{
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		scanf("%d", tab + i);
	int wyn = 0;
	int p = 1, k = n;
	for(int i = 1; i <= n; i ++)
	{
		int najm = 1e9, poz = 0;
		for(int j = p; j <= k; j++)
		{
			if(tab[j] < najm)
			{
				najm = tab[j];
				poz = j;
			}
		}
		if(k - poz < poz - p)
		{
			for(int i = poz + 1; i <= k; i++)
			{
				swap(tab[i - 1], tab[i]);
				wyn++;
			}
			k--;
		}
		else
		{
			for(int i = poz - 1; i >= p; i--)
			{
				swap(tab[i], tab[i + 1]);
				wyn++;
			}
			p++;
		}
	}
	return wyn;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, przyp());
	return 0;
}
