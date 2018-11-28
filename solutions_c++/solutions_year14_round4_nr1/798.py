#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int a[100010];
int n, x;

bool can(int cnt)
{
    if(cnt >= n)
        return 1;
    int p = 0;
    for(int i = n-1 ; i >= p ; --i)
    {
        if(a[p] + a[i] <= x)
            ++p;
        
        cnt--;
    }
    return cnt >= 0;
}

int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt", "w", stdout);
    ios::sync_with_stdio();
    int t;
    cin >> t;
    for(int tt = 1 ; tt <= t ; ++tt)
    {
        cin >> n >> x;
        for(int i = 0 ; i < n ; ++i)
            cin >> a[i];
        sort(a, a+n);
        
        int ans = 0;
        for(int i = 20 ; i >= 0 ; --i)
        if(!can(ans+(1<<i)))
            ans += (1<<i);
        ++ans;
        cout << "Case #" << tt << ": " << ans << "\n";
    }
    return 0;
}