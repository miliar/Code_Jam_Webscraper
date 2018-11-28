#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

char ans[99999];
int n, r, p, s;
int good;
int N, R, P, S;

void brute(int lvl, int idx, char c) {
    if (lvl == n) {
        if (c == 'R') --r;
        if (c == 'P') --p;
        if (c == 'S') --s;
        ans[idx] = c;
        return;
    }
    if (c == 'S') {
        brute(lvl + 1, idx * 2, 'S');
        brute(lvl + 1, idx * 2 + 1, 'P');
    }
    if (c == 'P') {
        brute(lvl + 1, idx * 2, 'P');
        brute(lvl + 1, idx * 2 + 1, 'R');
    }
    if (c == 'R') {
        brute(lvl + 1, idx * 2, 'R');
        brute(lvl + 1, idx * 2 + 1, 'S');
    }
}

void prepare(int lvl) {
    for (int h = 0; h < lvl; ++h) {
        for (int i = 0; i < (1 << lvl); i += (1 << (h + 1))) {
            if (strcmp(ans + i, ans + i + (1 << h)) > 0) {
                for (int j = 0; j < (1 << h); ++j)
                    swap(ans[i + j], ans[i + j + (1 << h)]);
            }
        }
    }
}

int main()
{
    ///freopen("A-large.in", "r", stdin);
    ///freopen("A-large.out", "w", stdout);

    int t = 0;
    cin >> t;
    for (int ttt = 1; ttt <= t; ++ttt) {
        cin >> n >> r >> p >> s;
        N = n; P = p; R = r; S = s;
        for (int i = 0; i < 17000; ++i) ans[i] = 0;

        n = N; p = P; r = R; s = S;
        good = 1; brute(0, 0, 'R');
        if (good && p == 0 && r == 0 && s == 0) { prepare(n); ans[1 << n] = 0;
            cout << "Case #" << ttt << ": " << ans << "\n"; continue; }

        n = N; p = P; r = R; s = S;
        good = 1; brute(0, 0, 'P');
        if (good && p == 0 && r == 0 && s == 0) { prepare(n); ans[1 << n] = 0;
            cout << "Case #" << ttt << ": " << ans << "\n"; continue; }

        n = N; p = P; r = R; s = S;
        good = 1; brute(0, 0, 'S');
        if (good && p == 0 && r == 0 && s == 0) { prepare(n); ans[1 << n] = 0;
            cout << "Case #" << ttt << ": " << ans << "\n"; continue; }

        cout << "Case #" << ttt << ": IMPOSSIBLE\n";
    }

    return 0;
}
