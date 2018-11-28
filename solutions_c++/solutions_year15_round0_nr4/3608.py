#include <cstdio>
using namespace std;
int main ()
{
	int t; scanf ("%d", &t);
	for (int i=1; i<=t; i++)
	{
		int X, R, C; scanf ("%d %d %d", &X, &R, &C);
		if (X == 1)
			printf ("Case #%d: GABRIEL\n", i);
		if (X == 2)
		{
			if (R*C % 2 == 0) printf ("Case #%d: GABRIEL\n", i);
			else		 	  printf ("Case #%d: RICHARD\n", i);
		}
		if (X == 3)
		{
			if (R*C == 6 || R*C == 9 || R*C == 12) printf ("Case #%d: GABRIEL\n", i);
			else 					  			   printf ("Case #%d: RICHARD\n", i);
		}
		if (X == 4)
		{
			if (R*C == 12 || R*C == 16) printf ("Case #%d: GABRIEL\n", i);
			else 		 				printf ("Case #%d: RICHARD\n", i);
		}
	}
	return 0;
}
