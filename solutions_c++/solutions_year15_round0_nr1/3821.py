#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int S;
char ch[1005];
void Solve()
{
    int n,T,cnt=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        scanf(" %s",ch);
        int ans=0,now=0,t;
        for(int i=0;i<=n;i++)
        {
            t=ch[i]-'0';
            if(i<=now)now+=t;
            else
            {
                ans+=i-now;
                now=i+t;
            }
        }
        printf("Case #%d: %d\n",++cnt,ans);
    }
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    Solve();
    return 0;
}
