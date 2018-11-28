#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>
#include <iomanip>

using namespace std;

struct Quaternion
{
    char c;
    bool minus;
    Quaternion(char _c = '1', bool _minus = false) { c = _c; minus = _minus; }
};

Quaternion operator* (const Quaternion& a, const Quaternion& b)
{
    bool minus = a.minus != b.minus;
    if (a.c == '1')
    {
        return Quaternion(b.c,  minus);
    }
    else if (a.c == 'i')
    {
        if (b.c == '1') return Quaternion(a.c, minus);
        if (b.c == 'i') return Quaternion('1', !minus);
        if (b.c == 'j') return Quaternion('k', minus);
        return Quaternion('j', !minus);
    }
    else if (a.c == 'j')
    {
        if (b.c == '1') return Quaternion(a.c, minus);
        if (b.c == 'i') return Quaternion('k', !minus);
        if (b.c == 'j') return Quaternion('1', !minus);
        return Quaternion('i', minus);
    }
    else
    {
        if (b.c == '1') return Quaternion(a.c, minus);
        if (b.c == 'i') return Quaternion('j', minus);
        if (b.c == 'j') return Quaternion('i', !minus);
        return Quaternion('1', !minus);
    }

}

string solution()
{
    int l, x;
    cin >> l >> x;

    string t;
    cin >> t;

    //x = min(x, 20);
    string s;
    for (int i = 0; i < x; ++i)
        s += t;

    int n = s.length();

    Quaternion prefix;
    for (int i = 1; i <= n - 2; ++i)
    {
        prefix = prefix * Quaternion(s[i - 1], false);
        if (!(prefix.c == 'i' && prefix.minus == false))
            continue;

        Quaternion middle;
        Quaternion last;
        for (int j = 0; i + j < n; ++j)
            last = last * Quaternion(s[i + j], false);


        for (int j = 1; i + j <= n - 1; ++j)
        {
            middle = middle * Quaternion(s[i + j - 1], false);
            last = Quaternion(s[i + j - 1], true) * last;

            if (middle.c == 'j' && middle.minus == false &&
                last.c == 'k' && last.minus == false)
            {
                return "YES";
            }
        }
    }

    return "NO";
}


int main(int argc, char* argv[])
{
    ios::sync_with_stdio(false);

    int testsNumber;
    cin >> testsNumber;

    for (int testIndex = 0; testIndex < testsNumber; ++testIndex)
    {
        cout << "Case #" << testIndex + 1 << ": ";

        cout << solution();

        cout << endl;
    }

    cerr << fixed << setprecision(4) << clock() * 1.0 / CLOCKS_PER_SEC << endl;
    return 0;
}