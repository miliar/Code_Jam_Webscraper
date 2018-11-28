#include <bits/stdc++.h>

#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t, n, j, cnt, i;
    scanf("%d %d %d",&t,&n,&cnt);
    printf("Case #1:\n");
    for ( i = 1; i <= cnt; i++ ){
        printf("11");
        for ( j = ( n - 4 ) / 2 - 1; j >= 0; j-- ){
            if ( ( ( i >> j ) & 1 ) == 1 ){
                printf("11");
            }
            else{
                printf("00");
            }
        }
        printf("11 ");
        for ( j = 3; j <= 11; j++ ){
            printf("%d ",j);
        }
        printf("\n");
    }
    return 0;
}
