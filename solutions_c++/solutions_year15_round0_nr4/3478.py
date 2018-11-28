// OminousOmino.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int q=1;q<=T;q++)
	{
		printf("Case #%d: ", q);
		int X;
		scanf("%d", &X);
		int R;
		scanf("%d", &R);
		int C;
		scanf("%d", &C);
		if(X == 1)
			printf("GABRIEL\n");
		else
		{
			if(X == 2 && R*C%2 == 0)
				printf("GABRIEL\n");
			else
				{
					if(X == 3 && R*C%3 == 0 && R > 1 && C > 1)
						printf("GABRIEL\n");
					else
					{
						if(X == 4 && R*C > 11 )
							printf("GABRIEL\n");
						else
							printf("RICHARD\n");
					}
				}
		}
	}
	return 0;
}

