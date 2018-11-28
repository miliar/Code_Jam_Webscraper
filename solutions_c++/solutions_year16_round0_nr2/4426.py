#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
using namespace std;
char s[700];
int a[700];
int main()
{
#ifndef ONLINE_JUDGE
    freopen("B-large (1).in", "r", stdin);
    freopen("out1.out", "w", stdout);
#endif
    int T;
    scanf("%d",&T);
    int u=0;
    while(T--)
    {
        int ans=0;
        scanf("%s",s);
        int len=strlen(s);
        for(int i=0;i<len;i++)
        {
            if(s[i]=='-') a[i]=0;
            else if(s[i]=='+') a[i]=1;
        }
        for(int i=0;i<len-1;i++)
        {
            if(a[i]!=a[i+1])
            {
                a[i]=a[i+1];
                ans++;
            }
        }
        if(a[len-1]==0) printf("Case #%d: %d\n",++u,ans+1);
        else printf("Case #%d: %d\n",++u,ans);
    }
    return 0;
}
