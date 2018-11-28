#include <cstdio>
#include <vector>

int main(int argc, char *argv[]) {
    int T;
    std::scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int N;
        std::scanf("%d", &N);

        if (N == 0) {
            std::printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        std::vector<int> digits;
        for (int i = 0; i < 10; i++) {
            digits.push_back(0);
        }

        int nn = N;
        while (true) {
            int m = nn;
            while (m > 0) {
                digits[m % 10] = 1;
                m -= m % 10;
                m /= 10;
            }

            int sum = 0;
            for (int i = 0; i < 10; i++) {
                sum += digits[i];
            }

            if (sum < 10) {
                nn += N;
            } else {
                break;
            }
        }

        std::printf("Case #%d: %d\n", t, nn);
    }

    return 0;
}