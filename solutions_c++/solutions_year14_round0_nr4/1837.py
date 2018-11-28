#include <stdio.h>
#include <algorithm>
using namespace std;

const int MAX = 1010;
int num;
double m1[MAX];
double m2[MAX];

int main()
{
	//freopen("D-large.in", "r", stdin);
	//freopen("D-large.out", "w", stdout);


	int nCase;
	int t, i, j;
	int ans1, ans2;
	scanf("%d", &nCase);
	for (t = 1; t <= nCase; ++ t)
	{
		scanf("%d", &num);
		for (i = 0; i < num; ++ i)
		{
			scanf("%lf", &m1[i]);
		}
		for (i = 0; i < num; ++ i)
		{
			scanf("%lf", &m2[i]);
		}
		sort(m1, m1 + num);
		sort(m2, m2 + num);
		
		ans1 = 0; i = j = 0;
		while (true)
		{
			if (i >= num || j >= num)
			{
				break;
			}
			if (m1[i] > m2[j])
			{
				ans1 ++;
				i++; j++;
			}
			else
			{
				i++;
			}
		}

		ans2 = 0; i = j = 0;
		while (true)
		{
			if (i >= num || j >= num)
			{
				break;
			}
			if (m1[i] < m2[j])
			{
				ans2 ++;
				i++; j++;
			}
			else
			{
				j++;
			}
		}
		ans2 = num - ans2;

		
		printf("Case #%d: %d %d", t, ans1, ans2);
		
		if (t < nCase)
		{
			printf("\n");
		}
	}

	//system("pause");
	return 0;
}

