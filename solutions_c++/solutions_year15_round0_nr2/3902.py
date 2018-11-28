#include <vector>
#include <iostream>
#include <algorithm>

static std::vector<int> primes {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
};

struct State {
    // number of diners with index+1 pancakes
    std::vector<int> data;

    void compress() {
        while (!data.empty()) {
            if (data.back() > 0)
                break;
            data.pop_back();
        }
    }

    size_t eat_pancakes() const {
        State new_state;
        new_state.data.assign(data.begin() + 1, data.end());
        return new_state.solve() + 1;
    }

    size_t divide_pancakes(size_t num_pancakes) const {
        size_t old_index = num_pancakes - 1;
        int diners = data[old_index];
        if (!diners)
            return -1;
        size_t min_ticks = -1;
        for (auto prime : primes) {
            // try to divide pancakes into prime parts
            if (num_pancakes % prime)
                continue;
            State new_state;
            size_t new_index = (num_pancakes / prime) - 1;
            new_state.data.assign(data.begin(), data.end());
            new_state.data[old_index] -= diners;
            new_state.data[new_index] += diners * prime;
            new_state.compress();
            size_t ticks = new_state.solve() + diners * (prime - 1);
            if (min_ticks > ticks)
                min_ticks = ticks;
        }
        return min_ticks;
    }

    size_t solve() const {
        if (data.size() == 1)
            return 1;
        size_t ticks = eat_pancakes();
        size_t div_ticks = divide_pancakes(data.size());
        if (ticks > div_ticks)
            ticks = div_ticks;
        return ticks;
    }
};

int main() {
    int T;
    std::cin >> T;
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        int D;
        std::cin >> D;
        State state;
        state.data.resize(1000);
        for (int i = 0; i < D; ++i) {
            int num_pancakes;
            std::cin >> num_pancakes;
            state.data[num_pancakes - 1] += 1;
        }
        state.compress();
        int total_ticks = state.solve();
        std::cout << "Case #" << caseNum << ": " << total_ticks << std::endl;
    }
}
