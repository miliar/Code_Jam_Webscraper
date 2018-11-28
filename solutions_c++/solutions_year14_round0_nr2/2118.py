#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int flag[20];

int main() {
    
    freopen("in.txt", "r",stdin);
    freopen("outt.txt", "w", stdout);
	int k;
    cin >> k;
    for ( int kk = 1 ; kk <= k ; kk ++ ) {
        double c , f , x;
        printf( "Case #%d: " , kk );
        cin >> c >> f >> x;
        double ans = 0 , mn = x / 2;
        for ( int i = 0 ; ans <= mn ; i ++) {
            ans = x / ( 2 + i * f );
            for ( int j = 0 ; j < i ; j ++ ) {
                ans += c / ( 2 + j * f );
            }
            mn = min( mn , ans );
        }
        printf( "%.7lf\n" , mn );
    }
	return 0;
}