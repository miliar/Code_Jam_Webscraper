#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <ctime>
#include <vector>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

bool f[1010];

bool pd(int x)
{
    int y=x;
    int n=0;
    int a[10];
    while (y>0)
    {
        n++;
        a[n]=y%10;
        y/=10;
    }
    for (int i=1;i<=n;i++)
    {
        if (a[i]!=a[n-i+1]) return false;
    }
    return true;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    memset(f,0,sizeof(f));
    f[1]=true;
    f[4]=f[9]=true;
    for (int i=1;i<=1000;i++)
    {
        if (pd(i) && pd(i*i) && i*i<=1000)
            f[i*i]=true;
    }
    int cas=1;
    while (T--)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        int ans=0;
        for (int i=a;i<=b;i++)
        if (f[i]) ans++;
        printf("Case #%d: %d\n",cas++,ans);
    }
}
