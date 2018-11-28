/*
 * Author:  chlxyd
 * Created Time:  2014/4/12 19:53:58
 * File Name: A.cpp
 */
#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<ctime>
using namespace std;
const double eps(1e-8);
typedef long long lint;
#define clr(x) memset( x , 0 , sizeof(x) )
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clrs( x , y ) memset( x , y , sizeof(x) )
int T , x , y ;
int a[2][10][10] ;
int cal( int p , int x ) {
    repf( i , 1 , 4 )
        repf( j , 1 , 4 )
            if ( a[p][i][j] == x )
                return i ;
}
int main(){
    freopen("A.out","w",stdout) ;
    scanf("%d" , &T ); 
    repf( t , 1 , T ) {
        scanf("%d" , &x ) ;
        repf( i , 1 , 4 )
            repf( j , 1 , 4 ) scanf("%d" , &a[0][i][j] ) ;
        scanf("%d" , &y ) ;
        repf( i , 1 , 4 )
            repf( j , 1 , 4 ) scanf("%d" , &a[1][i][j] ) ;
        int ans = 0 , ret = 0 ;
        repf( i , 1 , 16 ) {
            int x1 = cal(0,i) , y1 = cal(1,i) ;
            if ( x1 == x && y1 == y ) {
                ans ++ ;
                ret = i ;
            }
        }
        printf("Case #%d: " , t ) ;
        if ( ans == 1 ) printf("%d\n" , ret ) ;
        else if ( ans == 0 ) puts("Volunteer cheated!") ;
        else puts("Bad magician!") ;
    }
}

