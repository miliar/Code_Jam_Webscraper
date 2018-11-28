#include <cstdio>
#include <cmath>
#include <cstring>
int f[1010];
int a, b;
int main ()
{
    //freopen("a.out","r",stdin);
    //freopen("b.out","w",stdout);
    memset(f,0,sizeof(f));
    for(int i = 1; i <= 9; i++)
    {
        f[i] = 1; f[i*11] = 1;
        for(int j = 0; j <= 9; j++)
        f[101*i+10*j] = 1;
    }
    int cas, t = 0, ans;
    scanf("%d",&cas);
    while(t++<cas)
    {
        scanf("%d%d",&a,&b);
        a = ceil(sqrt(a)); b = floor(sqrt(b));
        ans = 0;
        for(int i = a; i <= b; i++)
            ans+=(f[i]&&f[i*i]);
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
