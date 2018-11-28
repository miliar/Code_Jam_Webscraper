#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

bool vis[10];
bool judge(int n)
{
    while(n)
    {
        vis[n%10]=1;
        n/=10;
    }
    for(int i=0;i<10;i++)
        if(!vis[i])
            return false;
    return true;
}
int solve(int n)
{
    memset(vis,0,sizeof(vis));
    for(int i=1;i<=100;i++)
        if(judge(n*i))
            return n*i;
    return -1;
}
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",cas++);
        if(n==0)    printf("INSOMNIA\n");
        else    printf("%d\n",solve(n));
    }
    return 0;
}
