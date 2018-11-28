#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

int rec(std::vector<int> counts, int delta_time) {
    int max_i;
    for (int i = counts.size() - 1; i >= 1; --i) {
        if (counts[i] != 0) {
            max_i = i;
            break;
        }
    }

    int best_time = delta_time + max_i;
    int t = counts[max_i];
    counts[max_i] = 0;
    for (int i = 1; i < max_i; ++i) {
        counts[i] += t;
        counts[max_i - i] += t;
        best_time = std::min(best_time, rec(counts, delta_time + t));
        counts[i] -= t;
        counts[max_i - i] -= t;
    }

    return best_time;
}

int solution(std::vector<int>& counts) {
    return rec(counts, 0);
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    std::cin >> t;
    for (size_t i = 0; i < t; ++i) {
        std::vector<int> counts(10);
        int d;
        std::cin >> d;
        int p;
        for (int j = 0; j < d; ++j) {
            std::cin >> p;
            ++counts[p];
        }

        std::cout << "Case #" << i + 1 << ": " << solution(counts) << '\n';
    }
}
