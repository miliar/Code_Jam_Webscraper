#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std ;

int map[11][11] ;

int n , m ;

int judge( int x )
{
    int i , j ;
    for( j = 0 ; j < m ; j ++ )
    {
        if( map[x][j] != 1 )
            return 1 ;
    }
    return 0 ;
}

int make( int y )
{
    int i ;
    for( i = 0 ; i < n ; i ++ )
    {
        if( map[i][y] != 1 )
            return 1 ;
    }
    return 0 ;
}

int solve()
{
    int i , j ;
    for( i = 0 ; i < n ; i ++ )
    {
        for( j = 0 ; j < m ; j ++ )
        {
            if( map[i][j] == 1 )
            {
                if( judge( i ) && make( j ) )
                    return 0 ;
            }
        }
    }
    return 1 ;
}

int main()
{
    freopen("in.txt" , "r" , stdin) ;
    freopen("out.txt" , "w" , stdout) ;
    int cas , i , j , T ;
    scanf("%d" , &T) ;
    for( cas = 1 ; cas <= T ; cas ++ )
    {
        scanf("%d %d" , &n , &m) ;
        for( i = 0 ; i < n ; i ++ )
        {
            for( j = 0 ; j < m ; j ++ )
                scanf("%d" , &map[i][j]) ;
        }
        if( solve() )
            printf("Case #%d: YES\n" , cas) ;
        else
            printf("Case #%d: NO\n" , cas) ;
    }
    return 0 ;
}
