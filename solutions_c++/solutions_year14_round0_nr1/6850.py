#define LOCAL

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <bitset>
#include <cassert>

using namespace std;

const int INF = 0x3f3f3f3f;
const double PI = 3.14159265358979323846;

#define NAME "A-small-attempt0"
#define ABS( a ) ( (a) > 0 ? (a) : -(a) )
#define SIZE( a ) ( int( (a).size() ) )
#define LENGTH( a ) ( int( (a).length() ) )
#define SQR( a ) ( (a) * (a) )

int main()
{
  #ifdef LOCAL
  freopen( NAME".in", "rt", stdin );
  freopen( NAME".out", "wt", stdout );
  #endif

	int tests;
	int m[4][4];
	scanf("%d", &tests);
	for( int test = 1; test < tests + 1; ++test )
	{
		int a, mark[20];

		memset( mark, 0, sizeof( mark ) );

		scanf("%d", &a);
		for( int i = 0; i < 4; ++i )
			for( int j = 0; j < 4; ++j )
				scanf("%d", &m[i][j]);
		for( int i = 0; i < 4; ++i ) mark[m[a - 1][i]] = 1;

		scanf("%d", &a);
		for( int i = 0; i < 4; ++i )
			for( int j = 0; j < 4; ++j )
				scanf("%d", &m[i][j]);
		for( int i = 0; i < 4; ++i ) ++mark[m[a - 1][i]];

		int num = -1, ans = 0;
		for( int i = 0; i < 20; ++i ) if( mark[i] > 1 )
		{
			num = i;
			++ans;
		}
		
		printf("Case #%d: ", test);
		if( ans == 1 ) printf("%d\n", num);
		else if( ans == 0 ) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}

  #ifdef LOCAL
  fclose( stdin );
  fclose( stdout );
  #endif

  return 0;
}       
