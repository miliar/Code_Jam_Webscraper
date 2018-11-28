#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int y,x,n,T,tot,p,ouc[20];

int main()
{
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);

	scanf("%d", &T);

	for (int i = 1; i <= T; i ++)
	{
		scanf("%d", &n);
		memset(ouc, 0, sizeof ouc);
		printf("Case #%d: ", i);
		if (n == 0) { puts("INSOMNIA"); continue; }
		x = n, tot = 10;
		while (1)
		{
			y = x;
			while (y)
			{
				p = y % 10;
				if (ouc[p] == 0) tot --;
				ouc[p] = 1;
				y /= 10;
			}
			if (!tot) break;
			x = x + n;
		}
		printf("%d\n", x);
	}

	return 0;
}
