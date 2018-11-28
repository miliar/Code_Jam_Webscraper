# include "stdio.h"

bool who_wins(int x, int r, int c)
{
	if (x == 1)
		return 0;

	if ((r * c) % x != 0)
		return 1;
	else
	{
		if ( x == 2)
			return 0;

		else if (x == 3)
		{
			if ( r == 1 or c == 1)
				return 1;
			else
				return 0;
		}
		else
		{
			if (r == 3 or c == 3 or (r == 4 and c == 4))
				return 0;
			else
				return 1;
		}
	} 
}

int main()
{
	int t, x, r, c, i = 1;

	scanf("%d", &t);

	while(i <= t)
	{
		scanf("%d %d %d", &x, &r, &c);
		bool val = who_wins(x, r, c);

		if (val)
			printf("Case #%d: RICHARD\n", i);
		else
			printf("Case #%d: GABRIEL\n", i);
		i++;
	}
}