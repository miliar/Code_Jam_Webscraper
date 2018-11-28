#include <iostream>
using namespace std;
int t;

void solve(int t)
{
    int ans = 0, sm = 0, cnt = 0;
    string s;
    cin >> sm >> s;
    for (int i = 0; i <= sm; ++i)
    {
        if (s[i] != '0')
        {
            if (cnt < i)
            {
                ans += i - cnt;
                cnt += i - cnt;
            }
            cnt += s[i] - '0';
        }
    }
    cout << "Case #" << t << ": " << ans << endl;
}

int main()
{
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}
