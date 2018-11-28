#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("quala.txt", "r", stdin);
    freopen("qualao.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string tt;
        cin >> tt;
        tt += '+';
        int ans = 0;
        for (int i = tt.size() - 2; i >= 0; i--)
        {
            if (tt[i] != tt[i + 1])
            {
                ans++;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
