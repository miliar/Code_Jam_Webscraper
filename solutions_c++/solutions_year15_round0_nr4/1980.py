#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

int main(int argc, char** argv)
{
	int T, X, R, C;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		scanf("%d %d %d", &X, &R, &C);
		if (X == 1)
		{
			printf("Case #%d: GABRIEL\n", i);
		}
		else if (X >= 7)
		{
			printf("Case #%d: RICHARD\n", i);
		}
		else if (X == 2)
		{
			if (R % 2 == 1 && C % 2 == 1)
			{
				printf("Case #%d: RICHARD\n", i);		
			}
			else
			{
				printf("Case #%d: GABRIEL\n", i);
			}
		}
		else if (X == 3)
		{
			if ((R == 1 || C == 1))
			{
				printf("Case #%d: RICHARD\n", i);	
			}
			else if ((R % 3 == 0 && C % 2 == 0)
				|| (R % 2 == 0 && C % 3 == 0)
				|| (R % 3 == 0 && C % 3 == 0))
			{
				printf("Case #%d: GABRIEL\n", i);
			}
			else
			{
				printf("Case #%d: RICHARD\n", i);
			}
		}
		else if (X == 4)
		{
			if ((R == 1 || C == 1)
				|| (R % 2 == 1 && C % 2 == 1))
			{
				printf("Case #%d: RICHARD\n", i);	
			}
			else if ((R % 4 == 0 && C % 3 == 0)
				|| (R % 3 == 0 && C % 4 == 0)
				|| (R % 4 == 0 && C % 4 == 0))
			{
				printf("Case #%d: GABRIEL\n", i);
			}
			else
			{
				printf("Case #%d: RICHARD\n", i);	
			}
		}
		else if (X == 5)
		{
			if ((R == 1 || C == 1))
			{
				printf("Case #%d: RICHARD\n", i);	
			}
			else if ((R % 2 == 0 && C % 2 == 0)
				|| (R % 6 == 0 && C % 3 == 0)
				|| (R % 3 == 0 && C % 6 == 0))
			{
				printf("Case #%d: GABRIEL\n", i);
			}
			else
			{
				printf("Case #%d: RICHARD\n", i);	
			}
		}
		else if (X == 6)
		{
			if ((R == 1 || C == 1))
			{
				printf("Case #%d: RICHARD\n", i);	
			}
			else if ((R % 6 == 0 && C % 4 == 0)
				|| (R % 4 == 0 && C % 6 == 0))
			{
				printf("Case #%d: GABRIEL\n", i);
			}
			else
			{
				printf("Case #%d: RICHARD\n", i);	
			}
		}
	}
}