#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std ;

int  t , cs = 1 , n , m , f[105][105] ;

int main(){
    freopen("t.out","w",stdout) ;
    cin >> t ;
    while ( t -- )
    {
        cin >> n >> m ;
        for ( int i = 0;i < n;i ++)
            for ( int j =0;j < m;j ++)
                cin >> f[i][j] ;
        int ans = 1 ;

        for ( int i = 0 ;i < n ; i ++)
            {
            if ( ans == 0 ) break ;
            int equ = 1 ;
            for ( int j = 1;j < m;j ++)
                if ( f[i][j] != f[i][j-1]) { equ = 0 ; break; }
            if ( equ ) continue ;
            int k = 0 , minn  = f[i][0] ;
            for (int j = 1;j < m;j ++)
                if ( f[i][j] < minn ) { minn = f[i][j] , k = j ; }
            for ( int k = 0;k < m; k ++)
                if ( f[i][k] == minn ){
                    for ( int j = 0;j < n;j ++)
                        if ( f[j][k] > minn) {
                        ans = 0 ; break ;
                }
               }
        }
        if (ans) printf("Case #%d: YES\n" , cs++) ;
        else printf("Case #%d: NO\n",cs++) ;
        //if ( ans ) cout << "Case #"<<cs++<<": YES"<<endl;
        //else cout << "Case #"<<cs++<<": NO"<<endl;
    }
    return 0 ;
}
