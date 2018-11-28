#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int s[100010];

int main()
{
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        int n,x;
        scanf("%d%d",&n,&x);
        for (int i=0;i<n;i++)
            scanf("%d",&s[i]);
        sort(s,s+n);
        int head=0,tail=n-1,ans=0;
        while (head<=tail)
        {
            if (s[tail]+s[head]<=x) ans++,head++,tail--;
            else tail--,ans++;
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
