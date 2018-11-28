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

int a[1000];
bool used[1000];
bool used2[1000];
int c, d, v;

void add(int x)
{
	for (int i = 0; i <= v; i++)
		used2[i] = false;
	for (int i = 0; i <= v; i++)
		if (used[i])
			used2[i + x] = true;
	for (int i = 0; i <= v; i++)
		used[i] |= used2[i];
}

void solve()
{
	cin >> c >> d >> v;
	for (int i = 0; i < d; i++)
		cin >> a[i];

	for (int i = 0; i <= v; i++)
		used[i] = false;
	used[0] = true;

	for (int i = 0; i < d; i++)
		add(a[i]);

	int ans = 0;
	for (int i = 0; i <= v; i++)
		if (!used[i])
		{
			ans++;
			add(i);
		}

	printf("%d", ans);

	return;
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
		solve();
		printf("\n");
	}
}