
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

typedef long long ll;

int main()
{
	//freopen("D-large.in", "r", stdin);
	//freopen("D-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d: ", cases);
		if ((k + c - 1) / c > s)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		vector<ll> ans;
		for (int i = 1; i <= k; i += c)
		{
			ll base = 1, p = 1;
			for (int j = 0; j < c; j++, base *= k)
			{
				p += base*(min((i + j), k) - 1);
			}
			ans.push_back(p);
		}
		for (int i = 0; i < ans.size(); i++)
		{
			printf("%lld%s", ans[i], i == ans.size() - 1 ? "\n" : " ");
		}
	}
	//system("pause");
	return 0;
}