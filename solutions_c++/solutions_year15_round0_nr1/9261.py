#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    int T_lim; cin >> T_lim;

    for (int T = 0; T < T_lim; T++)
    {
        int k_lim; cin >> k_lim;
        string s;  cin >> s;

        int sum = 0;
        int ans = 0;

        for (int k = 0; k <= k_lim; k++)
        {
            ans = max(ans, k-sum);
            sum += s[k]-'0';
        }

        cout << "Case #" << T+1 << ": " << ans << "\n";
    }

    return 0;
}
