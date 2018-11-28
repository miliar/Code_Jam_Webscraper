#include <bits/stdc++.h>
#define  mem(x, v)      memset(x, v, sizeof(x))
#define  pb             push_back
#define  mp             make_pair
#define  INF            0x3fffffff
#define  read(x, n)     for ( int i = 0; i < n; i++ ) cin >> x[i];
#define  debug(x, n)    for ( int i = 0; i < n; i++ ) cout <<  x[i] << ' '
#define  min3(a, b, c)  min((a), min((b), (c)))
#define  MOD            1000000007LL
#define  MAX            1005

using namespace std;
typedef long long ll;
typedef vector<vector<pair<int, int> > > graph;

int a[MAX];

int main ( ) {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin.tie(0);
    ios_base::sync_with_stdio(0);

    int T, S;
    char t;
    cin >> T;
    for ( int c = 1; c <= T; ++c ) {
        cin >> S;
        for ( int i = 0; i <= S; ++i ) {
            cin >> t;
            a[i] = t - 48;
        }

        int current = 0, ans = 0;
        for ( int i = 0; i <= S; ++i ) {
            if ( current >= i ) current += a[i];
            else {
                ans += i - current;
                current += a[i] + (i - current);
            }
        }

        cout << "Case #" << c << ": " << ans << '\n';
    }
}
