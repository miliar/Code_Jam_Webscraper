#include <bits/stdc++.h>

using namespace std;

template<class T>
using v = vector<T>;

void solve()
{
    int n, r, p, s;
    v<int> d(3);
    cin >> n >> d[0] >> d[1] >> d[2];
    v<int> c(3, 0);
    string cans;
    string dsp = "RPS";
    function<string (int, int)> tr = [&](int t, int step)
    {
        if (step == 0)
        {
            c[t]++;
            return string(1, dsp[t]);
        }
        string s1 = tr(t, step - 1);
        string s2;
        if (t == 0)
            s2 = tr(2, step - 1);
        if (t == 1)
            s2 = tr(0, step - 1);
        if (t == 2)
            s2 = tr(1, step - 1);
        if (s1 < s2)
            return s1 + s2;
        else
            return s2 + s1;
    };

    vector<string> pans;
    for (int i = 0; i < 3; ++i)
    {
        c = v<int>(3, 0);
        string tmp = tr(i, n);
        if (c == d)
        {
            pans.push_back(tmp);
        }
    }
    sort(pans.begin(), pans.end());
    if (pans.empty())
        cout << "IMPOSSIBLE";
    else
        cout << pans[0];
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}