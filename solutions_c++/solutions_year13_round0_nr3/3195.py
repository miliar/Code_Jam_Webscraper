#include <stdio.h>
#include <string.h>
#include <math.h>
#define sqr(x) (x)*(x)
#define ll long long
int T,a,b;
int judge(int a)
{
    int b=int(sqrt(a));
    if(sqr(b)!=a)return 0;
    int ret=1;
    int st[10];
    int cp=0,aa=a,bb;
    while(a)
    {
        st[cp++]=a%10;
        a/=10;
    }
    for(int i=0;i<cp;i++)a=a*10+st[i];
    if(a!=aa)return 0;

    cp=0,bb=b;
    while(b)
    {
        st[cp++]=b%10;
        b/=10;
    }
    for(int i=0;i<cp;i++)b=b*10+st[i];
    if(b!=bb)return 0;
    return 1;
}
int main()
{
    scanf("%d",&T);
    int tt=0;
    while(T--)
    {
        scanf("%d%d",&a,&b);
        int ans=0;
        for(int i=a;i<=b;i++)
        {
            if(judge(i))
            {
                ans++;
            }
        }
        printf("Case #%d: %d\n",++tt,ans);
    }
    return 0;
}
