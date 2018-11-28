#include <iostream>

using namespace std;

int main()
{
    int ttt;
    cin >> ttt;
    for (int tti = 1; tti <= ttt; tti++)
    {
        int n, cnt = 0, ans = 0;
        char s[1007];
        cin >> n >> s;
        for (int i = 0; i <= n; i++)
        {
            int x = s[i] - 48;
            if (cnt < i)
            {
                ans += i - cnt;
                cnt = i;
            }
            cnt += x;
        }
        cout << "Case #" << tti << ": " << ans << endl;
    }
    return 0;
}
