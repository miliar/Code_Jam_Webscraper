#include <iostream>
#include <fstream>

#define FOR0(i,n) for(i=0;i<n;++i)
#define FOR1(i,n) for(i=1;i<=n;++i)

using namespace std ;

int m[4][4] = {
    {0,1,2,3},
    {1,0,3,2},
    {2,3,0,1},
    {3,2,1,0}
} ;

int z[4][4] = {
    {0,0,0,0},
    {0,1,0,1},
    {0,1,1,0},
    {0,0,1,1}
} ;

inline int decode(char c) {
    if( c == 'i' )
        return 1 ;
    else if( c == 'j' )
        return 2 ;
    else
        return 3 ;
}

int l, x, cx, p, i, j, c, sgn, c2, sgn2, step ;
int answered ;
string s, s2 ;

int main() {
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;

    int T, _T ;
    cin >> T ;
    FOR1(_T,T) {
        cout << "Case #" << _T << ": " ;

        cin >> l >> x >> s ;

        s2 = "" ;
        for( cx = 1 ; cx <= x ; ++cx )
            s2 += s ;
        c = sgn = j = 0 ; step = 1 ;
        for(i = 0 ; i < x*l ; ++i) {
            sgn ^= z[c][decode(s2[i])] ;
            c = m[c][decode(s2[i])] ;
            if( c == step && !sgn ) {
                ++step ;
                c = sgn = 0 ;
                if( step == 3 ) {
                    ++i ;
                    break ;
                }
            }
        }
        if( step < 3 ) {
            cout << "NO" << endl ;
            continue ;
        }
        c = sgn = 0 ;
        for( ; i < x*l ; ++i ) {
            sgn ^= z[c][decode(s2[i])] ;
            c = m[c][decode(s2[i])] ;
        }
        if( c == 3 && !sgn )
            cout << "YES" << endl ;
        else
            cout << "NO" << endl ;
    }
}
