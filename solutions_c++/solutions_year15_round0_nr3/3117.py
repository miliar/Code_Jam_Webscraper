#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=10010;
char str[maxn];
int matrix[5][5]=
{
    {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1},
};
int rev[maxn];
int main()
{
    int T,cas=1;
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        int n,x;
        scanf("%d%d",&n,&x);
        scanf("%s",str);
        for(int i=0;i<n;i++)
            str[i]=str[i]-'i'+2;
        int tot=n*x;
        rev[tot]=1;
        for(int i=tot-1;i>=0;i--)
            if(rev[i+1]<0)  rev[i]=-matrix[str[i%n]][-rev[i+1]];
            else rev[i]=matrix[str[i%n]][rev[i+1]];
        int now=1,flag=true;
        for(int i=0;flag&&i<tot;i++)
        {
            if(now<0)   now=-matrix[-now][str[i%n]];
            else now=matrix[now][str[i%n]];
            if(now==2)
            {
                int now1=1;
                for(int j=i+1;flag&&j<tot;j++)
                {
                    if(now1<0)  now1=-matrix[-now1][str[j%n]];
                    else now1=matrix[now1][str[j%n]];
                    if(now1==3&&rev[j+1]==4)    flag=false;
                }
            }
        }
        if(flag)    printf("Case #%d: NO\n",cas++);
        else printf("Case #%d: YES\n",cas++);
    }
    return 0;
}
