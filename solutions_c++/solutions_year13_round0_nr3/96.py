#include <algorithm>
#include <iostream>
#include <string.h>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstdlib>
#include <complex>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pii pair<int, int>
#define pll pair<long long, long long>
#define F first
#define S second
#define MP make_pair
#define bi big_int

struct big_int
{
    string val;

    big_int() {}

    big_int(string c)
    {
        val = c;
    }

    void read()
    {
        cin >> val;
        reverse(val.begin(), val.end());
    }

    big_int operator * (big_int b)
    {
        string c;
        for (int i = 0; i < val.length() + b.val.length() + 2; ++i)
            c += '0';
        for (int i = 0; i < val.length(); ++i)
        {
            int carry = 0;
            for (int j = 0; j < b.val.length() || carry; ++j)
            {
                int aa = val[i] - '0';
                int bb = (j < b.val.length() ? b.val[j] - '0' : 0);
                int cc = c[i + j] - '0';
                int cur = aa * bb + carry + cc;
                c[i + j] = char(cur % 10 + '0');
                carry = cur / 10;
            }
        }
        while (c.length() > 1 && c[c.length() - 1] == '0')
            c.erase(c.length() - 1, 1);
        return big_int(c);
    }

    bool is_poly()
    {
        string rval = val;
        reverse(rval.begin(), rval.end());
        return val == rval;
    }

    void print()
    {
        string rval = val;
        reverse(rval.begin(), rval.end());
        cout << rval << endl;
    }

    bool operator >= (big_int &b)
    {
        while (b.val.length() > 1 && b.val[b.val.length() - 1] == '0')
            b.val.erase(b.val.length() - 1, 1);
        while (val.length() > 1 && val[val.length() - 1] == '0')
            val.erase(val.length() - 1, 1);
        reverse(val.begin(), val.end());
        reverse(b.val.begin(), b.val.end());
        if (val.length() > b.val.length())
        {
            reverse(val.begin(), val.end());
            reverse(b.val.begin(), b.val.end());
            return true;
        }
        if (val.length() < b.val.length())
        {
            reverse(val.begin(), val.end());
            reverse(b.val.begin(), b.val.end());
            return false;
        }
        bool ret = (val >= b.val);
        reverse(val.begin(), val.end());
        reverse(b.val.begin(), b.val.end());
        return ret;
    }
};

vector<vector<big_int> > p;

void pre()
{
    p.resize(53);
    p[1].push_back(bi("0"));
    p[1].push_back(bi("1"));
    p[1].push_back(bi("2"));
    p[1].push_back(bi("3"));
    p[2].push_back(bi("00"));
    p[2].push_back(bi("11"));
    p[2].push_back(bi("22"));
    for (int i = 3; i <= 51; ++i)
        for (int lo = i - 2; lo > 0; lo -= 2)
            for (int j = 0; j < p[lo].size(); ++j)
            {
                string cur = p[lo][j].val;
                while (cur.length() < i - 2)
                    cur = "0" + cur + "0";
                cur = "1" + cur + "1";
                big_int b(cur);
                big_int a = b * b;
                if (a.is_poly())
                    p[i].push_back(b);
                cur[0] = '2';
                cur[cur.length() - 1] = '2';
                b = big_int(cur);
                a = b * b;
                if (a.is_poly())
                    p[i].push_back(b);
            }
    for (int i = 0; i <= 51; ++i)
        for (int j = 0; j < p[i].size(); ++j)
            p[i][j] = p[i][j] * p[i][j];
}

void solve(int test)
{
    big_int a, b;
    a.read();
    b.read();
    long long ans = 0;
    for (int i = 1; i <= 51; ++i)
        for (int j = 0; j < p[i].size(); ++j)
        {
            big_int cur = p[i][j];
            if (cur >= a && b >= cur)
                ++ans;
        }
    cout << "Case #" << test << ": " << ans << endl;
}


int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    pre();

    int test;
    cin >> test;
    for (int i = 1; i <= test; ++i)
        solve(i);


    return 0;
}
