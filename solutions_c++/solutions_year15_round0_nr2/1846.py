#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int T,n,ans,a[23333],f[23333];

int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
for(int t=1;t<=T;t++){
    ans=23333333;
    scanf("%d",&n);for(int i=1;i<=n;i++)scanf("%d",&a[i]);
    for(int i=1;i<=1000;i++){
        f[i]=i;
        for(int j=1;j<=n;j++){
            if(a[j]>i)f[i]+=((a[j]%i)?(a[j]/i):(a[j]/i)-1);
        }
        ans=min(ans,f[i]);
    }
    printf("Case #%d: %d\n",t,ans);
}
    return 0;
}
