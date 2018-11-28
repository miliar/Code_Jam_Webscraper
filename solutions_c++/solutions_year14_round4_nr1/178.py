#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int A[10005],Hash[10005];
int main(){
    int n,m,i,j,k,l,T,tt=0;
    scanf("%d",&T);
    freopen("A.out","w",stdout);
    while(T--){
        tt++;
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++){
            scanf("%d",&A[i]);
            Hash[i]=0;
        }
        int ans=0;
        sort(A+1,A+1+n);
        j=1;
        for(i=n;i>=1;i--)
            if(!Hash[i]){
                while(j<=n&&Hash[j]&&A[j]+A[i]<=m)j++;
                if(j==i||A[i]+A[j]>m){
                    ans++;
                    Hash[i]=1;
                }else{
                    ans++;
                    Hash[i]=1;
                    Hash[j]=1;
                }
            }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
