#include <iostream>
#include <cstdio>
using namespace std;
const int MAXN = 1005;

int p[MAXN*MAXN] , a[MAXN*MAXN];
int D;

bool possible( int mid )
{
    for ( int specialRounds = 0; specialRounds < mid ; specialRounds++ )
    {
        int canLeave = mid - specialRounds;
        int N = D;
        for ( int i = 1; i <= D; i++ )
            a[i] = p[i];

        for ( int x = 1; x <= specialRounds ; x++ )
        {
            int best = 1;
            for ( int i = 2 ; i <= N; i++)
            {
                if ( a[i] > a[best] ) best = i;
            }

            N++;
            a[N] = canLeave;
            a[best] -= a[N];
        }

        bool flag = true;
        for ( int i = 1; i <= N; i++)
        {
            if ( a[i] > canLeave ) flag = false;
        }
        if ( flag ) return true;
    }

    return false;
}

int main()
{
    freopen("input.in" , "r" , stdin );
    freopen("output.out" , "w" , stdout );

    int T;
    cin >> T;

    for (int _t = 1 ; _t <= T; _t++ )
    {
        cin >> D;
        for (int i = 1; i <= D; i++)
            cin >> p[i];

        int l = 0;
        int r = MAXN;
        while ( r - l > 1 )
        {
            int mid = ( l + r ) / 2;
            if ( possible( mid ) )
                r = mid;
            else
                l = mid;
        }

        cout << "Case #" << _t << ": " << r << endl;
    }

    return 0;
}
