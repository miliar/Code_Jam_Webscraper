#include <bits/stdc++.h>

using namespace std;

void solution();

int main()
{
    ios_base::sync_with_stdio(false);
#ifdef HOME
    freopen("A.in", "rt", stdin);
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

string s;

void solve()
{
    int n = s.size();
    reverse(s.begin(), s.end());
    string s1, s2;
    for (int i = 0; i < n; ++i)
    {
        bool exists = false;
        for (int j = i + 1; j < n; ++j)
            if (s[j] > s[i])
                exists = true;
        if (exists)
            s2 += s[i];
        else
            s1 += s[i];
    }
    reverse(s2.begin(), s2.end());
    cout << s1 << s2 << endl;
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
    }
}
