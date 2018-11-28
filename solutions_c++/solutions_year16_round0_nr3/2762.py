#include <bits/stdc++.h>

using namespace std;

int cnt;

inline long long prime(long long x)
{
    for (long long i = 2; i * i <= x; i++)
    {
        if (x % i == 0)
        {
            return i;
        }
    }
    return -1;
}

void gen(string s, int len)
{
    if ((int)s.size() + 1 == len)
    {
        s += '1';
        long long t = 0;
        bool ok = true;
        vector<long long> cr;
        for (int i = 2; i <= 10; i++)
        {
            long long cnum = 0;
            long long cpow = 1;
            for (int j = len - 1; j >= 0; j--)
            {
                cnum += cpow * (s[j] == '1');
                cpow *= i;
            }
            long long cdiv = prime(cnum);
            if (cdiv == -1)
            {
                ok = false;
                break;
            }
            cr.push_back(cdiv);
        }
        if (ok)
        {
            cout << s << " ";
            for (int dv : cr)
            {
                cout << dv << " ";
            }
            cout << '\n';
            cnt--;
        }
        if (cnt == 0)
        {
            exit(0);
        }
        return;
    }
    if ((int)s.size() == 0)
    {
        s += '1';
        gen(s, len);
    }
    else
    {
        string t = s;
        t += '1';
        gen(t, len);
        t = s;
        t += '0';
        gen(t, len);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("out.txt", "w", stdout);
    cout << "Case #1:\n";
    cnt = 50;
    gen("", 16);
}
