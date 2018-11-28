#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>
using namespace std;
bool check(string const& s)
{
    for (int i = 0; i < s.size(); ++i)
    {
        if (s[i] != '+')
            return false;
    }
    return true;
}
void revert(string &s, int last)
{
    for(int i = 0; i <= last; ++i)
    {
        if (s[i] == '-')
        {
            s[i] = '+';
        }
        else
        {
            s[i] = '-';
        }
    }
}

int res_count(string s)
{
    int i = 0;
    for (; !check(s); ++i)
    {
        int last = 0;
        for (; last + 1 < s.size(); ++last)
        {
            if (s[last] != s[last + 1])
            {
                break;
            }
        }

        revert(s, last);
    }

    return i;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        string s;
        cin >> s;
        cout << "Case #" << + i + 1 << ": " << res_count(s) << endl;
    }
    return 0;
}