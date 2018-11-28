#include<cstdio>
#define N 10010
int ii,test,i,f[N],ans,sum,n;
char s[N];
int main()
{
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&test);
    for (ii=1;ii<=test;ii++)
    {
        scanf("%d",&n);
        scanf("%s",s);
        for (i=0;i<=n;i++)
        f[i]=s[i]-48;
        
        sum=f[0];ans=0;
        for (i=1;i<=n;i++)
        if (f[i])
        {
                 if (sum<i)
                 {
                           ans+=i-sum;
                           sum=i;
                 }
                 sum=sum+f[i];
        }
        printf("Case #%d: %d\n",ii,ans);
    }
}
