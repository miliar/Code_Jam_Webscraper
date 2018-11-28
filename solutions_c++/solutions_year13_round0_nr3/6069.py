#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

bool ispal ( long long n )
{
    long long r = 0, n2 = n;
    while ( n2 )    {
        r*= 10;
        r+= n2%10;
        n2/= 10;
    }
    if ( n == r )   return true;
    else return false;
}

int main()
{
    freopen ( "input.txt", "r", stdin );
    freopen ( "output.txt", "w", stdout );

    long long i, j, k, l, t, caseno = 0, a, b, total, ans;
    scanf ( "%lld", &t );

    while ( t-- )   {
        scanf ( "%lld %lld", &a, &b );
        printf ( "Case #%d: ", ++caseno );
        ans = 0;
        j = (long long)sqrt ( a );
        k = (long long)sqrt ( b );
        for ( i = j; i <= k; i++ )  {
            l = i*i;
            if ( ispal(i) && ispal (l) && l>=a && l<=b )
                ans++;
        }
        cout << ans << endl;
    }
    return 0;
}
