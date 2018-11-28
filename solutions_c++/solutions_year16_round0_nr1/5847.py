#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

inline uint16_t get_mask(uint64_t num) {
        uint16_t mask {0};
        while (num > 0/* && mask != target */) {
                mask |= (1 << (num % 10));
                num /= 10;
        }
        return mask;
}

inline uint64_t get_result(uint64_t num) {
        const uint16_t target {0b0000001111111111};
        uint64_t current {num};
        uint16_t mask {get_mask(current)};
        while (mask != target) {
                current += num;
                mask |= get_mask(current);
        }
        return current;
}

vector<uint64_t> precompute() {
        const size_t data_size {1000000};
        vector<uint64_t> res(data_size + 1);
        for (size_t i {1}; i <= data_size; ++i) {
                res[i] = get_result(i);
        }
        return res;
}

int main() {
        vector<uint64_t> res {precompute()};
        size_t T;
        cin >> T;
        for (size_t i {1}; i <= T; ++i) {
                cout << "Case #" << i << ": ";
                int N;
                cin >> N;
                if (N == 0) {
                        cout << "INSOMNIA\n";
                        continue;
                }
                cout << res[N] << '\n';
        }
        return 0;
}