#include<iostream>
#include<cstdio>
#define ll long long
using namespace std;
int n,p,q,r,s;
ll a[1000010];
ll pre[1000010],suf[1000010];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int T;
    cin>>T;
    int cas = 1;
    while (T--) {
        scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
        for (int i = 1; i <= n; i++) {
                a[i] = ((ll)(i - 1) * p + q) % r + s;
        }
        a[0] = a[n + 1] = 0;
      //  for (int i =0 ; i <= n + 1; i++) printf("a%d\n",a[i]);
        for (int i = 0; i <= n + 1; i++)
            if (i == 0) pre[i] = a[0];
        else pre[i] = a[i] + pre[i - 1];
        for (int i = n + 1; i >= 0; i--)
            if (i == n + 1) suf[i] = a[n + 1];
        else suf[i] = suf[i + 1] + a[i];
      //  for (int i =0 ; i<= n + 1; i++) printf("p%d\n",pre[i]);
      //  for (int i =0 ; i<= n + 1; i++) printf("s%d\n",suf[i]);
        int p ,q = 1;
        ll ans = suf[0];
        for (p = 1; p <= n; p++) {
            q = max(q,p);
            while (q < n && max(suf[q + 1],suf[0] - suf[q + 1] - pre[p - 1]) > max(suf[q + 2],suf[0] - suf[q + 2] - pre[p - 1])) q++;
            ans = min(ans,max(pre[p - 1],max(suf[q + 1],suf[0] - suf[q + 1] -pre[p - 1])));
        }
        printf("Case #%d: %.11f\n",cas++,(suf[0] - ans) * 1.0 / suf[0]);
    }
}
