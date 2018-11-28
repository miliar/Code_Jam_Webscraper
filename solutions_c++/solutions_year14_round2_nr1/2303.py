#include <bits/stdc++.h>

using namespace std ;
string str[105] ;
int status[105][105][5] ;

int main() {

    #ifndef ONLINE_JUDGE
        freopen( "in.txt" , "r" , stdin ) ;
        freopen( "out.txt" , "w" , stdout ) ;
    #endif // ONLINE_JUDGE

    int t , ans , n ;
    cin >> t ;
    for( int k = 1 ; k <= t ; k++ ) {

        cin >> n ;
        for( int i = 1 ; i <= n ; i++ ) {
            cin >> str[i] ;
        }

        int index , max_index = INT_MIN ;
        memset( status , 0 , sizeof( status ) ) ;
        for( int i = 1 ; i <= n ; i++ ) {
            int j = 1 ;
             status[i][0][0] = str[i][0] ; index = 0 ; status[i][0][1]++ ;
            while( str[i][j] ) {
                if( str[i][j] == str[i][j-1] ) status[i][index][1]++ ;
                else {
                    status[i][++index][0] = str[i][j] ;
                    status[i][index][1]++ ;
                }
                j++ ;
            }
            max_index = max( index , max_index ) ;
        }

        bool flag ;
        for( int j = 0 ; j<= max_index ; j++ ) {
            flag = false ; status[102][j][1] += status[1][j][1] ;
            for( int i = 2 ; i <= n ; i++ ) {
                if( status[i][j][0] != status[1][j][0] ) { flag = true ; break ;}
                else {
                    status[102][j][1] += status[i][j][1] ;
                }
            }
            if( flag ) { break ; }
        }


        cout << "Case #" << k << ": " ;
        if( flag ) cout << "Fegla Won" << endl ;
        else {
            int avg ; ans = 0 ;
            for( int j = 0 ; j <= index ; j++ ) {

                    avg = status[102][j][1]/n ;
                    avg += ( status[102][j][1]%n < ( n - status[102][j][1]%n ) ? 0 : 1 ) ;
                for( int i = 1 ; i <= n ; i++ ) {
                    if( status[i][j][1] > avg ) ans += ( status[i][j][1] - avg ) ;
                    else ans += ( avg - status[i][j][1] ) ;
                }

                //ans += ( status[102][j][1]%n < ( n - status[102][j][1]%n ) ? status[102][j][1]%n : ( n - status[102][j][1]%n ) ) ;
            }
            cout << ans <<   endl ;
        }
    }


    return 0 ;
}
