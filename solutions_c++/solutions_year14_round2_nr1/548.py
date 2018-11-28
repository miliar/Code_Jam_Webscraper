#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

typedef pair<char, int> pic;

const int maxN = 110;

int n;
vector <pic> ar[maxN];
char s[110];
int m[110];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int q;
	scanf("%d", &q);
	for (int t = 0; t < q; t++)
	{
		memset(m, 0, sizeof(0));
		printf("Case #%d: ", t + 1);
		scanf("%d\n", &n);
		bool good = true;
		for (int i = 0; i < n; i++)
		{
			scanf("%s", &s);
			int l = strlen(s);
			ar[i].clear();
			ar[i].push_back(pic(s[0], 1));
			for (int j = 1; j < l; j++)
			{
				if (s[j] == s[j - 1])
				{
					ar[i][ar[i].size() - 1].second++;
				}
				else
				{
					ar[i].push_back(pic(s[j], 1));
				}
			}
			if (i > 0)
			{
				if (ar[i].size() != ar[i - 1].size())
				{
					good = false;
				}
				if (good)
				{
					for (int j = 0; j < ar[i].size(); j++)
					{
						if (ar[i][j].first != ar[i - 1][j].first)
						{
							good = false;
						}
					}
				}
			}
			for (int j = 0; j < ar[i].size(); j++)
			{
				m[j] = max(m[j], ar[i][j].second);
			}
		}
		if (!good)
		{
			printf("Fegla Won\n");
			continue;
		}
		int ans = 0;
		for (int i = 0; i < ar[0].size(); i++)
		{
			int best = 1e9;
			for (int j = 1; j <= m[i]; j++)
			{
				int cur = 0;
				for (int k = 0; k < n; k++)
				{
					cur += abs(j - ar[k][i].second);
				}
				if (cur < best)
				{
					best = cur;
				}
			}
			ans += best;
		}
		printf("%d\n", ans);
	}
	return 0;
}