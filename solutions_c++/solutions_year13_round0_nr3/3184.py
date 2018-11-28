#include <iostream>
#include <cstdio>
#define LL long long
using namespace std;
int a[1000000];
struct cong
{
    LL a,b;
    cong(){}
    cong(LL c,LL d)
    {
        a = c;
        b = d;
    }
};
cong v[1000000];
bool check(LL x)
{
    int cnt = 0;
    while (x)
    {
        int y = x % 10;
        x /= 10;
        a[cnt++] = y;
    }
    cnt--;
    for (int i=0;i<=cnt/2;i++)
    {
        if (a[i]!=a[cnt-i]) return false;
    }
    return true;
}
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int cnt = 0;
    for (LL i=1;i<=10000000;i++)
    {
        LL x = i*i;
        if (check(x) && check(i))
        {
            v[cnt++] = cong(i,x);
        }
    }
/*
    for (int i=0;i<cnt;i++)
    {
        printf("%lld %lld\n",v[i].a,v[i].b);
    }
*/
    int T;
    scanf("%d",&T);
    int cas = 0;
    int x,y;
    while (T--)
    {
        scanf("%d%d",&x,&y);
        int t1,t2;
        for (int i=0;i<cnt;i++)
            if (v[i].b<x) continue;
            else {t1 = i;break;}
        for (int i=t1;i<cnt;i++)
            if (v[i].b<=y) continue;
            else {t2 = i;break;}
        printf("Case #%d: %d\n",++cas,t2-t1);
    }

    return 0;
}
