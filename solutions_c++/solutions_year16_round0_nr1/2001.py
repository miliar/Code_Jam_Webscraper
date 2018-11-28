#include <iostream>
#include <algorithm>
#include <vector>
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

        vector<bool> seen(10, false);
        int count = 0;
        for (int i = N ;; i += N) {
            for (int n = i; n != 0; n /= 10) {
                if (!seen[n % 10])
                    count++;
                seen[n % 10] = true;
                if (count == 10) {
                    printf("Case #%d: %d\n", t, i);
                    goto next_case;
                }
            }
        }

        next_case:
        ;
    }

    return 0;
}
