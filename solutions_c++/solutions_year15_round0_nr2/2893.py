#include<cstdio>
#include<queue>
#include<algorithm>
using namespace std;
int p[1003];
int main(){
    freopen("D://debug/B-large.in","r",stdin);
    freopen("D://debug/x.out","w",stdout);
    int t;scanf("%d",&t);
    int d,i,j,ans,tmp,h;
    for(int cas=1;cas<=t;cas++){
        scanf("%d",&d);
        for(i=1;i<=d;i++)scanf("%d",&p[i]);
        sort(p+1,p+d+1);
        ans=p[d];
        for(j=p[d]-1;j;j--){
            tmp=j;
            for(i=d;i;i--){
                if(p[i]<=j)break;
                tmp+=p[i]/j-1+(p[i]%j!=0);
            }
            if(tmp<ans)ans=tmp;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}

