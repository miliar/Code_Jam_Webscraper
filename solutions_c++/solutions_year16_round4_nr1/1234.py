#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size
#define mp make_pair
#define pb push_back

using namespace std;

void solve(int l, int r, char c, vector<char>& v)
{
    if (l == r) {
        v[0] = c;
        return;
    }
    int m = (l + r) >> 1;
    int n = (r - l + 1) >> 1;
    vector<char> x(n), y(n);
    if (c == 'S') {
        solve(l, m, 'P', x);
        solve(m + 1, r, 'S', y);
    } else if (c == 'R') {
        solve(l, m, 'R', x);
        solve(m + 1, r, 'S', y);
    } else {
        solve(l, m, 'P', x);
        solve(m + 1, r, 'R', y);
    }
    if (x > y) {
        swap(x, y);
    }
    for (int i = 0; i < 2 * n; ++i) {
        if (i < n) {
            v[i] = x[i];
        } else {
            v[i] = y[i - n];
        }
    }
}

int main()
{

    ifstream cin("input");
    ofstream cout("output");

    int tt;
    cin >> tt;
    for (int c = 1; c <= tt; ++c) {
        int n;
        cin >> n;
        vector<char> v(1 << n);

        vector<vector <char> > a(3);

        solve(0, (1 << n) - 1, 'P', v);
        a[0] = v;

        solve(0, (1 << n) - 1, 'R', v);
        a[1] = v;

        solve(0, (1 << n) - 1, 'S', v);
        a[2] = v;

        int r, s, p;
        cin >> r >> p >> s;

        vector<char> ans(1 << n, '?');
        for (int i = 0; i < 3; ++i) {
            int rr = 0, ss = 0, pp = 0;
            for (int j = 0; j < (1 << n); ++j) {
                if (a[i][j] == 'S') {
                    ++ss;
                } else if (a[i][j] == 'P') {
                    ++pp;
                } else {
                    ++rr;
                }
            }
            if (rr != r || ss != s || pp != p) {
                continue;
            }
            for (int j = 0; j < (1 << n); ++j) {
                if (ans[j] == '?' || ans[j] > a[i][j]) {
                    ans = a[i];
                    break;
                } else if (ans[j] < a[i][j]) {
                    break;
                }
            }
        }

        cout << "Case #" << c << ": ";
        if (ans[0] == '?') {
            cout << "IMPOSSIBLE";
        } else {
            for (int j = 0; j < (1 << n); ++j) {
                cout << ans[j];
            }
        }
        cout << "\n";
    }

}
