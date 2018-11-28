#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        int v[10] = {0};
        int sum = 55;
        int now = 0;
        while (sum > 0) {
            now += N;
            int tmp = now;
            while (tmp > 0) {
                int r = tmp % 10;
                if (v[r] == 0) {
                    v[r] = 1;
                    sum -= r+1;
                }
                tmp /= 10;
            }
        }
        printf("Case #%d: %d\n", t, now);
    }
    return 0;
}
