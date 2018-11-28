#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

const int MAXN = 109 ;

int N ;
double X , V , pX[MAXN] , pV[MAXN] ;
double a[3][MAXN] , t[MAXN] ;

void Init() {
    for ( int i = 1 ; i <= N ; i ++ ) cin >> pV[i] >> pX[i] ;
}

void Solve() {
    bool panL = false , panR = false ;
    for ( int i = 1 ; i <= N ; i ++ ) {
        if ( pX[i] <= X ) panL = true ;
        if ( pX[i] >= X ) panR = true ;
    }
    if ( !panL || !panR ) { cout << "IMPOSSIBLE\n" ; return ; }
    panL = false , panR = false ;
    for ( int i = 1 ; i <= N ; i ++ ) {
        if ( pX[i] < X ) panL = true ;
        if ( pX[i] > X ) panR = true ;
    }
    if ( !panL || !panR ) {
        double sumV = 0.0 ;
        for ( int i = 1 ; i <= N ; i ++ ) if ( pX[i] == X ) sumV += pV[i] ;
        cout << fixed << V / sumV << "\n" ;
        return ;
    }
    /*
    \sum {ti * pV[i]} = V
    \sum {ti * pV[i] * pX[i]} = X * \sum \{ti * pV[i]\}
    
    \sum {ti * [pV[i]*pX[i] - X*pV[i]]} = 0
    */
    double L = 0.0 , R = 10000000000.0 , Mid ;
    double CoolV , CoolX , HotV , HotX , WellV ;
    while ( R-L > 1e-9 ) {
        Mid = (L+R) / 2.0 ;
        
        CoolV = 0.0 , CoolX = 0.0 ;
        HotV  = 0.0 , HotX  = 0.0 ;
        WellV = 0.0 ;
        
        for ( int i = 1 ; i <= N ; i ++ ) {
            if ( pX[i] == X ) WellV += Mid * pV[i] ;
            else if ( pX[i] < X ) {
                CoolV += Mid * pV[i] ;
                CoolX += Mid * pV[i] * pX[i] ;
            } else {
                HotV += Mid * pV[i] ;
                HotX += Mid * pV[i] * pX[i] ;
            }
        }
        CoolX /= CoolV ;
        HotX  /=  HotV ;
        /*
            CoolX * CoolV + HotX * HotV = X * (CoolV + HotV)
            
            HotV = (CoolX * CoolV - X * CoolV) / (X - HotX)
            CoolV = (HotX * HotV - X * HotV) / (X - CoolX)
        */
        
        double _HotV  = (CoolX * CoolV - X * CoolV) / (X - HotX) ;
        double _CoolV = (HotX * HotV - X * HotV) / (X - CoolX) ;
        //cout << fixed << HotV << " " << _HotV << " " << CoolV << " " << _CoolV << "\n" ;
        if ( ( HotV  >=  _HotV && CoolV + _HotV + WellV >= V ) ||
             ( CoolV >= _CoolV && _CoolV + HotV + WellV >= V ) ) {
            R = Mid ;
        } else {
            L = Mid ;
        }
    }
    
    cout << fixed << (L+R)/2.0 << "\n" ;
    /*
    for ( int i = 1 ; i <= N ; i ++ ) a[1][i] = pV[i] ;
    for ( int i = 1 ; i <= N ; i ++ ) a[2][i] = pV[i]*pX[i] - X*pV[i] ;
    
    if ( N == 1 ) cout << fixed << V / pV[1] << "\n" ;
    else { // if ( N == 2 )
        if ( pX[1] == pX[2] ) {
            if ( pV[1] >= pV[2] ) cout << fixed << V / pV[1] << "\n" ;
            else                  cout << fixed << V / pV[2] << "\n" ;
        } else {
            t[1] = V * a[2][2] / (a[1][1]*a[2][2] - a[2][1]*a[1][2]) ;
            t[2] = V * a[2][1] / (a[1][2]*a[2][1] - a[2][2]*a[1][1]) ;
            
            if ( t[1] <= t[2] ) cout << fixed << t[2] << "\n" ;
            else                cout << fixed << t[1] << "\n" ;
        }
    }
    */
}

int main() {
    //freopen("B.in" , "r" , stdin) ; freopen("B.out" , "w" ,stdout) ;
    //freopen("B-small-attempt0.in" , "r" , stdin) ; freopen("B-small-attempt0.out", "w" ,stdout) ;
    freopen("B-small-attempt1.in" , "r" , stdin) ; freopen("B-small-attempt1.out", "w" ,stdout) ;
    
    int Test ; cin >> Test ;
    cout.precision(9) ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        cin >> N >> V >> X ;
        Init() ;
        cout << "Case #" << i << ": " ;
        Solve() ;
    }
}
