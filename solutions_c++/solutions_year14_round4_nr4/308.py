#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define drep( i, j, k ) for( i = j ; i >= k ; --i )
#define Maxn 115
#define MaxL 115
#define MaxD 1015

int n, Ans, CAns, T, Case, L[Maxn], C, m, sel[Maxn] ;
char S[Maxn][MaxL] ;
struct Tree {
        char V ;
        int L, R ;
        #define lc( p ) Tr[p].L
        #define rc( p ) Tr[p].R
        #define v( p ) Tr[p].V 
} Tr[MaxD] ;

inline void Insert( int t )
{
        int i, p ;
        
        for( p = 0, i = 1 ; i <= L[t] ; ++i ) {
                if( ! lc( p ) ) {
                        lc( p ) = ++C ;
                        v( C ) = S[t][i] ;
                        p = C ;
                } else {
                        for( p = lc( p ) ; rc( p ) && ( v( p ) != S[t][i] ) ; p = rc( p ) ) ;   
                        if( v( p ) != S[t][i] ) {
                                rc( p ) = ++ C ;
                                v( C ) = S[t][i] ;
                                p = C ;         
                        }
                }
        }
}

void Dfs( int p )
{
        int tans, i, j ;
        bool vis[Maxn] ;
        
        if( p > m ) {
                memset( vis, 0, sizeof( vis ) ) ;               
                rep( i, 1, m )
                        vis[sel[i]] = 1 ;
                rep( i, 1, n ) 
                        if( ! vis[i] ) return ;
                        
                tans = 0 ; 
                rep( i, 1, n ) {
                        C = 0 ;
                        memset( Tr, 0, sizeof( Tr ) ) ;
                        rep( j, 1, m ) 
                                if( sel[j] == i ) 
                                        Insert( j ) ;   
                        
                        tans += ( C + 1 ) ;
                }       
                
                if( tans > Ans ) {
                        Ans = tans ;
                        CAns = 1 ;
                } else if( tans == Ans )
                        ++ CAns ;
                
                return ; 
        }
        
        rep( i, 1, n ) {
                sel[p] = i ;
                Dfs( p + 1 ) ;  
        }
        
}

int main()
{
        
        freopen("D.in", "r", stdin);
        freopen("D.out", "w", stdout);
        
        int i ;
        
        for( scanf("%d", &T) ; T-- ; ) {
                Ans = CAns = 0 ;
                
                scanf("%d%d\n", &m, &n) ;       
                rep( i, 1, m ) {
                        scanf("%s", S[i]+1) ;   
                        L[i] = strlen( S[i]+1 ) ; 
                }
                
                Dfs( 1 ) ;
                
                printf("Case #%d: %d %d\n", ++ Case, Ans, CAns ) ; 
        }
        return 0 ; 
        
        fclose(stdin);
        fclose(stdout);
        
}
