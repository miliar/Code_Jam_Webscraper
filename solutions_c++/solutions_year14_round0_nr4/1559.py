#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

#define INF 0x7fffffff

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int T, cs;
	scanf("%d", &T);
	for (cs = 1; cs <= T; ++cs)
	{
		int n, i, j;
		deque<int> da, db;
		double t;
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
		{
			scanf("%lf", &t);
			da.push_back(int(t * 100000));
		}
		for (i = 0; i < n; ++i)
		{
			scanf("%lf", &t);
			db.push_back(int(t * 100000));
		}
		sort(da.begin(), da.end());
		sort(db.begin(), db.end());
		vector<bool> f(n, false);
		int resa = 0, resb = 0;
		for (i = 0; i < n; ++i)
		{
			for (j = 0; j < n; ++j)
			{
				if (!f[j] && db[j] > da[i])
				{
					break;
				}
			}
			if (j < n)
			{
				f[j] = true;
			}
			else
			{
				resb++;
			}
		}
		for (i = 0; i < n; ++i)
		{
			for (j = 0; j < n - i; ++j)
			{
				if (da[i + j] < db[j])
				{
					break;
				}
			}
			if (j == n - i)
			{
				break;
			}
		}
		resa += n - i;
		printf("Case #%d: ", cs);
		printf("%d %d\n", resa, resb);
	}
}