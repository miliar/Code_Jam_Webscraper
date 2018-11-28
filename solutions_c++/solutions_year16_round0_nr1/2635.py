#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    if(n == 0)
    {
        cout << "INSOMNIA\n";
        return;
    }
    int i;
    int ok[10];
    memset(ok, 0, sizeof(ok));
    for(i = n; ; i += n)
    {
        int j = i;
        while(j)
        {
            ok[j % 10] = 1;
            j /= 10;
        }
        if(accumulate(ok, ok + 10, 0) == 10)
            break;
    }
    cout << i << "\n";
    return;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
