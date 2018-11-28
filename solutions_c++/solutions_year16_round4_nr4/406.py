#include <bits/stdc++.h>

using namespace std;

template<class T>
using v = vector<T>;

bool check(v<string> &p)
{
//    for (int i = 0; i < p.size(); ++i)
//    {
//        for (int j = 0; j < p.size(); ++j)
//            cerr << (bool)p[i][j];
//        cerr << endl;
//    }
//    cerr << endl;
    for (int i = 0; i < p.size(); ++i)
    {
        set<int> states;
        states.insert(0);
        for (int j = 0; j < p.size(); ++j)
        {
            if (i == j) continue;
            set<int> ns;
            for (auto x: states)
            {
                for (int z = 0; z < p.size(); ++z)
                {
                    if (p[j][z])
                        ns.insert(x | (1 << z));
                }
            }
            for (auto x: ns)
                states.insert(x);
        }
        for (auto x: states)
        {
            bool ok = false;
            for (int j = 0; j < p.size(); ++j)
            {
                if (p[i][j] && (x & (1 << j)) == 0)
                    ok = true;
            }
            if (!ok) return false;
        }
    }
    return true;
}

void stupid()
{
    int n;
    cin >> n;
    v<string> p(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> p[i];
        for (int j = 0; j < n; ++j)
            p[i][j] -= '0';
    }
    int ans = 1000;

    function<void(int, int, int)> tr = [&](int i, int j, int c)
    {
//        cerr << i << " " << j << " " << n << endl;
        if (check(p))
        {
            ans = min(ans, c);
            return;
        }
        if (j < n - 1)
            tr(i, j + 1, c);
        if (j == n - 1 && i < n - 1)
            tr(i + 1, 0, c);
        if (p[i][j]) return;
        p[i][j] = true;
        tr(i, j, c + 1);
        p[i][j] = false;
    };
    tr(0, 0, 0);
    cout << ans;
}


void solve()
{

}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        stupid();
        cout << endl;
    }
}