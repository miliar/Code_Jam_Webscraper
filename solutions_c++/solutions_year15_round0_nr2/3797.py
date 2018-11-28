 #include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;
#define INF 0x3f3f3f3f
int a[1200] ;
int main() {
    int t,kase=0;
    int n,sum;
    freopen("B-large.in","r",stdin) ;
    freopen("large.txt","w",stdout) ;
    scanf("%d", &t) ;
    for(kase = 1; kase <= t; kase++)
    {
        scanf("%d", &n) ;
        int maxn = -INF;
        int minn;
        for(int i = 0 ; i < n ; i++)
        {
            scanf("%d", &a[i]) ;
            maxn = max(maxn,a[i]) ;
        }
        minn = maxn ;
        for(int i = 1 ; i <= maxn ; i++)
        {
            sum = i ;
            for(int j = 0 ; j < n ; j++)
            {
                if( a[j] > i )
                {
                    if( a[j]%i == 0 )
                        sum += (a[j]/i-1) ;
                    else
                        sum += (a[j]/i) ;
                }
            }
            minn = min(minn,sum) ;
        }
        printf("Case #%d: %d\n", kase, minn) ;
    }
    fclose(stdin);
    fclose(stdout);
    return 0 ;
}
