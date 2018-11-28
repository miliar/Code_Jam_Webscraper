#include <iostream>
#include <cstdio>

int main()
{
	int32_t Z;	scanf("%d", &Z);
	for(int32_t q = 1; q <= Z; q++)
	{
		int32_t x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		if(x >= 7 )
		{
			printf("Case #%d: RICHARD\n", q);
		}
		else if( (r*c)%x || (r < x && c < x) || (r<<1 < x || c<<1 < x) )
		{
			printf("Case #%d: RICHARD\n", q);
		}else
		{
			if( ( x == 4 && ( (r == 4 && c == 2) || (r == 2 && c == 4) ) ) || (x == 6 && ((r == 6 && c == 3) || (r == 3 && c == 6))) )
				printf("Case #%d: RICHARD\n", q);
			else 
				printf("Case #%d: GABRIEL\n", q);
		}
	}
	return 0;
}