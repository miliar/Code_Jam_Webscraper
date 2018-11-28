#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int a[1005],n,m;
int f(int x)
{
    int ret=x;
    for(int i=0;i<n;i++)
    {
        if(a[i]%x==0&&a[i]) ret+=a[i]/x-1;
        else ret+=a[i]/x;
    }
    return ret;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        m=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            m=max(a[i],m);
        }
        int ret=f(1);
        for(int i=2;i<=m;i++)
            ret=min(ret,f(i));
        printf("Case #%d: %d\n",++ca,ret);
    }
    return 0;
}
