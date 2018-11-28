#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int judge(int X, int R, int C)
{
	//1. RxC can't be divided by X
	if( (R*C) % X )
	{
		//Richard will win
		return 0;
	}
	else
	{
		if( X >= 7)
		{
			//can form a empty space
			return 0;
		}
		else if( X > R && X > C)
		{
			return 0;
		}
		else if( (X+1)/2 > min(R, C) )
		{
			return 0;
		}
		//X=1, X=2, X=3 will work
		else if( X == 4 && min(R, C) == 2)
		{
			return 0;
		}
		else if( X == 5 && R*C == 15 )
		{
			return 0;
		}
		else if( X == 6 && min(R, C) < 3 )
		{
			return 0;
		}

	}
	return 1;
}


int main()
{
	int numCase;
	int i;
	int X, R, C;

	scanf("%d", &numCase);

	//printf("numcase %d\n", numCase);

	for( i = 1; i <= numCase; i++)
	{
		scanf("%d %d %d", &X, &R, &C);
		//printf("X= %d R= %d C= %d\n", X, R, C);

		printf("Case #%d: %s\n", i, (judge(X,R,C) == 0? "RICHARD" : "GABRIEL") );
	}


	return 0;
}
