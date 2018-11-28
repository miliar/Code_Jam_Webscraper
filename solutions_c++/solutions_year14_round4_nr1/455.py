#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
using namespace std;
int s[100005],is[100005];
int cmp(int a,int b){
    return a>b;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,m,i,j,ans,C=0;
    scanf("%d",&t);
    while(t--){
        memset(is,0,sizeof(is));
        scanf("%d%d",&n,&m);
        ans=0;
        for(i=0;i<n;i++)
            scanf("%d",&s[i]);
        sort(s,s+n,cmp);
        for(i=0;i<n;i++){
            if(is[i]) continue;
            is[i]=1;
            ans++;
            for(j=i+1;j<n;j++){
                if(s[i]+s[j]<=m && is[j]==0){
                    is[j]=1;
                    break;
                }
            }
        }
        printf("Case #%d: %d\n",++C,ans);
    }
}
