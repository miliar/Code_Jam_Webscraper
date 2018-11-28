#include <stdio.h>
#include <algorithm>

const int N = 1005;

inline int abs(int x) { return x < 0 ? -x : x; }

int main()
{
	int T, c;
	int n, a[N], x[N], i, j, k, ans, sum, mi, cnt; 
	bool check, flag;

	scanf("%d", &T);
	for (c = 1; c <= T; c++)
	{
		scanf("%d", &n);
		mi = 0;
		for (i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			if (a[i] > a[mi]) mi = i;
			x[i] = i;
		}

		ans = n * n;

		do {
			flag = true;
			check = (x[0] == mi);
			for (i = 1; i < n; i++)
			{
				if (a[x[i-1]] < a[x[i]] == check)
				{
					flag = false;
					break;
				}
				if (x[i] == mi) check = !check;
			}
			if (!flag) continue;

			sum = 0;
			for (i = 0; i < n; i++)
				for (j = i + 1; j < n; j++)
					if (x[j] < x[i])
						sum++;
			if (sum < ans) ans = sum;
		} while (std::next_permutation(x, x+n));
		
		printf("Case #%d: %d\n", c, ans);
	}


	return 0;
}
