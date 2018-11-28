#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define FILE "A-large"

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    int t; cin >> t;
    for(int j = 1; j <= t; ++j)
    {
        int sm; string stt;
        cin >> sm >> stt;
        int s[sm+1];
        for(int i = 0; i < stt.length(); ++i)
            s[i] = stt[i]-'0';
        int ans = 0;
        int up = s[0];
        for(int i = 1; i <= sm; ++i)
        {
            if(up < i && s[i])
            {
                ans += abs(up-i);
                up += abs(up-i);
            }
            up += s[i];
        }
        cout << "Case #" << j << ": " << ans << endl;
    }

    return 0;
}
