#include <bits/stdc++.h>
#define int long long
using namespace std;
int a[101];
void solve(int t, int x)
{
    cout << "Case #" << t;
    cout << ":";
    for(int i = 0; i <= 9; i ++)
    {
        a[i] = 0;
    }
    for(int i = 1; i <= 1000; i ++)
    {
        int r = i * x;
        while(r > 0)
        {
            a[r % 10] = 1;
            r /= 10;
        }
        int ok = 1;
        for(int j = 0; j <= 9; j ++)
        {
            if(a[j] == 0)
                ok = 0;
        }
        if(ok)
        {
            cout << " " << i * x << endl;
            return ;
        }
    }
    puts(" INSOMNIA");
    return ;
}
main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, x;
    cin >> n;
    for(int i = 1; i <= n; i ++)
    {
        scanf("%I64d", &x);
        solve(i, x);
    }
}
