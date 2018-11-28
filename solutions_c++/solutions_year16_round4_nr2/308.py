#include <bits/stdc++.h>
using namespace std;

const int N = 200;
double f[N + 1][N / 2 + 1];
int mark[N + 1][N / 2 + 1];
double p[N];
double a[N];
int run;

double F(int n, int agree) {
    if (agree < 0) return 0;
    if (n < agree) return 0;
    if (n == 0) return 1;
    double &res = f[n][agree];
    if (mark[n][agree] == run) return res;
    mark[n][agree] = run;
    res = a[n - 1] * F(n - 1, agree - 1) + (1 - a[n - 1]) * F(n - 1, agree);
    return res;
}
 
double runTest() {
    int n; cin >> n;
    int k; cin >> k;
    for (int i = 0; i < n; ++i) cin >> p[i];
    sort(p, p + n);
    double res = 0;
    for (int i = 0; i <= k; ++i) {
        int ptr = 0;
        for (int j = 0; j < i; ++j) a[ptr++] = p[j];
        for (int j = 0; j < k - i; ++j) a[ptr++] = p[n - j - 1];
        ++run;
        res = max(res, F(ptr, ptr / 2));
    }
    /*int bestmask = 0;
    for (int mask = 0; mask < 1 << n; ++mask) if (__builtin_popcount(mask) == k) {
        int ptr = 0;
        for (int i = 0; i < n; ++i) if ((mask & 1 << i) != 0) a[ptr++] = p[i];
        ++run;
        if (F(ptr, ptr / 2) >= res) res = F(ptr, ptr / 2), bestmask = mask;
        //res = max(res, F(ptr, ptr / 2));
    }
    cerr << bitset<16>(bestmask) << endl;*/
    return res;
}

int main() {
    cout.precision(12);
    int nt; cin >> nt;
    for (int tc = 1; tc <= nt; ++tc)
        cout << "Case #" << tc << ": " << fixed << runTest() << endl;
    return 0;
}
