#include<cstdio>
#include<algorithm>
using namespace std;
char s[1004];
int main(){
    freopen("D://debug/A-large.in","r",stdin);
    freopen("D://debug/x.out","w",stdout);
    int t;scanf("%d",&t);
    int sm,ans,sum,i;
    for(int cas=1;cas<=t;cas++){
        scanf("%d%s",&sm,s);
        sum=ans=0;
        for(i=0;i<=sm;i++){
            if(sum<i)ans=max(ans,i-sum);
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
