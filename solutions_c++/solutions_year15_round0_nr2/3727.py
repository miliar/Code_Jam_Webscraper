#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAX_N = 1005;
int T, ans;
int D, P[MAX_N];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);

	for (int i = 0; i < T; ++i)
	{
		int maxp = -1;
		scanf("%d", &D);
		for (int j = 0; j < D; ++j)
		{
			scanf("%d", &P[j]);
			maxp = max(maxp, P[j]);
		}
		ans = -1;
		int tt = -1;
		for (int j = 1; j <= maxp; ++j)
		{
			int res = j;
			for (int k = 0; k < D; ++k)
			{
				if (P[k] > j)
				{
					res = res + ceil(double(P[k])/(double)j) - 1;
					/* code */
				}
				/* code */
			}
			if (ans == -1 || ans > res)
			{
				ans = res;
				tt = j;
				/* code */
			}
			/* code */
		}
		printf("Case #%d: %d\n", i+1, ans);
		/* code */
	}

}