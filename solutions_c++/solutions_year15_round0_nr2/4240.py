#include <bits/stdc++.h>
using namespace std;

int solve()
{
    int a[1010];
    int n;
    scanf("%d",&n);
    int ans = 0;
    for(int i = 1; i <= n; i ++) {
        scanf("%d",&a[i]);
        ans = max(ans,a[i]);
    }
    for(int i = 1; i <= ans; i ++) {
        int sum = 0;
        for(int j = 1; j <= n; j ++) 
            if(a[j] > i) sum += (a[j] + i - 1) / i - 1;
        ans = min(ans,sum + i);
        //cout << sum << " " << i << endl;
    }
    return ans;
}
    
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        int ans = solve();
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
