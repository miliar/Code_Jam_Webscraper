#include <iostream>
#include <cstdint>

using namespace std;

void solve(int N, int *m, uint64_t &x, uint64_t &y) {
    int biggest_diff = 0;
    x = y = 0;
    for (int n = 1; n < N; n++) {
        int diff = m[n - 1] - m[n];
        biggest_diff = max(biggest_diff, diff);
        if (diff > 0) x += diff;
    }
    for (int n = 0; n < N - 1; n++) {
        y += min(biggest_diff, m[n]);
    }
}

int main(int argc, char *argv[])
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        int N;
        cin >> N;
        int m[1001];
        for (int n = 0; n < N; n++) {
            cin >> m[n];
        }
        uint64_t x, y;
        solve(N, m, x, y);
        cout << "Case #" << t << ": " << x << " " << y << endl;
    } /* 't' for loop */

    return 0;
}
