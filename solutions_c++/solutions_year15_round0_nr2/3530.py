#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int a[2000], bans = 2000;

int tr(int big, multiset<int> s)
{
    int t = 0;
    while (*prev(s.end()) > big)
    {
        auto ma = *prev(s.end());
        s.erase(prev(s.end()));
        s.insert(big);
        s.insert(ma - big);
        t++;
        if (t > bans)
            return t;
    }
//    if (*prev(s.end()) > big)
//        return t + *prev(s.end()) - big;
    return t;
}

multiset<int> s;

int proceed()
{
    bans = 2000;
    s.clear();
    int am;
    cin >> am;
    for (int i = 0; i < am; ++i)
        (cin >> a[i]), s.insert(a[i]);
//    if (am == 1)
//        return a[0];
    for (int lam = *prev(s.end()); lam > 0; --lam)
        bans = min(tr(lam, s) + lam, bans);
    return bans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
        cout << "\nCase #" << i + 1 << ": " << proceed();
    return 0;
}
