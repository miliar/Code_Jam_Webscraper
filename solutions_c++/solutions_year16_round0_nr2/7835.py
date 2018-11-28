//GCJ 2016Q B
#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXL 105
using namespace std;
char c[MAXL];
int solve()
{
    int ans=0;
    int len = strlen(c);
    if(c[0]=='-') ans++;
    for(int i=1;i<len;++i)
    {
        if(c[i]=='-'&&c[i-1]=='+')
            ans+=2;
    }
    return ans;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int Case;
    scanf("%d",&Case);
    for(int t=1;t<=Case;++t)
    {
        scanf("%s",&c);
        printf("Case #%d: %d\n",t,solve());
    }
    return 0;
}
