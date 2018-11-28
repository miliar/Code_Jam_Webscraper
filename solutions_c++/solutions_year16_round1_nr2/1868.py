#include <stdio.h>
#include <algorithm>
using namespace std;
int cnt[3000],ans[55];
int main (void)
{
    int i,j,k,t,n,p,len;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d",&n);
        for(j=0;j<2*n-1;j++){
            for(k=0;k<n;k++){
                scanf("%d",&p);
                cnt[p]++;
            }
        }
        len=0;
        for(j=1;j<=2500;j++){
            if(cnt[j]%2) ans[len++]=j;
            cnt[j]=0;
        }

        printf("Case #%d:",i+1);
        for(j=0;j<len;j++)
            printf(" %d",ans[j]);

        printf("\n");

    }

    return 0;
}
