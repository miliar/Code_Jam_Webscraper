#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#define prt(k) cout<<#k" = "<<k<<endl;
using namespace std;
typedef long long ll;
char s[2333];
int sum[2333];
int a[2333];
int main()
{
    freopen("A.in","r",stdin); freopen("A.out","w",stdout);
    int re, ca=1; cin>>re;
    while (re--)
    {
        int n;
        scanf("%d%s", &n, s);
        for (int i=0;i<=n;i++)
            a[i]=s[i]-'0';
        sum[0]=  a[0];
        for (int i=1;i<=n;i++)
            sum[i]=sum[i-1] + a[i];
        int ans = 0;
        for (int i=1;i<=n;i++)
            ans = max(ans, i-sum[i-1]);
        printf("Case #%d: %d\n", ca++, ans);
    }
    return 0;
}
