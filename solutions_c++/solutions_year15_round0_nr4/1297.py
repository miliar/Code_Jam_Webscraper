#include <stdio.h>
#include <algorithm>
using namespace std;
int d, t, i, j, ans, x, r,c ,a;



int main()
{
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("D-sss.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		scanf("%d%d%d", &x, &r, &c);
		if (r < c)
		{
			a = r;
			r = c;
			c = a;
		}
		if (x < 7 && (r*c) % x == 0 && r >= x&&c>x-2)
		{
			printf("GABRIEL\n");
		}
		else printf("RICHARD\n");

		
		

	}
	return 0;
}