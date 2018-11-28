#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std ;
string s ;
int n ;
int Run() {
    int _ , cas = 1 ; cin >> _ ;
    while( _-- ) {
        cout << "Case #" << cas++ << ": " ;
        cin >> n >> s ;
        int now = s[0] - '0' , ans = 0 ;
        for( int i = 1 ; i < s.length() ; ++i ) {
            if( now < i ) { ans += i - now ; now = i ; }
            now += s[i] - '0' ;
        }
        cout << ans << endl ;
    }
}
int main () {
//    freopen("in.txt","r",stdin);
    ios::sync_with_stdio(0) ;
    return Run() ;
}
