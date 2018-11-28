#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

int n;
int a[1005];

int main(){
    freopen("Qua_B(large).in","r",stdin);
    freopen("Qua_B.out","w",stdout);
    int test, cnt= 0; scanf("%d", &test);
    while(test--){
        scanf("%d", &n);
        int res= 1005;
        for(int i=1;i<=n;i++) scanf("%d", &a[i]);
        for(int i=1;i<=1000;i++){
            int cost= i;
            for(int j=1;j<=n;j++) cost+= (a[j]-1)/i;
            res= min(res, cost);
        }
        cnt++; printf("Case #%d: %d\n", cnt, res);
    }
    return 0;
}
