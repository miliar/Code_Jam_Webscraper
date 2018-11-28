#include <iostream>
#include <random>
#include <map>


std::vector<int> primes;
int P;

bool isPrime(int a) {
    for (int i = 2; i*i <= a; ++i) {
        if (a % i == 0) return false;
    }
    return true;
}

uint32_t remainder(uint32_t a, uint32_t b, uint32_t d)
{
    uint32_t w = 1;
    uint32_t res = 0;
    for (int i = 0; i < P; ++i) {
        if (a & 1) {
            res = res + w;
            if (res >= d) {
                res -= d;
            }
        }
        w = (w * b) % d;
        a >>= 1;
    }
    return res;
}

std::vector<int> f(uint32_t a)
{
    std::vector<int> result;
    for (int base = 2; base <= 10; ++base) {
        for (auto d : primes) {
            if (remainder(a, base, d) == 0) {
                result.push_back(d);
                break;
            }
        }
        if (result.size() != base - 1) return {};
    }
    return result;
}

void solve(int n, int p) {
    ::P = p;
    std::map<uint32_t, std::vector<int>> result;
    std::mt19937 gen(12345);
    while (result.size() < n) {
        uint32_t a = gen();
        a |= (uint32_t(1) << (P - 1));
        a |= 1;
        a &= ((uint64_t(1) << P) - 1);
        if (result.count(a)) continue;
        auto divisors = f(a);        
        if (!divisors.empty()) {
            result[a] = divisors;
        }
    }
    
    for (const auto& item : result) {
        for (int i = P - 1; i >= 0; --i) {
            std::cout << ((item.first >> i) & 1);
        }
        for (auto d : item.second) {
            std::cout << " " << d;
        }
        std::cout << std::endl;
    }    
}

int main() {
    for (int i = 2; i < 10; ++i) {
        if (isPrime(i)) {
            primes.push_back(i);
        }
    }
    
    int T;
    std::cin >> T;
    int n, p;
    for (int i = 1; i <= T; ++i) {
        std::cin >> p >> n;
        std::cout << "Case #" << i << ":\n";
        solve(n, p);
    }
    return 0;
}