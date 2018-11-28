#include <cassert>
#include <iostream>
#include <string>
using namespace std;

int solve(int smax, const string& s)
{
    assert(static_cast<unsigned>(smax + 1) == s.size());

    int res = 0;
    int sum = 0;
    for (int i = 0; i <= smax; ++i)
    {
        int d = s[i] - '0';
        if (d > 0 && sum + res < i)
            res += i - (sum + res);
        sum += d;
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    string s;
    for (int i = 1; i <= T; ++i)
    {
        unsigned smax;
        cin >> smax >> s;
        cout << "Case #" << i << ": " << solve(smax, s) << '\n';
    }
    cout.flush();

    return 0;
}
