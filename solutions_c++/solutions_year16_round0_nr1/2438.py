#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
bool f[10];
bool check(int x)
{
	while (x)
	{
		f[x % 10] = 1;
		x /= 10;
	}
	for (auto i : f) if (!i) return 0;
	return 1;
}
int main()
{
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --)
	{
		int n;
		scanf("%d", &n);
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", ++ zzz);
			continue;
		}
		memset(f, 0, sizeof(f));
		int ans = n;
		while (!check(ans))
		{
			ans += n;
		}
		printf("Case #%d: %d\n", ++ zzz, ans);
	}
}

