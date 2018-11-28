#include <iostream>
#include <cstdio>
#include <cstring>
#define INF 0x3f3f3f3f

using namespace std;
const int M = 1100;
int a[M];

int main()
{
    //freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int T,n,maxn,cnt = 0;
    cin>>T;
    while(T--) {
        scanf("%d",&n);
        maxn = 0;
        for(int i = 1; i <= n; i++) {
            scanf("%d",a + i);
            maxn = max(maxn,a[i]);
            a[i]--;
        }
        int ans = INF;
        for(int i = 1; i <= maxn; i++) {
            int num = 0;
            for(int k = 1; k <= n; k++) {
                num += a[k] / i;
            }
            ans = min(ans,num + i);
        }
        printf("Case #%d: %d\n",++cnt,ans);
    }
    return 0;
}
//
