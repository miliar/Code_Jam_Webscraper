#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int a[105];
char s[105];

int dp_f[105];
int dp_g[105];
int g(int n);
int f(int n)
{
    if(n<0)
        return 0;
    if(dp_f[n]!=-1)
        return dp_f[n];
    if(s[n]=='+')
        return dp_f[n]=f(n-1);
    else
        return dp_f[n]=1+g(n-1);
}
int g(int n)
{
    if(n<0)
        return 0;
    if (dp_g[n]!=-1)
        return dp_g[n];
    if (s[n]=='-')
        return dp_g[n]=g(n-1);
    else
        return dp_g[n]=1+f(n-1);
}

int main()
{
    freopen("C:\\Users\\lpc\\Downloads\\B-large.in","r",stdin);
    freopen("e:\\codejam\\2L.txt","w",stdout);
    int t;
    int cs=0;
    scanf("%d",&t);
    while (t--)
    {
        memset(dp_f,-1, sizeof(dp_f));
        memset(dp_g,-1, sizeof(dp_g));
        scanf("%s",s);
        printf("Case #%d: %d\n",++cs,f(strlen(s)-1));
    }
    return 0;
}