#include <array>
#include <cstdint>
#include <iostream>

using namespace std;

constexpr int N {16};
constexpr int J {50};

uint64_t is_prime(const uint64_t k) {
        if (k % 2 == 0) return 2;
        for (uint64_t t {3}; t * t <= k; t += 2) {
                if (k % t == 0)
                        return t;
        }
        return 0;
}

int main() {
        array<int, N> num;
        num[0] = num[N - 1] = 1;
        cout << "Case #1:\n";
        int cnt {0};
        for (uint32_t t {0}; cnt < J; ++t) {
                uint32_t tmp {t};
                for (size_t i {1}; i <= N - 2; ++i) {
                        num[i] = (tmp & 1);
                        tmp = tmp >> 1;
                }
                array<uint64_t, 9> divisor;
                bool flag {true};
                for (int base {2}; base <= 10; ++base) {
                        uint64_t k {0};
                        for (size_t i {0}; i < N; ++i) {
                                k = k * base + num[i];
                        }
                        divisor[base - 2] = is_prime(k);
                        if (divisor[base - 2] == 0) {
                                flag = false;
                                break;
                        }
                }
                if (flag) {
                        for (size_t i {0}; i < N; ++i) cout << num[i];
                        for (size_t i {0}; i < 9; ++i) cout << ' ' << divisor[i];
                        cout << '\n';
                        ++cnt;
                }
        }
        return 0;
}