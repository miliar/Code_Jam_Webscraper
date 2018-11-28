#include <bits/stdc++.h>
#define  pb             push_back
#define  mp             make_pair
#define  MAX            300005
#define  INF            0x3fffffffffffffff
#define  MAXLOG         18
#define  MOD            1000000007LL

using namespace std;
typedef long long ll;
typedef vector<vector<int> > graph;

int f[27];

int main ( ) {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t, n, x;
    cin >> t;
    for ( int c = 1; c <= t; ++c ) {
        memset(f, 0, sizeof f);

        cin >> n;
        set<pair<int, int> > part;

        int sum = 0;
        for ( int i = 0; i < n; ++i ) {
            cin >> f[i];
            sum += f[i];
            part.insert( mp(f[i], i) );
        }

        cout << "Case #" << c << ':';

        char a = 0, b = 0;
        while ( !part.empty() ) {
            int c = part.rbegin()->first;
            int p = part.rbegin()->second;
            if ( a == 0 ) a = p + 65;
            part.erase( mp( c, p ) );
            if ( c > 1 ) part.insert( mp(c - 1, p) );
            --sum;

            if ( part.rbegin()->first > sum / 2 ) {
                int c = part.rbegin()->first;
                int p = part.rbegin()->second;
                b = p + 65;
                part.erase( mp( c, p ) );
                if ( c > 1 ) part.insert( mp(c - 1, p) );
                --sum;
            }

            if ( b ) cout << ' ' << a << b;
            else cout << ' ' << a;
            a = b = 0;
        }

        if ( a != 0 ) cout << ' ' << a;
        cout << '\n';
    }
}
