#include<cstring>
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
char s[1010];
int a[1010];
int n,k;
int fun(char ch)
{
    if(ch=='-') return 0;
    return 1;
}
int work()
{
    for(int i=1;i<=n-k+1;i++)
    {
        a[i]=fun(s[i])^1;
        for(int j=1;j<k && i-j>=1;j++)
            a[i]^=a[i-j];
    }
    for(int i=n-k+2;i<=n;i++)
    {
        int x=fun(s[i]);
        for(int j=1;j<k && i-j>=1;j++)
            x^=a[i-j];
        if(x==0) return -1;
    }
    int ans=0;
    for(int i=1;i<=n;i++)
        ans+=a[i];
    return ans;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        memset(a,0,sizeof(a));
        scanf("%s",s+1);
        scanf("%d",&k);
        n=strlen(s+1);
        int ans=work();
        printf("Case #%d: ",cas);
        if(ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}
