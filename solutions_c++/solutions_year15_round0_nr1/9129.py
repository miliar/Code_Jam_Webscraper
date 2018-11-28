#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int tt = 1; tt <= T; tt++)
    {
        cout << "Case #" << tt << ": ";


        int ans = 0;
        int now = 0;
        int S;
        cin  >> S;
        for(int i = 0; i <= S; i++)
        {
            char c;
            cin >> c;

            if(c > '0')
                ans += max(0, i - now - ans);
            now += c - '0';
        }
        cout << ans << '\n';
    }
}

