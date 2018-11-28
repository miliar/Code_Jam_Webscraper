#include <iostream>
#include <cstdio>
using namespace std;

int t, n;
int v;
char r;

int main()
{

    freopen( "A-large.in"  , "r", stdin  );
    freopen( "A-large.out", "w", stdout );
    cin >> t;

    for( int k = 1; k <= t; k++ ){

        cin >> n;
        int sum = 0, ret = 0;
        for( int i = 0; i <= n; i++ ){
            cin >> r;
            v = ( r - '0' );
            if( sum < i ){
                ret += i - sum;
                sum = i;
            }
            sum += v;
        }
        cout << "Case #" << k << ": " << ret << "\n";

    }

    return 0;

}
