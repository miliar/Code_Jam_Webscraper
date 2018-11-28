#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    freopen("a.out", "w", stdout);
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test)
    {
        string s;
        cin >> s;
        while (!s.empty() && s.back() == '+')
            s.pop_back();
        for (int i = 0; i < 200; ++i)
        {
            int sum = 0;
            for (auto x : s)
                if (x == '+')
                    ++sum;
                else
                    break;
            if (sum == s.length())
            {
                printf("Case #%d: %d\n", test + 1, i);
                break;
            }
            if (s[0] != '-')
            {
                for (auto &x : s)
                    if (x == '+')
                        x = '-';
                    else
                        break;
            }
            else
            {
                for (auto &x : s)
                    if (x == '+')
                        x = '-';
                    else
                        x = '+';
                reverse(s.begin(), s.end());
                while (!s.empty() && s.back() == '+')
                    s.pop_back();
            }
        }
    }

    return 0;
}
