#include <bits/stdc++.h>

using namespace std;

void solution();

int main()
{
    ios_base::sync_with_stdio(false);
#ifdef HOME
    freopen("B.in", "rt", stdin);
    clock_t start = clock();
#endif
    solution();
#ifdef HOME
    cerr.precision(3);
    cerr << endl << "Total time: " << fixed << double(clock() - start) / double(CLOCKS_PER_SEC) << endl;
#endif
    return 0;
}

typedef long long ll;
#define int ll

void inverse(string& s, int r)
{
    reverse(s.begin(), s.begin() + r);
    for (int i = 0; i < r; ++i)
    {
        if (s[i] == '+')
            s[i] = '-';
        else if (s[i] == '-')
            s[i] = '+';
    }
}

string s;

bool is_right(const string& s)
{
    int n = s.size();
    for (int i = 0; i < n; ++i)
        if (s[i] != '+')
            return false;
    return true;
}

void solve()
{
    int n = s.size();
    int res = 0;
    for (int i = n - 1; i >= 0; --i)
    {
        if (s[i] == '-')
        {
            if (s[0] != '-')
            {
                int j = 0;
                while (j < n && s[j] == '+')
                    ++j;
                if (j > 0)
                {
                    inverse(s, j);
                    ++res;
                }
                if (j == n)
                    break;
            }
            inverse(s, i + 1);
            ++res;
        }
    }
    assert(is_right(s));
    cout << res;
}

void solution()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        cin >> s;
        cout << "Case #" << t + 1 << ": ";
        solve();
        cout << '\n';
    }
}
