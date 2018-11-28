
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

#define maxn 1005

int naomi[maxn];
int ken[maxn];
int main()
{

	int T;scanf("%d" , &T );
	fr( t , 1 , T+1 )
	{
		int n; 
		scanf("%d" , &n );
		fr( i , 0 , n )
		{
			long double a;
			scanf("%lf" , &a );
			naomi[i] = (int)(a*1000000);
		}
		sort( naomi , naomi + n );
		fr( i , 0 , n )
		{
			long double a;
			scanf("%lf" , &a );
			ken[i] = (int)(a*1000000);
		}
		sort( ken , ken+n );

		int fairPlay = 0;
		int kb= 0 , ke = n-1;
		for( int i = n-1 ; i >= 0 ; i-- )//loop on naomi
			if( ken[ke] > naomi[i] )//ken wins
				ke--;
			else 
			{
				kb ++;
				fairPlay++;
			}

		kb = 0; ke = n-1;
		int deceitful = 0;
		for( int i = n-1 ; i >= 0 ; i-- )//loop on ken
			if( ken[i] < naomi[ke] )// naomi naturally wins
			{
				deceitful++;
				ke--;
			}
			else
				kb ++;


		printf("Case #%d: %d %d\n" , t , deceitful , fairPlay );

	}
	return 0;
}