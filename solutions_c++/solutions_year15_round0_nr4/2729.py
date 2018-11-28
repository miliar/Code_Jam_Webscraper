#include<bits/stdc++.h>
using namespace std;
int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		int x, r, c;
		scanf("%d%d%d", &x, &r, &c);
		if (x == 1)
		{
			printf("Case #%d: GABRIEL\n", i);
		}
		else if(x == 2)
		{
			printf(((r*c)&1)?"Case #%d: RICHARD\n":"Case #%d: GABRIEL\n", i);
		}
		else if (x == 3)
		{

			if (r >= 2 && c >= 2 && ((r*c)%3==0))printf("Case #%d: GABRIEL\n", i);
			else printf("Case #%d: RICHARD\n", i);
		}
		else
		{
			if (r >= 3 && c >= 3 && ((r*c) % 4 == 0))printf("Case #%d: GABRIEL\n", i);
			else printf("Case #%d: RICHARD\n", i);
		}
	}
	return 0;
}