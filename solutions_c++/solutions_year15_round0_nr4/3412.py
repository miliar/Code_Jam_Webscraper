//Problem D. Ominous Omino
#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for( int cs = 1; cs <= t; ++cs ) {
        long long x, r, c;
        cin >> x >> r >> c;
        string ans;
        if( x == 1 ) ans = "GABRIEL";
        else if( x == 2 ) {
            if( r*c % 2 == 0 ) ans = "GABRIEL";
            else               ans = "RICHARD";
        }
        else if( x == 3 ) {
            if( r == 3 && c == 3 ) ans = "GABRIEL";
            else if( r == 4 && c == 3 ) ans = "GABRIEL";
            else if( r == 3 && c == 4 ) ans = "GABRIEL";
            else if( r == 2 && c == 3 ) ans = "GABRIEL";
            else if( r == 3 && c == 2 ) ans = "GABRIEL";
            else                       ans = "RICHARD";
        }
        else if( x == 4 ) {
            if( r == 4 && c == 4 ) ans = "GABRIEL";
            else if( r == 4 && c == 3 ) ans = "GABRIEL";
            else if( r == 3 && c == 4 ) ans = "GABRIEL";
            else                       ans = "RICHARD";
        }
        cout << "Case #" << cs << ": " << ans << endl;
    }
}
