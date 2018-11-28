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

int main()
{
    freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int t, i, d;
	double c, f, x, T, F, D;

	sc1(t);

	fr( i, t )
	{
	    D = T = 0.0;  F = 2.0;
	    sc( "%lf %lf %lf", &c, &f, &x );
	    D = x/F;
	    T = (c/F);
	    d = (ceil)(x/c) - 1;
	    while( d )
	    {
	        F += f;
            D = min(D, (T + (x / F)));
	        T += (c/F);
	        d--;
	    }
	    pr( "Case #%d: %.7lf\n", i+1, D );
	}

return 0;
}
