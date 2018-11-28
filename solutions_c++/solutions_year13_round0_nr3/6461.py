/*
* File:   main.cpp
* Author: Sreekanth
*
* Created on May 21, 2011
*/

#include "stdlib.h"
#include "stdio.h"
#include "math.h"
#include "string.h"

bool ispolin(long int i)
{
	char str[400] ={0};
	sprintf(str,"%ld",i);
	int len = strlen(str);
	bool ispolin = true;
	for( int it = 0 ; it < len/2 ; it++)
	{
		if(str[it] != str[len - it - 1])
		{
			ispolin = false;
		}
	}
	return ispolin;
}

int issqr(long int n)
{
	double h = n & 0xF; // last hexidecimal "digit"
    if (h > 9)
        return 0; // return immediately in 6 cases out of 16.

    // Take advantage of Boolean short-circuit evaluation
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        // take square root if you must
        int t = (int) floor( sqrt((double) n) + 0.5 );
		if (t*t == n)
		{
			return t;
		}
		return 0;
    }
    return 0;
}
int main()
{
	freopen("I.in","r",stdin);
	freopen("O.op","w",stdout);

	int cases;
	scanf("%d",&cases);
	int caserunning=0;
	while (cases--)
	{
		char dummy;
		scanf("%c",&dummy);
		int min , max;
		scanf("%ld",&min);
		scanf("%ld",&max);
		int res = 0;
		for(int i = min ; i <= max ; i++)
		{
			if(ispolin(i))
			{
				int temp;
				if(temp = issqr(i))
				{
					if(ispolin(temp))
					{
						res += 1;
					}
				}
			}
		}

		printf("Case #%d: %d\n" , ++caserunning , res);


	}


	return 0;
}
