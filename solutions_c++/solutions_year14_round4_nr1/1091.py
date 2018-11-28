#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
int a[1000];
int main()
{
    int T, n, m, x, g = 0;
    scanf("%d", &T);
    while (T --)
    {
        memset(a, 0, sizeof(a));
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++ i){
            scanf("%d", &x);
            a[x] ++;
        }
        int ans = 0;
        for(int i = 0; i <= m; ++ i){
            while(a[i] > 0){
                a[i] --;
                ans ++;
                for(int j = m - i; j > 0; j --){
                    if(a[j] > 0){
                        a[j] --;
                        break;
                    }
                }
                
            }
        }

        printf("Case #%d: %d\n",++g,ans);
    }

    return 0;
}