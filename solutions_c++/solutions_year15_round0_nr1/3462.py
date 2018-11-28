#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int solve(const string &s)
{
    int up = 0;
    int ans = 0;
    for (int i = 0; i < s.size(); ++i)
    {
        if (up < i)
        {
            int diff = i - up;
            ans += diff;
            up += diff;
        }

        up += s[i] - '0';
    }
    return ans;
}

int main(int argc, char* argv[])
{
    ios_base::sync_with_stdio(false);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int test = 0; test < T; ++test)
    {
        int s_max;
        cin >> s_max;

        string s;
        s.reserve(s_max + 5);

        cin >> s;

        cout << "Case #" << test + 1 << ": " << solve(s) << "\n";
    }

	return 0;
}

