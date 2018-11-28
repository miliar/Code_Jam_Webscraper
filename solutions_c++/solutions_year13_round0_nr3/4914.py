#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std ;

int solve( int k )
{
    int a[111] ;
    int flag = 0 ;
    while( k )
    {
        int t = k % 10 ;
        a[flag ++] = t ;
        k /= 10 ;
    }
    for( int i = 0 ; i < flag ; i ++ )
    {
        if( a[i] != a[flag - 1 - i] )
            return 0 ;
    }
    return 1 ;
}

int judge( int k )
{
    int c = (int)sqrt((double) k) ;
    if( c * c != k )
        return 0 ;
    if( solve( k ) && solve( c ) )
        return 1 ;
    return 0 ;

}

int main()
{
    int cas , T , i , j , ans , a , b ;

    freopen("in.txt" , "r" , stdin) ;
    freopen("out.txt" , "w" , stdout) ;
    scanf("%d" , &T) ;
    for( cas = 1 ; cas <= T ; cas ++ )
    {
        scanf("%d %d" , &a , &b) ;
        ans = 0 ;
        for( i = a ; i <= b ; i ++ )
        {
            if( judge( i ) )
                ans ++ ;
        }
        printf("Case #%d: %d\n" , cas , ans) ;
    }
    return 0 ;
}
