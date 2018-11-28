#include <bits/stdc++.h>
#define  pb             push_back
#define  mp             make_pair
#define  INF            0x3fffffff
#define  MAX            2005

using namespace std;
typedef long long ll;
typedef vector<vector<int> > graph;

int main ( ) {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    string S;
    for ( int c = 1; c <= T; ++c ) {
        cin >> S;
        int ans = 1;
        for ( int i = 1; i < S.size(); ++i )
            if ( S[i - 1] != S[i] )
                ++ans;
        cout << "Case #" << c << ": " << (ans - (S.back() == '+')) << '\n';
    }
}
