#include <bits/stdc++.h>
using namespace std;

const int N = 1010;

int solve1(int b[],int n)
{
    int ans = 0;
    for(int i = 1; i <= n; i ++)
        for(int j = i + 1; j <= n; j ++)
            if(b[i] > b[j]) ans ++;
    return ans;
}

int solve2(int c[],int n)
{
    int ans = 0;
    for(int i = 1; i <= n; i ++)
        for(int j = i + 1; j <= n; j ++)
            if(c[i] < c[j]) ans ++;
    return ans;
}

void solve()
{
    int a[N],n;
    scanf("%d",&n);
    for(int i = 1; i <= n; i ++) scanf("%d",&a[i]);
    int ans = 0;
    for(int i = 1; i <= n; i ++) {
        int x = 0,y = 0;
        for(int j = 1; j < i; j ++)
            if(a[j] > a[i]) x ++;
        for(int k = i + 1; k <= n; k ++)
            if(a[k] > a[i]) y ++;
        ans += min(x,y);
    }
    cout << ans << endl;
}
        
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}


