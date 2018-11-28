#include <iostream>
#include <vector>
using namespace std;

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int T, cs;
	scanf("%d", &T);
	for (cs = 1; cs <= T; ++cs)
	{
		int p, q, i, j, t;
		int f[20] = {0};
		scanf("%d", &p);
		for (i = 0; i < 4; ++i)
		{
			for (j = 0; j < 4; ++j)
			{
				scanf("%d", &t);
				if(i + 1 != p)
				{
					continue;
				}
				f[t]++;
			}
		}
		scanf("%d", &q);
		vector<int> ans;
		for (i = 0; i < 4; ++i)
		{
			for (j = 0; j < 4; ++j)
			{
				scanf("%d", &t);
				if(i + 1 != q)
				{
					continue;
				}
				f[t]++;
				if (f[t] == 2)
				{
					ans.push_back(t);
				}
			}
		}
		printf("Case #%d: ", cs);
		if (ans.empty())
		{
			printf("Volunteer cheated!\n");
		}
		else if (ans.size() > 1)
		{
			printf("Bad magician!\n");
		}
		else
		{
			printf("%d\n", ans[0]);
		}
	}
}