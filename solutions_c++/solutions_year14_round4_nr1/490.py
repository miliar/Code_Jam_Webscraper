#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, x;
int s[100020];

int main()
{
	int t, T;
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		scanf("%d %d", &n, &x);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &s[i]);
		}
		sort(s, s + n);

		int be = n;
		for (int sk = 0; sk < n; ++sk)
		{
			int i = 0;
			int j = n - 1 - sk;
			int sl = 0;
			while (i < j)
			{
				while (s[i] + s[j] > x && i < j)
				{
					++sl;
					--j;
				}
				if (i < j)
				{
					++i;
					--j;
				}
			}
			if (i == j)
				++sl;
			sl += sk;
			if (sl < be)
				be = sl;
		}
		printf("Case #%d: %d\n", t, (n + be) / 2);
	}
	return 0;
}
