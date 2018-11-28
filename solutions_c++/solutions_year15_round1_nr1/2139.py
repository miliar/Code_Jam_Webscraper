#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1002;

int a[N];

int main()
{
	int i, t, n, m1, m2;
	int m2_v; // need to divde by 10
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		m1 = m2 = 0;
		m2_v = 0;
		scanf("%d", &n);
		scanf("%d", &a[0]);
		for (i = 1; i < n; i++)
		{
			scanf("%d", &a[i]);
			if (a[i-1] > a[i])
			{
				m1 += a[i-1] - a[i];
				m2_v = max(m2_v, a[i-1] - a[i]);
			}
		}
 		for (i = 1; i < n; i++)
			if (a[i-1] >= m2_v)
				m2 += m2_v;
			else
				m2 += a[i-1];
		printf("Case #%d: %d %d\n", cases, m1, m2);
	}
	return 0;
}

