
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

#define n 4
int first[n][n];
int second[n][n];
int main()
{

	int T;scanf("%d" , &T );
	fr( t , 1 , T+1 )
	{
		int a , b;
		scanf("%d" , &a ); a--;
		fr( i , 0 , n )
			fr(j , 0 , n )
			scanf("%d" , &first[i][j]);
		scanf("%d" , &b ); b--;
		fr( i , 0 , n )
			fr(j , 0 , n )
			scanf("%d" , &second[i][j]);

		set<int> ans;
		fr( i , 0 , n )
			fr( j , 0 , n )
			if( first[a][i] == second[b][j] ) ans.insert( first[a][i] );

		printf("Case #%d: " , t );
		if( ans.size() == 1 )
			printf("%d\n" , *ans.begin());
		else if( ans.size() == 0 )
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
		
	}
	return 0;
}