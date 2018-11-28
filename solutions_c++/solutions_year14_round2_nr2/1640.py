
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

int main()
{

	int T; scanf("%d" , &T );
	fr( t , 1 , T+1 )
	{
		int a , b , k; scanf("%d%d%d" , &a , &b , &k  );
		L ans = 0;
		fr( i , 0 , a )
			fr( j , 0 , b )
				if( (i&j) < k )
					ans ++;
		cout <<" Case #" << t << ": " << ans << endl; 
		
	}
	return 0;
}