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

#define N 1000000
int n;
int ans[N + 1];

void precalc()
{
    for (int i = 0; i <= N; ++i)
        ans[i] = -1;
    for (int i = 1; i <= N; ++i)
    {
        set<int> d;
        int k = i;
        while (d.size() != 10)
        {
            int m = k;
            while (m > 0)
            {
                d.insert(m % 10);
                m /= 10;
            }
            k += i;
        }
        ans[i] = k - i;
    }
}

void solve()
{
    assert(n >= 0 && n <= N);
    if (ans[n] == -1)
        cout << "INSOMNIA" << "\n";
    else
        cout << ans[n] << "\n";
}

void solution()
{
    int T;
    cin >> T;
    precalc();
    for (int t = 0; t < T; ++t)
    {
        cin >> n;
        cout << "Case #" << t + 1 << ": ";
        solve();
    }
}
