#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

const int sz = 1000;
int cnt[sz];

void Solution()
{
	int n, s;
	scanf("%d%d", &n, &s);
	for (int i = 0; i < n; i++)
	{
		int x;
		scanf("%d", &x);
		cnt[x]++;
	}

	int ans = 0;
	for (int i = 0; i < sz; i++)
	{
		while (cnt[i] > 0)
		{
			ans++;
			cnt[i]--;
			int rem = s - i;
			for (int j = rem; j >= i; j--)
				if (cnt[j] > 0)
				{
					cnt[j] --;
					break;
				}
		}
	}
	printf("%d", ans);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}