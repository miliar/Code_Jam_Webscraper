#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int dp[10010][10010];
char s[10010];
int road[5][5]={0,0,0,0,0, 0,1,2,3,4, 0,2,-1,4,-3, 0,3,-4,-1,2, 0,4,3,-2,-1};
int id(char c)
{
    if(c=='1')
        return 1;
    if(c=='i')
        return 2;
    if(c=='j')
        return 3;
    return 4;
}
int abs(int a)
{
    return a>0?a:-a;
}
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int t;
    scanf("%d",&t);
    int c=t;
    while(t--)
    {
        int x,l;
        scanf("%d%d",&l,&x);
        scanf("%s",s);
        for(int i=0;i<x;i++)
        {
            for(int j=0;j<l;j++)
                s[i*l+j]=s[j];
        }
        for(int i=0;i<x*l;i++)
            dp[i][i]=id(s[i]);
        for(int len=2;len<=x*l;len++)
        {
            for(int i=0;i<x*l;i++)
            {
                int j=i+len-1;
                if(j>=x*l)break;
                int flag=dp[i][j-1]>0?1:-1;
                dp[i][j]=flag*road[abs(dp[i][j-1])][id(s[j])];
            }
        }
        int ok=0;
        for(int i=1;i<x*l;i++)
        {
            if(dp[0][i-1]!=2)continue;
            for(int j=i+1;j<x*l;j++)
            {
                if(dp[i][j-1]==3&&dp[j][x*l-1]==4)
                {
                    ok=1;
                    break;
                }
            }
            if(ok)break;
        }
        if(ok)
            printf("Case #%d: YES\n",c-t);
        else printf("Case #%d: NO\n",c-t);
    }
}
