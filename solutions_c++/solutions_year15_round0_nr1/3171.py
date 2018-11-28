#include<cstdio>
char s[1010];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int sum,ans,T,n,i,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        scanf("%s",s);
        sum=s[0]-'0';
        ans=0;
        for(i=1;i<=n;i++)
        {
            if(sum<i) ans+=i-sum,sum=i;
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
