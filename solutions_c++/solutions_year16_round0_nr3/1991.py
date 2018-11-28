#include <bits/stdc++.h>
using namespace std;
const int n = 16;
int res = 500;
char d[n];
long long ans[11];
void dfs(int now)
{
    if (now==n)
    {
        --res;
        d[n]='\0';
        printf("%s%s",d,d);
        for (int i=2;i<=10;++i)
            printf(" %I64d",ans[i]);
        printf("\n");
        return;
    }
    d[now]='1';
    for (int i=2;i<=10;++i)
        ans[i]=ans[i]*i+1;
    dfs(now+1);
    if (res==0) return;
    for (int i=2;i<=10;++i)
        ans[i]/=i;
    if (now!=0&&now!=n-1)
    {
        d[now]='0';
        for (int i=2;i<=10;++i)
            ans[i]=ans[i]*i;
        dfs(now+1);
        if (res==0) return;
        for (int i=2;i<=10;++i)
            ans[i]/=i;
    }
}
int main()
{
    freopen("output.txt","w",stdout);
    memset(ans,0,sizeof ans);
    puts("Case #1:");
    dfs(0);
    return 0;
}
