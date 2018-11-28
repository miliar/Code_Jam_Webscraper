#include <cstdio>
#include <vector>

using namespace std;

inline int min(int a, int b) {
    return a < b ? a : b;
}

int f(int largest, vector<int> pancakes) {
    while (!pancakes[largest]) {
        --largest;
    }
    if (largest <= 1) {
        return 1;
    }

    // split into 2's
    vector<int> pancakes2 = pancakes;
    pancakes2[largest / 2] += pancakes2[largest];
    pancakes2[largest - (largest / 2)] += pancakes2[largest];

    int best = min(largest, pancakes[largest] + f(largest - 1, pancakes2));

    if (largest == 9) {
        pancakes[3] += pancakes[9] * 3;
        best = min(best, pancakes[9] * 2 + f(largest - 1, pancakes));
    }
    return best;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        vector<int> pancakes(15);
        int d;
        scanf("%d", &d);
        int p;
        for (int i = 0; i < d; ++i) {
            scanf("%d", &p);
            ++pancakes[p];
        }

        printf("Case #%d: %d\n", t, f(10, pancakes));
    }
}