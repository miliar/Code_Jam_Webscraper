#include <bits/stdc++.h>

#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t, k, c, s, j;
    scanf("%d",&t);
    for ( int cases = 1; cases <= t; cases++ ){
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d: ",cases);
        if ( s < k ){
            printf("IMPOSSIBLE\n");
        }
        else{
            for ( j = 1; j <= k; j++ ){
                printf("%d ",j);
            }
            printf("\n");
        }
    }
    return 0;
}
