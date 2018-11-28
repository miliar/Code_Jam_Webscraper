#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int flag[20];

int main() {
    
//    freopen("in.txt", "r",stdin);
//    freopen("out.txt", "w", stdout);
	int k;
    cin >> k;
    for ( int kk = 1 ; kk <= k ; kk ++ ) {
        memset( flag , 0 , sizeof( flag ) );
        printf( "Case #%d: " , kk );
        int n , m;
        cin >> n;
        for ( int i = 1 ; i < 5 ; i ++ ) {
            for ( int j = 1 ; j < 5 ; j ++ ) {
                cin >> m;
                if ( i == n ) {
                    flag[m] ++;
                }
            }
        }
        cin >> n;
        for ( int i = 1 ; i < 5 ; i ++ ) {
            for ( int j = 1 ; j < 5 ; j ++ ) {
                cin >> m;
                if ( i == n ) {
                    flag[m] ++;
                }
            }
        }
        int ans = 0 , num = 0;
        for ( int i = 1 ; i < 17 ; i ++ ) {
            if ( flag[i] == 2 ) {
                ans = i; num ++;
            }
        }
        if ( num > 1 ) cout << "Bad magician!" << endl;
        else if ( num == 1 ) cout << ans << endl;
        else cout << "Volunteer cheated!" << endl;
    }
	return 0;
}