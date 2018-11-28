#include <iostream>
#include <cstdint>
#include <vector>
#include <algorithm>

std::vector<int64_t> precalc;

int64_t get(int64_t x) {
    if (x < 0)
        return 0;
    auto it = std::lower_bound(precalc.begin(), precalc.end(), x);

    return it - precalc.begin();
}


int64_t calc(int64_t a, int64_t b) {
    return get(2 * b + 1) - get(2 * a - 1);
}

bool is_poly(int64_t x) {
    std::string val = std::to_string(x);

    size_t len = val.size();
    for (size_t i = 0; i < len / 2; i++) {
        if (val[i] != val[len - i - 1])
            return false;
    }
    return true;
}

void prec() {
    precalc.push_back(-1);
    const int64_t maxn = (int64_t)(1e7) + 10LL;
    for (int64_t i = 0; i < maxn; i++) {
        int64_t sq = i * i;
        if (is_poly(i) && is_poly(sq))
            precalc.push_back(2 * sq);
    }
}

int main() {
    prec();
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        int64_t a, b;
        std::cin >> a >> b;
        std::cout << "Case #" << i + 1 << ": " << calc(a, b) << std::endl;
    }

    return 0;
}
