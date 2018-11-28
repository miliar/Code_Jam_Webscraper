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

typedef pair< int, int > pii;
typedef long long i64;

//#define NAME "b"
#define NAME "B-small-attempt0"
#define ABS( a ) ( (a) > 0 ? (a) : -(a) )
#define SIZE( a ) ( int( (a).size() ) )
#define LENGTH( a ) ( int( (a).length() ) )
#define SQR( a ) ( (a) * (a) )
#define FS first
#define SE second

int main()
{
  #ifdef LOCAL
  freopen( NAME".in", "rt", stdin );
  freopen( NAME".out", "wt", stdout );
  #endif

	int tests;
	scanf("%d", &tests);
	for( int test = 1; test <= tests; ++test )
	{
		int a, b, k;
		scanf("%d%d%d", &a, &b, &k);
		int ans = 0;
		for( int i = 0; i < a; ++i )
			for( int j = 0; j < b; ++j )
				if( (i & j) < k ) ++ans;
		printf("Case #%d: %d\n", test, ans);
	}
	
  #ifdef LOCAL
  fclose( stdin );
  fclose( stdout );
  #endif

  return 0;
}       
