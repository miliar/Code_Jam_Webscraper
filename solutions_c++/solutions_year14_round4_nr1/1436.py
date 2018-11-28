#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;


int x[20000];

int main() {
    int T, N, X;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        cin >> N >> X;
        for (int i = 0; i < N; ++i) cin >> x[i];
        sort(x, x + N);
        int ans = 0;
        for (int i = 0, j = N - 1; i <= j; ) {
            if (i == j) {
                ++ans;
                break;
            }
            if (x[i] + x[j] <= X) {
                ++i;
                --j;
            } else {
                --j;
            }
            ++ans;
        }
        cout << "Case #" << times << ": " << ans << endl;
    }
    return 0;
}
