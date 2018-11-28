#include <cstdio>
#include <vector>

int main(int argc, char *argv[]) {
    int T;
    std::scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int K, C, S;
        std::scanf("%d %d %d", &K, &C, &S);

        int minS = 0, kk = K;
        while (kk > 0) {
            kk -= C;
            minS++;
        }

        if (S < minS) {
            std::printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }

        std::vector<long int> positions;

        if (C >= K) {
            long int pos = 0;
            for (int i = 0; i < K; i++) {
                pos *= K;
                pos += i;
            }
            positions.push_back(pos);
        } else {
            for (int i = 0; i < K; i += C) {
                long int pos = i;
                long int start = i + 1;
                long int end = i + C;

                if (end >= K) {
                    end = K;
                    start = K - C + 1;
                }

                while (start < end) {
                    pos *= K;
                    pos += start;
                    start += 1;
                }
                positions.push_back(pos);
            }
        }

        std::printf("Case #%d: ", t);
        for (int p = 0; p < positions.size(); p++) {
            std::printf("%ld ", positions[p] + 1);
        }
        std::printf("\n");
    }

    return 0;
}