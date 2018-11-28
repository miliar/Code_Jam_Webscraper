#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int MAXAB = 1023;

bool used[MAXAB];

int main(){

    freopen ( "B-small-attempt0.in", "r", stdin );
    freopen ( "B-small.out", "w", stdout );

    int t;
    cin >> t;

    for ( int testcase = 1; testcase <= t; ++testcase ){
        int a, b, k;
        cin >> a >> b >> k;
        memset ( used, false, sizeof ( used ) );
        int cnt = 0;
        for ( int i = 0; i < a; ++i ){
            for ( int j = 0; j < b; ++j ){
                cnt += (i&j) < k;
            }
        }

        cout << "Case #" << testcase << ": " << cnt << endl;
    }

    return 0;
}
