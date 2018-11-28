#include "stdio.h"
#include "algorithm"
#include <set>
using namespace std;

int main()
{
	int t, n;
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.ou", "wt", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &t);
		if (t == 0)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
		}
		else
		{
			set<int> c;
			int j = 0;
			int u = t;
			int temp;
			while (c.size()<10)
			{
				j++;
				u = t*j;
				int k = 10;
				int sub = 0;
				while (u>0)
				{
					temp = u % 10;
					c.insert(temp);
					u = u / 10;
					if (c.size() == 10)
						break;
				}
			}
			printf("Case #%d: %d\n", i + 1, t*j);
		}
	}
}