#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int get_best(double *a, double *b, int n)
{
	bool flag[n];
	for (int k = 0; k < n; k++)
	{
		flag[k] = 0;
	}

	int result = 0;
	for (int k = 0; k < n; k++)
	{
		int mint = -1;
		double minv = 1;
		for (int t = 0; t < n; t++)
		{
			if (flag[t]) continue;
			if (b[t] > a[k] && b[t] < minv)
			{
				minv = b[t];
				mint = t;
			}
		}
		
		if (mint == -1)
		{
			for (int t = 0; t < n; t++)
			{
				if (!flag[t])
				{
					flag[t] = 1;
					break;
				}
			}
		} else {
			result++;
			flag[mint] = 1;
		}
	}
	return result;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int n;
		cin >> n;
		double a[n], b[n];
		for (int k = 0; k < n; k++)
		{
			cin >> a[k];
		}
		for (int k = 0; k < n; k++)
		{
			cin >> b[k];
		}
		sort(a, a + n);
		sort(b, b + n);
		
		printf("Case #%d: %d %d\n", t, get_best(b, a, n), n - get_best(a, b, n));
	}
	return 0;
}
