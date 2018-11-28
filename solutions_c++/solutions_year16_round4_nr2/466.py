#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000;

long double a[maxn];

void solve() {
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n);
    long double ans = 0;
    for (int i = 0; i <= k; i++) {
        long double b[k];
        for (int j = 0; j < i; j++) {
            b[j] = a[j];
        }
        for (int l = 0; l < (k - i); l++)
            b[i + l] = a[n - l - 1];
        long double f[k + 2][k + 2];
        for (int q = 0; q <= k; q++)
            for (int w = 0; w <= k; w++) {
                f[q][w] = 0;
            }
        f[0][0] = 1.;
        for (int w = 0; w < k; w++){
            for (int j = 0; j <= w; j++) {
                f[w + 1][j + 1] += f[w][j] * b[w];
                f[w + 1][j] += f[w][j] * (1 - b[w]);
            }
        }
        ans = max(ans, f[k][k / 2]);
    }
    for (int i = 0; i < n; i++) {
        if (i + k > n) {
            break;
        }
        long double b[k];
        for (int j = 0; j < k; j++) {
            b[j] = a[i + j];
        }
        long double f[k + 2][k + 2];
        for (int q = 0; q <= k; q++)
            for (int w = 0; w <= k; w++) {
                f[q][w] = 0;
            }
        f[0][0] = 1.;
        for (int w = 0; w < k; w++){
            for (int j = 0; j <= w; j++) {
                f[w + 1][j + 1] += f[w][j] * b[w];
                f[w + 1][j] += f[w][j] * (1 - b[w]);
            }
        }
        ans = max(ans, f[k][k / 2]);
    }
    cout.precision(20);
    cout << (double)ans << endl;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test;
    cin >> test;
    for (int id = 1; id <= test; id++) {
        cout << "Case #" << id << ": ";
        solve();
    }
    return 0;
}