#include <bits/stdc++.h>
using namespace std;
const int MAXS = 100 + 2;

string s;

void solve(){
    int ans = 0;
    for( int i = 1; i < s.size(); ++i )
        if( s[ i ] != s[ i - 1 ] )
            ++ans;
    ans += ( s[ (int)s.size() - 1 ] == '-' );
    cout << ans << "\n";
}

int main(){
    int T; cin >> T;
    for( int kase = 1; kase <= T; ++kase ){
        cin >> s;
        printf("Case #%d: ", kase);
        solve();
    }
    return 0;
}
