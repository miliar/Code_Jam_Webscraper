#include <fstream>
#include <algorithm>

using namespace std;

int v[11];

int main()
{
    freopen ( "data.in", "r", stdin );
    freopen ( "data.out", "w", stdout );
    int t, n, y, z, c, i;
    scanf ( "%d", &t );
    for ( i = 1; i <= t; ++i )
    {
        fill( v, v + 10, 0 );
        scanf ( "%d", &n ), y = n;
        if ( n == 0 )
        {
            printf ( "Case #%d: INSOMNIA\n", i );
            continue;
        }
        c = 0;
        for ( ; c != 10; n += y )
        {
            z = n;
            while (z > 0)
            {
                if ( v[z%10] == 0 )
                    ++v[z%10], ++c;
                z /= 10;
            }
        }
        printf ( "Case #%d: %d\n", i, n - y );
    }
    return 0;
}
