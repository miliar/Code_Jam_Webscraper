#include<bits/stdc++.h>
using namespace std ;

int F( string s ) {
    for( int k = 0 ; ; k ++ ) {
        int tmp = k ;
        int bc = s[0]-'0'+k ;
        bool f = 0 ;
        for( int i = 1 ; i < s.size() ; i++ ) {
            if( bc < i ) {
                f = 1 ;
                break ;
            }
            bc += s[i]-'0' ;
        }
        if( !f )return tmp ;
    }
}

int main() {
//    freopen("A-large.in","r",stdin) ;
//    freopen("A-large.out","w",stdout) ;
    int cases , caseno = 1;
    cin >> cases ;
    bool ff = 0 ;
    while( cases -- ) {
        long long n ;
        string s ;
        cin >> n >> s ;
        long long tot = 0 ;
        long long bc = s[0]-'0' ;
        for( int i = 1 ; i < s.size() ; i++ ) {
            if( bc < i ) {
                tot += (i-bc) ;
                bc += (i-bc) ;
            }
            bc += s[i]-'0' ;
        }
        long long other = F( s ) ;

        if( other != tot ) {
            ff = 1 ;
        }
        cout << "Case #"<<caseno++ << ": " << tot << "\n" ;
    }
    //if( ff )cout << "WA\n" ;
    return 0 ;
}


/*
//
//int main(){
//
//    srand(time(NULL)) ;
//    freopen("in.txt","r",stdin) ;
//    freopen("in.txt","w",stdout) ;
//    int cases = 1000 ;
//    cout << cases << endl ;
//    while( cases -- ){
//        int n = rand()%20 ;
//        cout << n << " " ;
//        for( int i = 0 ; i < n+1 ; i++ ){
//            cout << rand()%2 ;
//        }cout << endl ;
//    }
//}
*/
