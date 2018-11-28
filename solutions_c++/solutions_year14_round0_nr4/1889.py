#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

double a[1005] , b[1005];

int main() {
    
//    freopen("in.txt", "r",stdin);
//    freopen("outt.txt", "w", stdout);
	int k;
    cin >> k;
    for ( int kk = 1 ; kk <= k ; kk ++ ) {
        printf( "Case #%d: " , kk );
        int n;
        cin >> n;
        for ( int i = 0 ; i < n ; i ++ ) {
            cin >> a[i];
        }
        sort( a , a + n );
        for ( int i = 0 ; i < n ; i ++ ) {
            cin >> b[i];
        }
        sort( b , b + n );
        int ans , i , j;
        ans = i = j = 0;
        while ( i < n ) {
            if ( a[i] > b[j] ) {
                ans ++; i ++; j ++;
            }
            else {
                i ++;
            }
        }
        cout << ans;
        ans = i = j = 0;
        while ( i < n ) {
            if ( b[i] > a[j] ) {
                ans ++; i ++; j ++;
            }
            else {
                i ++;
            }
        }
        cout << ' ' << n - ans << endl;
    }
	return 0;
}