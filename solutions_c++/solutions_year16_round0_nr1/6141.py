#include <bits/stdc++.h>
#define  pb             push_back
#define  mp             make_pair
#define  INF            0x3fffffff
#define  MAX            2005

using namespace std;
typedef long long ll;
typedef vector<vector<int> > graph;

#define  check          1023

int main ( ) {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int T, N;
    cin >> T;
    for ( int c = 1; c <= T; ++c ) {
        cin >> N;
        if ( !N ) { cout << "Case #" << c << ": INSOMNIA\n"; continue; }
        for ( int ans = 0, i = 1; ; ++i ) {
            int xd = i * N;
            while ( xd ) {
                ans |= 1 << (xd % 10);
                xd /= 10;
            }
            if ( ans == check ) {
                cout << "Case #" << c << ": " << i * N << '\n';
                break;
            }
        }
    }
}
