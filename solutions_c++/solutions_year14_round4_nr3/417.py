#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std ;
const int inf = 1000000000 ;
int w , h , b ;
int ch[501][501];
int f[501][501] ;
int dir[8][2] = {0,1,0,-1,1,0,-1,0,
                 1,1,1,-1,-1,1,-1,-1
                };
int hashs[501][501] ;
int que[501*501][2] , cl , op ;
int ans ;
void put( int x , int y , int v ) {

    if ( f[x][y] > v ) {
        f[x][y] = v ;
        if ( hashs[x][y] == 0 ) {
            hashs[x][y] = 1 ;
            que[op][0] = x ;
            que[op][1] = y;
            ++op ;
        }
    }
}
bool inside( int x , int y ) {
    return x >= 0 && x < w && y >= 0 && y < h ;
}

void spfa() {

    cl = op = 0 ;
    for ( int i = 0 ; i < w ; ++i )
        for ( int j = 0 ; j < h ; ++j ) {
            f[i][j] = inf ;
            hashs[i][j] = 0 ;
        }

    for ( int j = 0 ; j < h ; ++j ) {
        put(0,j,1-ch[0][j]);
    }

    while ( cl < op ) {

        int x = que[cl][0] ;
        int y = que[cl][1] ;

        for ( int l = 0 ; l < 8 ; ++l )
        {
            int xx , yy ;
            xx = x + dir[l][0] ;
            yy = y + dir[l][1] ;
            if ( inside(xx,yy) ){
                int c = 1-ch[xx][yy] ;
                put( xx,yy,c+f[x][y] );
            }
        }
        hashs[x][y] = 0 ;
        ++cl ;
    }

    for ( int j = 0 ; j < h ; ++j )
        if ( f[w-1][j] < ans )
            ans = f[w-1][j] ;
}


int main(){

    int T , test = 1 ;
    cin >> T ;
    while ( T -- ) {

        cin >> w >> h >> b ;
        for ( int i = 0 ; i < w ; ++i )
            for ( int j = 0 ; j < h ; ++j )
                ch[i][j] = 0 ;

        for ( int i = 0 ; i < b ; ++i )
        {
            int x0 , x1 , y0 , y1 ;
            cin >> x0 >> y0 >> x1 >> y1 ;
            for ( int j = x0 ; j <= x1 ; ++j )
                for ( int k = y0 ; k <= y1 ; ++k )
                    ch[j][k] = 1 ;
        }
        ans = inf ;
        spfa();
        cout << "Case #" << test++ << ": ";
        cout << ans << endl ;

    }

    return 0;
}
