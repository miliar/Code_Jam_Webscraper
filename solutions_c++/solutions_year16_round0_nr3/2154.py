#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>
using namespace std;

bool check(string const& s)
{
    return s[0] == s.back() && s.back() == '1';
}

int get_div(string const& s, int base)
{
    for (int i = 2; i < 30000; ++i)
    {
        int cur = 0;
        string st = s;
        reverse(st.begin(), st.end());
        while(st.size())
        {
            cur = cur * base + st.back() - '0';
            st.pop_back();
            cur = cur % i;
        }
        if (cur == 0)
        {
            return i;
        }
    }
    return 1;
}

bool check_cj(string const& s)
{
    bool checks = true;
    vector<int> divisor;

    for (int i = 2; checks && i <= 10; ++i)
    {
        int div = get_div(s, i);
        if (div != 1)
        {
            divisor.push_back(div);
        }
        else
        {
            checks = false;
        }
    }
    if (checks)
    {
        cout << s << " ";
        for (int i = 0; i < divisor.size(); ++i)
        {
            cout << divisor[i] << " ";
        }
        cout << endl;
        return true;
    }
    return false;
}

void next_s(string& s)
{
    int c = 1;
    for (int i = s.size() - 2; i > 0 && c; --i)
    {
        s[i] = s[i] + c;
        if (s[i] == '2')
        {
            s[i] = '0';
            c = 1;
        }
        else
        {
            c = 0;
        }
    }
}

void res_count(int n, int j)
{
    string s("11");
    s.insert(1, string(n - 2, '0'));
    while(j > 0)
    {
        if (check_cj(s))
        {
            --j;
        };
        next_s(s);
    }
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n, j;
        cin >> n >> j;
        cout << "Case #" << + i + 1 << ":\n";
        res_count(n, j);
    }
    return 0;
}