#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int f[2000], f1[2000];
int ans;
int tmp;

int gen(int x)
{
    int ans = 0;
    for(int i = 1000; i > x; i--) if(f[i])
    {
        int p = i / x;
        if(i % x == 0) p--;
        ans += p * f[i];
    }
    return ans;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int d, p;
    int T;
    cin >> T;
    memset(f, 0, sizeof f);
    for(int ii = 1; ii <= T; ii++)
    {
        cin >> d;
        memset(f, 0, sizeof f);
        for(int i = 0; i < d; i++)
        {
            cin >> p;
            f[p]++;
        }
        ans = 2000;
        for(int i = 1; i <= 1000; i++)
            ans = min(ans, i + gen(i));
        cout << "Case #" << ii << ": " << ans << endl;
    }
    return 0;
}
