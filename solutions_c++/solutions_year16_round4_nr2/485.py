#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

const int N = 201;
ld dp[N][N], in[N], p[N];
bool cal[N][N];
int n, k;
vector <ld> v;

ld solve (int i, int y) {
    if (i == k) return 1.0;
    if (cal[i][y]) return dp[i][y] ;
    int win = y;
    int los = i-y;
    
    ld r = 0.0;
    
    if (win + 1 <= k/2) {
        r = p[i] * solve (i + 1, y + 1);
    } 
    if (los + 1 <= k/2) {
        r += (1 - p[i]) * solve (i + 1, y);
    }
    cal[i][y] = true;
    return dp[i][y] = r;
}

int main (void) {
    int T;
    cin >> T;
    for (int c = 1; c <= T; ++c) {
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> in[i];
        }
        sort (in, in + n);
        ld ans = 0.0;
        for (int s = 0; s < k; ++s) {
            int j = 0;
            for (int i = 0; i < s; ++i) p[j++] = in[i];
            for (int i = n-1; j < k; --i) p[j++] = in[i];
            memset (cal, 0, sizeof cal);
            ans = max (ans, solve (0, 0));
        }
    
        for (int i = 0; i < n; ++i) {
            if (i + k >= n) break;
            for (int j = 0; j < k; ++j) p[j] = in[i+j];
            memset (cal, 0, sizeof cal);
            ans = max (ans, solve (0, 0));
        }

        printf ("Case #%d: %.8Lf\n", c, ans);
    }

    return 0;
}
