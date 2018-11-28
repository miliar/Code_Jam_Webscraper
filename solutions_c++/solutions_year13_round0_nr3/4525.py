#include <iostream>
#include <cstdio>
using namespace std;

int Case, A, B, cnt, ans;

int main ( ) {
    freopen ( "C-small-attempt0.in", "r", stdin );
    freopen ( "output.txt", "w", stdout );
    cin >> Case;
    for ( cnt = 1; cnt <= Case; ++cnt ) {
        cin >> A >> B;
        ans = 0;
        for ( int i = A; i <= B; ++i )
            if ( i == 1 || i == 4 || i == 9 || i == 121 || i == 484 ) ans++;
        cout << "Case #" << cnt << ": " << ans << endl;
    }
}
