#include <bits/stdc++.h>
#define pb push_back
#define ll long long
#define MAX 50
#define INF 2000000000

using namespace std;

string s;
int t, i = 1;


int main ( )
{
    ios_base :: sync_with_stdio ( 0 );
    freopen ( "B-large.in", "r", stdin );
    freopen ( "B-large.out", "w", stdout );

    cin >> t;

    while(cin >> s)
    {
        reverse ( s.begin(), s.end() ); int ans = 0;

        int k = 0;
        while ( s[k] == '+' ) ++ k; int q = 0;
        for ( ; s[k]; ++ k )
        {
            if ( s[k] == '-' and q == 0 )
            {
                ++ ans;
                q = 1;
            }
            if ( s[k] == '+' and q == 1 )
            {
                ++ ans;
                q = 0;
            }
        }

        cout << "Case #" << i++ << ": " << ans << endl;
    }


    return 0;
}
