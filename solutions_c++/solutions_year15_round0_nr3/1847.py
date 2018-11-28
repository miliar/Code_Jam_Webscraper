#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<string>
using namespace std;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define maxn 200005
int a[5][5];        // i 2;j 3;k 4
int f[5][5];
void ini(int x,int y,int val1,int val2)
{
    a[x][y]=val1;
    f[x][y]=val2;
}
char s[10005];
int p[10005];
int tra(char c)
{
    if(c=='i')  return 2;
    if(c=='j')  return 3;
    if(c=='k')  return 4;
}
int solve(int l,int x)
{
    int tot=0;
    while(x--)
    {
        for(int i=0;i<l;i++)
        {
            p[tot++]=tra(s[i]);
        }
    }
    return tot;
}
struct node
{
    int st;
    int fu;
}now;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ini(1,1,1,0);
    ini(1,2,2,0);
    ini(1,3,3,0);
    ini(1,4,4,0);
    ini(2,1,2,0);
    ini(2,2,1,1);
    ini(2,3,4,0);
    ini(2,4,3,1);
    ini(3,1,3,0);
    ini(3,2,4,1);
    ini(3,3,1,1);
    ini(3,4,2,0);
    ini(4,1,4,0);
    ini(4,2,3,0);
    ini(4,3,2,1);
    ini(4,4,1,1);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int x,l;
        scanf("%d%d",&x,&l);
        scanf("%s",s);
        int len=solve(x,l);
        int flag=0;
        now.st=1;
        now.fu=0;
        for(int i=0;i<len;i++)
        {
            now.fu=(now.fu+f[now.st][p[i]])%2;
            now.st=a[now.st][p[i]];
            if(now.st==2&&now.fu==0&&flag==0)   flag=1;
            if(now.st==4&&now.fu==0&&flag==1)   flag=2;
            if(now.st==1&&now.fu==1&&flag==2&&i==len-1)   flag=3;
        }
        if(flag==3) printf("Case #%d: YES\n",cas);
        else printf("Case #%d: NO\n",cas);
    }
}
