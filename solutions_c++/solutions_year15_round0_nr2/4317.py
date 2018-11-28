#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAXN 2000
#define MAXL 1000
int A[MAXN];
int S[MAXN];
int T , N ; 

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int TestCase = 0 ;
    scanf("%d",&T);
    for ( TestCase = 1 ; TestCase <= T ; TestCase ++ ) {
        scanf("%d",&N);
        memset(S,0,sizeof(S));
        for ( int i = 1 ; i <= N ; i ++ ) scanf("%d",&A[i]) , S[A[i]]++; 
        for ( int i = 1 ; i < MAXN ; i ++ ) S[i] = S[i-1] + S[i]; 
        int MAXS = -1 ; 
        for ( int i = 1 ; i <= N ; i ++ ) if ( A[i] >= MAXS ) MAXS = A[i] ; 
        int Ans = MAXS ; 
        for ( int i = 1 ; i <= MAXS ; i ++ ) {
            int tmp = 0 ; 
            for ( int j = 1 ; j <= MAXS / i ; j ++ ) 
                tmp += j * ( S[ ( j + 1 ) * i ] - S[ j * i ] ) ; 
            if ( tmp + i < Ans ) Ans = tmp + i ; 
        }
        printf("Case #%d: %d\n",TestCase,Ans);
    }
    return 0 ; 
}
            