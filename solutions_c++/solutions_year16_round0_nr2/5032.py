#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;
char s[205];
int d[205];
int main()
{
    freopen("B_large.in","r",stdin);
    freopen("B_large.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        scanf("%s",s);
        int n=strlen(s);
        for(int i=0;i<n;i++)
        if(s[i]=='+') d[i]=1;
        else d[i]=0;
        int cur=1;
        int ans=0;
        for(int i=n-1;i>=0;i--)
        {
            if(cur==d[i]) continue;
            ans++;
            cur^=1;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
