#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>

#define MAXN 3000

using namespace std;
int A[MAXN];
int T , L ; 

int getDigit()
{
    char ch ; 
    ch = getchar();
    while ( ! ( ( '0' <= ch ) && ( ch <= '9' ) ) ) ch = getchar();
    return ( ch - '0' ) ; 
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int TestCase = 0 ; 
    scanf("%d",&T);
    for ( int TestCase = 1 ; TestCase <= T ; TestCase ++ ) {
        scanf("%d",&L);
        for ( int i = 0 ; i <= L ; i ++ ) A[i] = getDigit() ; 
        int Ans = 0 ; 
        int Now = A[0] ;
        A[0] = 0 ;  
        for ( int i = 1 ; i <= L ; i ++ ) { 
            if ( ( A[i] > 0 ) && ( i > Now ) ) Ans = Ans + i - Now , Now = i ;  
            Now = Now + A[i] ; 
            A[i] = 0 ; 
        }
        printf("Case #%d: %d\n",TestCase,Ans);
    }      
    return 0 ; 
}