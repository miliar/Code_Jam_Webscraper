#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>
#include <string>
#include <vector>
using namespace std;
#define N 1010
int a[N];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,n,cas=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        for(int i=0;i<=n;i++){
            scanf("%1d",&a[i]);
        }
        int ans=0;
        if(a[0]==0){
            a[0]=1;
            ++ans;
        }
        for(int i=1;i<=n;i++){
            if(a[i-1]<i){
                ans+=i-a[i-1];
                a[i]=a[i]+i;
            }
            else{
                a[i]+=a[i-1];
            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
