#include <cstdio>
#include <cstring>
#include <iostream>
#define fo(i) for(int i=1;i<=4;i++)
using namespace std ;
int k , ans , A[10][10] , B[10][10] , cnt[100] ;
void Solve() {
	memset( cnt , 0 , sizeof(cnt) ) ;
    scanf("%d", &k); fo(i) fo(j) scanf("%d" , &A[i][j]) ; fo(i) cnt[A[k][i]] ++ ;
    scanf("%d", &k); fo(i) fo(j) scanf("%d" , &B[i][j]) ; fo(i) cnt[B[k][i]] ++ ;
    ans = -1;
    for ( int i = 1 ; i <= 16 ; i ++ ) if ( cnt[i] == 2 ) if ( ans == -1 ) ans = i ; else { printf("Bad magician!\n") ; return ; }
	if (ans == -1) printf("Volunteer cheated!\n") ; else printf("%d\n", ans) ;
}

int main() {
//    freopen("A.in","r",stdin) ; freopen("A.out","w",stdout) ;
	freopen("A-small-attempt0.in","r",stdin) ; freopen("A-small-attempt0.out","w",stdout) ;
    int Test ; scanf("%d" , &Test) ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        printf( "Case #%d: " , i ) ;
		Solve() ;
	}
}
