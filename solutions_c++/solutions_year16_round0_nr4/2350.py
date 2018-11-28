#include <iostream>
#include <cstdio>

using namespace std;

int t, k, c, s;

void solve()
{
    if (k != s) printf("%s\n", "IMPOSSIBLE");
    else {
        for (int i = 1; i <= s; i++)
			printf("%d ", i);
		printf("\n");
    }
}

int main()
{
    freopen("frac.in", "r", stdin);
    freopen("frac.out", "w", stdout);

    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
	{
		scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d: ", i);
        solve();
	}
    return 0;
}
