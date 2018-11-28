#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int n, m;
long long s;
int main()
{
	int ncase, i, j, tt = 0;
	
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);
	scanf("%d", &ncase);
	while (ncase--)
	{
		scanf("%d %d %lld", &n, &m, &s);
		printf("Case #%d: ", ++tt);
		for (i = 1; i <= s; i++)
			printf(" %d", i);
		puts("");
	}
	return 0;
}
