#include <bits/stdc++.h>

#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n, cnt, t;
    scanf("%d",&t);
    for ( int k = 1; k <= t; k++ ){
        printf("Case #%d: ",k);
        cnt = 0;
        scanf("%d",&n);
        if ( n == 0 ){
            printf("INSOMNIA\n");
        }
        else{
            bool vis[10];
            int i;
            for ( i = 0; i < 10; i++ ){
                vis[i] = false;
            }
            int tmp;
            for ( i = 1; i <= 1000; i++ ){
                tmp = n * i;
                while( tmp != 0 ){
                    if ( !vis[ tmp % 10 ] ){
                        cnt++;
                        vis[ tmp % 10 ] = true;
                    }
                    tmp /= 10;
                }
                if ( cnt == 10 ){
                    break;
                }
            }
            printf("%d\n",n*i);
        }
    }
    return 0;
}
