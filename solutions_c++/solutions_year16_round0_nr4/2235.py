#include <cstdio>

using namespace std;

typedef long long ll;

int T;

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
	{
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d:", t);
		for (int i = 1; i <= s; i ++)
			printf(" %d", i);
		puts("");
	}
	return 0;
}
