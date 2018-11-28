#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

#define MAXN 1000

char G[MAXN][MAXN];
int  F[MAXN][MAXN];
char tmp[MAXN] ; 
int R , C ; 
int Ans = 0 ; 

void Init()
{
    scanf("%d %d",&R,&C);gets(tmp);
    for ( int i = 1 ; i <= R ; i ++ ){ 
        for ( int j = 1 ; j <= C ; j ++ ) 
            scanf("%c",&G[i][j]);
        gets(tmp);
    }
}

void Count()
{
    Ans = 0 ; 
    memset( F , 0 , sizeof(F) ) ; 
    for ( int i = 1 ; i <= R ; i ++ ) {
        for ( int j = 1 ; j <= C ; j ++ ) {
            if ( i == 1 ) { 
                F[i][j] |= 1 ; 
            } else {
                if ( ( F[i-1][j] & 1 ) && 
                     ( G[i-1][j] == '.' ) ) {
                    F[i][j] |= 1 ; 
                }
            }
        }
    }
    for ( int i = 1 ; i <= R ; i ++ ) {
        for ( int j = 1 ; j <= C ; j ++ ) {
            if ( j == 1 ) { 
                F[i][j] |= 2 ; 
            } else {
                if ( ( F[i][j-1] & 2 ) && 
                     ( G[i][j-1] == '.' ) ) {
                    F[i][j] |= 2 ; 
                }
            }
        }
    }
    for ( int i = R ; i >= 1 ; i -- ) {
        for ( int j = C ; j >= 1 ; j -- ) {
            if ( i == R ) { 
                F[i][j] |= 4 ; 
            } else {
                if ( ( F[i+1][j] & 4 ) && 
                     ( G[i+1][j] == '.' ) ) {
                    F[i][j] |= 4 ; 
                }
            }
        }
    }
    for ( int i = R ; i >= 1 ; i -- ) {
        for ( int j = C ; j >= 1 ; j -- ) {
            if ( j == C ) { 
                F[i][j] |= 8 ; 
            } else {
                if ( ( F[i][j+1] & 8 ) && 
                     ( G[i][j+1] == '.' ) ) {
                    F[i][j] |= 8 ; 
                }
            }
        }
    }
    for ( int i = 1 ; i <= R ; i ++ ) 
        for ( int j = 1 ; j <= C ; j ++ ) {
            if ( ( F[i][j] == 15 ) && ( G[i][j] != '.' ) ) {
                Ans = -1 ; return ;
            }
            if ( ( G[i][j] == '^' ) && ( F[i][j] & 1 ) ) Ans ++ ; 
            if ( ( G[i][j] == '<' ) && ( F[i][j] & 2 ) ) Ans ++ ; 
            if ( ( G[i][j] == 'v' ) && ( F[i][j] & 4 ) ) Ans ++ ; 
            if ( ( G[i][j] == '>' ) && ( F[i][j] & 8 ) ) Ans ++ ; 
        }
}

int main()
{
    int T ;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for ( int i = 1 ; i <= T ; i ++ ) {
        Init();
        printf("Case #%d: ",i);
        Count();
        if ( Ans == -1 ) 
            printf("IMPOSSIBLE\n");
        else 
            printf("%d\n",Ans);
    }
    return 0 ;
}