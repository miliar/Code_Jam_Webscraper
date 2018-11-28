#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
#define mem(a) memset( a, 0, sizeof(a) )
using namespace std;
typedef long long ll;

int a[20];
bool vis[10];
int main()
{
    ll b, c, i, j, n;
    int T, cas = 1, cnt;
    freopen("A-large.in", "r", stdin );
    freopen("out.txt", "w", stdout );
    scanf("%d", &T);
    while( T -- ){
        scanf("%lld", &n);
        if( n == 0 ){
            printf("Case #%d: INSOMNIA\n", cas ++ );
            continue;
        }
        i = 1;
        mem( vis );
        while(1){
            ll tmp = n*i;
            cnt = 0;
            while( tmp ){
                a[cnt++] = tmp%10;
                tmp /= 10;
            }
            for( j = 0; j < cnt; j ++ )vis[a[j]] = 1;
            int fl = 0;
            for( j = 0; j <= 9; j ++ )
                if( !vis[j] ){
                    fl = 1;
                    break;
                }
            if( !fl ) break;
            else i++;
        }
        printf("Case #%d: %lld\n", cas++, i*n );
    }
}
