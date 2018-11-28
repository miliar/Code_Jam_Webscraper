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

int f[26], ans[10];

inline void decrease ( char c, string s, int number ) {
    int xd = c - 65;
    while ( f[xd] ) {
        ++ans[number];
        for ( int i = 0; i < s.size(); ++i )
            --f[s[i] - 65];
    }
}

int main ( ) {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    string s;
    cin >> t;
    for ( int c = 1; c <= t; ++c ) {
        cin >> s;
        memset(ans, 0, sizeof ans);
        for ( int i = 0; i < s.size(); ++i ) ++f[s[i] - 65];

        decrease('Z', "ZERO", 0);
        decrease('W', "TWO", 2);
        decrease('U', "FOUR", 4);
        decrease('X', "SIX", 6);
        decrease('G', "EIGHT", 8);
        decrease('F', "FIVE", 5);
        decrease('H', "THREE", 3);
        decrease('S', "SEVEN", 7);
        decrease('O', "ONE", 1);
        decrease('I', "NINE", 9);

        cout << "Case #" << c << ": ";
        for ( int i = 0; i < 10; ++i ) {
            for ( int j = 0; j < ans[i]; ++j )
                cout << i;
        }
        cout << '\n';
    }
}
