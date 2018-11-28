#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<string>
#include<cctype>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<bitset>
#include<utility>
#include<algorithm>
#include<cstdlib>
#include<iostream>
using namespace std;

#define sc scanf
#define sc1(a) scanf( "%d", &a )
#define pr printf
#define pr1(a) printf( "%ld\n", a )
#define all(v) v.begin(),v.end()
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))
#define maxall(v) *max_element(all(v))
#define minall(v) *min_element(all(v))
#define fr( i, n ) for( __typeof(n) i=0; i<n; i++ )
#define rv( i, n ) for( __typeof(n) i=n-1; i>=0; i-- )
#define fo( i, m, n ) for( __typeof(n) i=m; i<=n; i++ )
#define ms( a, val ) memset( a, val, sizeof(a) )
#define pb push_back

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
    int a, b, i, j, k, p, n, t;

    sc1(t);

    fr( i, t )
    {
       sc( "%d %d %d", &a, &b, &k );
       p = 0;
       fr( j, a )
       {
           fr( n, b )
           {
               if( ( j & n ) < k )
                   p++;
           }
       }
       pr( "Case #%d: %d\n", i+1, p );
    }
return 0;
}
