#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int t,n;
int a[1010];

int main()
{
#ifdef Haha
    freopen("B-large.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
#endif // Haha
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a,a+n);
        int ans=1000000000;
        for(int i=1;i<=a[n-1];i++){
            int res=0;
            for(int j=0;j<n;j++){
                if(a[j]>i){
                    res+=(a[j]+i-1)/i-1;
                }
            }
            res+=i;
            ans=min(ans,res);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
