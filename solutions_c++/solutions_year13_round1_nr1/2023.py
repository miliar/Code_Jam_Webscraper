#include <stdio.h>
#include <string>
#include "bignum.h"
using namespace std;

#define rep(i, n) for (int i = 0; i < n; ++i)
int ri() { int a; scanf( "%d", &a ); return a; }
char sbuf [100005];
string rs () { scanf( "%s", sbuf ); return sbuf; }
long long rll() { long long a; scanf( "%lld" , &a ); return a ; }


int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\A-small-attempt0.in","rt",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\A-large-practice.out","wt",stdout);
	
	int N = ri();
	rep(n, N)
	{
		long long r = rll();
        long long t = rll();
        
        int total = 0;
        long long last = r * r;
        long long radius = r;
        while (true)
        {
            long long cost = radius * 2 + 1;
            if (!(cost < t || cost == t))
                break;
            total++;
            t = t - cost;
            radius = radius + 2;
        }
        

		printf("Case #%d: ", n+1);
		printf("%d\n", total);
	}
	return 0;
}
