#include<cstdio>
const int maxn=1010;
int T,n,cas=1;
char s[maxn];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%s",&n,s);
        int x=0,ans=0;
        for (int i=0;i<=n;x+=s[i]-'0',i++)
            if (x<i)
            {
                ans+=i-x;
                x=i;
            }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
