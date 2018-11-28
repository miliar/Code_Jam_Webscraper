#include <iostream>
#include <cstdio>
using namespace std;

int a[1111],n,cur,ans,T,cas=0;

int main(){
    freopen("B-large.in","rb",stdin);
    freopen("data.out","wb",stdout);
    scanf("%d",&T);
    while (T--){
        scanf("%d",&n);
        ans=0;
        for (int i=1; i<=n; i++) {
            scanf("%d",&a[i]);
            ans=max(ans,a[i]);
        }
        for (int i=1; i<=1000; i++){
            cur=0;
            for (int j=1; j<=n; j++)
                cur+=(a[j]-1)/i;
            ans=min(ans,cur+i);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
