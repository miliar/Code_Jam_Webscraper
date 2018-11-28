#include<iostream>
using namespace std;
typedef long long lint;
int x[10][10], y[10][10];
bool d[100];

int main() {
    freopen( "A.in", "r", stdin );
    freopen( "A.out", "w", stdout );
    
    int T;
    cin >>T;
    int cas = 0;
    while ( T -- ) {
        int a, b;
        scanf( "%d", &a );
        for ( int i = 1; i <= 4; i ++ ) 
            for ( int j = 1; j <= 4; j ++ )
                scanf( "%d", &x[i][j] );
        scanf( "%d", &b );
        for ( int i = 1; i <= 4; i ++ )
            for ( int j = 1; j <= 4; j ++ )
                scanf( "%d", &y[i][j] );
      
        int ans = -1, sum = 0; 
        memset( d, 0, sizeof(d) );
        for ( int i = 1; i <= 4; i ++ )
            d[x[a][i]] = true;
        
        for ( int i = 1; i <= 4; i ++ )     
            if ( d[y[b][i]] ) {
                if ( ans == -1 ) ans = y[b][i], sum = 1; else sum ++;
            }

        printf( "Case #%d: ", ++cas ); 
        if ( ans == -1 )
            cout <<"Volunteer cheated!"<<endl;
        else if ( sum == 1 ) 
            cout <<ans<<endl;
        else
            cout <<"Bad magician!"<<endl;

    }

    return 0;
}







