
#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

#define fr( i , c , n ) for( int i = (c) ; i < (n) ;i++ )
#define clr( a , c ) memset( a , c , sizeof a )
#define P pair<int , int>
#define L  long long
#define ld long double
#define eps 1e-9

ld x , f , c;
int main()
{

	int T ;scanf("%d" , &T );
	fr( t , 1 , T+1 )
	{
		scanf("%lf%lf%lf" , &c , &f , &x );
		ld ans = 0;
		ld prod = 2;
		while(1)
		{
			ld timeTarget = x/prod;
			ld timeFarm = c/prod + x/( prod + f );

			if( ( timeTarget - eps ) < timeFarm )
			{
				ans += x/prod;
				break;
			}
			else
			{
				ans += c/prod;
				prod += f;
			}
		}
		printf("Case #%d: %.9f\n" , t , ans);
	}
	return 0;
}