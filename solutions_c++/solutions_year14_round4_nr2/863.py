
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#define MAXN 1001
#define INF (1 << 30)

using namespace std;

int N;
int a[MAXN];

bool used[MAXN];
int cnt[MAXN][MAXN];

/*
pair <int, int> b[MAXN];

int solve_brute(bool print, int total_max) {
    int best = N * N;
    for (int mask = 0; mask < (1 << N); mask++) {
        int i = 0, j = N - 1;
        for (int k = 0; k < N; k++) {
            if (mask & (1 << k))
                b[i++] = make_pair(a[k], k);
            else
                b[j--] = make_pair(a[k], k);
        }
        sort(b, b + i);
        sort(b + i, b + N);
        reverse(b + i, b + N);

        int total = 0;
        for (i = 0; i < N; i++)
            for (j = 0; j < i; j++)
                if (b[i].second < b[j].second)
                    total++;
        if (print && total_max == total) {
            for (i = 0; i < N; i++)
                cerr << a[i] << " ";
            cerr << endl;
            for (i = 0; i < N; i++)
                cerr << b[i].first << " ";
            cerr << endl;
            return total_max;
        }
        best = min(best, total);
    }
    return best;
}
*/

void solve() {
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> a[i];

    for (int i = 0; i < N; i++)
        used[i] = false;

    for (int i = 0; i <= N; i++)
        for (int j = 0; j <= N; j++)
            cnt[i][j] = INF;
    cnt[0][0] = 0;

    for (int k = 1; k <= N; k++) {
        int cur = 0, pos = 0;
        int a_min = INF, i_min = 0;
        for (int i = 0; i < N; i++) {
            if (used[i])
                continue;
            if (a[i] < a_min) {
                a_min = a[i];
                i_min = i;
                cur = pos;
            }
            pos++;
        }
        used[i_min] = true;
        /*
        if (pos != N - k) {
            cerr << pos << " " << N - k << endl;
            assert(pos == N - k + 1);
        }
        */

        for (int i = 0; i <= k; i++) {
            int j = k - i;
            if (i > 0) {
                cnt[i][j] = min(cnt[i][j], cnt[i - 1][j] + cur);
            }
            if (j > 0) {
                cnt[i][j] = min(cnt[i][j], cnt[i][j - 1] + N - k - cur);
            }
        }
    }
    
    int cnt_best = INF;
    for (int i = 0; i <= N; i++)
        cnt_best = min(cnt_best, cnt[i][N - i]);
    cout << cnt_best << endl;

    /*
    int cnt2 = solve_brute(false, 0);
    if (cnt_best != cnt2) {
        cerr << "NOT EQUAL: " << cnt_best << " " << cnt2 << endl;
        solve_brute(true, cnt2);
    }
    */
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
}

