#include <cstdio>
#include <algorithm>
using namespace std;


int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t, n, a, cas = 1;
    int mote[110];
    scanf("%d", &t);
    while ( t -- )
    {
        scanf("%d %d", &a, &n);
        for (int i = 0; i < n; i ++)
            scanf("%d", &mote[i]);
        sort( mote, mote + n );
        int ans = n;
        for ( int i = n; i >= 0 && a > 1; i -- )
        {
            int cnt = n - i;
            int now = a;
            int j = 0;
            while ( j < i )
            {
                if ( now > mote[j] )
                {
                   now += mote[ j ++ ];
                }
                else {
                    while ( now - 1 > 0 && now <= mote[j] )
                    {
                        cnt ++;
                        now += ( now - 1 );
                    }
                }
            }
            if ( cnt < ans )
                ans = cnt;
        }
        printf("Case #%d: %d\n", cas++, ans );
    }
    return 0;
}
