#include<cstdio>
int i,j,t,shy[105],sum,ans;
char ipt[105][1005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(i=0;i<t;i++) {
        scanf("%d%s",&shy[i],&ipt[i]);
        for(j=0;j<=shy[i];j++) {
            if(sum<j){ans+=j-sum;sum+=j-sum;}
            sum+=ipt[i][j]-'0';
        }
        printf("Case #%d: %d\n",i+1,ans);
        ans=0;
        sum=0;
    }
}
