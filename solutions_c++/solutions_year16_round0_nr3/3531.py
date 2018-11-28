#include<iostream>
#include<cstdio> 
using namespace std;
const int N=1e5+10;
int vis[N],prime[N],tot=0;
int n=15, have=0, ok = 0;
int a[N];
int check(long long n) {
    if (n <= prime[tot]) {
        if (!vis[n]) {
            return -1;
        }
    }
    for (int i = 1; i <= tot; ++i) {
        if (n % prime[i] == 0) {
            return prime[i];
        }
    }
    return -1;
}
void dfs(int dep)
{
    if (ok) return;
    if(dep==n)
    {
        a[n]=1;
        int data[11];
        memset(data,0,sizeof(data));
        int flag=1;
        for(int i=2;i<=10;++i)
        {
            long long cur=0;
            for(int j=0;j<=n;++j)
            {
                cur=cur*i+a[j];
            }
            data[i]=check(cur);
            if(data[i]==-1)
            {
                flag = 0;
                break;
            }
        }
        if(flag)
        {
            for(int i=0;i<=15;++i) {
                printf("%d", a[i]);
            }
            for (int i = 2; i <= 10; ++i) {
                printf(" %d", data[i]);
            }
            printf("\n");
            if(++have==50) ok = 1;
        }
        return;
    }
    a[dep]=0;
    dfs(dep+1);
    a[dep]=1;
    dfs(dep+1);
}
void init()
{
    int n=1e5;
    memset(vis,0,sizeof(vis));
    for(int i=2;i<n;++i)
    {
        if(!vis[i])
        {
            prime[++tot]=i;
            for(int j=i+i;j<n;j+=i)vis[j]=1;
        }
    }
}
int main() 
{
    init();
    printf("Case #1:\n");
    a[0]=1;
    dfs(1);
    return 0;
}
