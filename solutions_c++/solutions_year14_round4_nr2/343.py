#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int n,a[1005];
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        int ans=0;
        for(int i=0;i<n;i++){
            int pfx=0,sfx=0;
            for(int j=  0;j<i;j++) if(a[j]>a[i]) pfx++;
            for(int j=i+1;j<n;j++) if(a[i]<a[j]) sfx++;
            ans+=min(pfx,sfx);
        }
        printf("Case #%d: %d\n",++no,ans);
    }
}
