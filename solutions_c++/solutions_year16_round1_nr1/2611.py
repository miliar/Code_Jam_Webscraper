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
        deque<char> d;
        d.push_front(s[0]);
        for ( int i = 1; i < s.size(); ++i ) {
            if ( s[i] >= d.front() ) d.push_front(s[i]);
            else d.push_back(s[i]);
        }
        cout << "Case #" << c << ": " << string(d.begin(), d.end()) << '\n';
    }
}
