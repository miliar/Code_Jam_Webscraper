#include <bitset>
#include <cmath>
#include <iostream>
#include <vector>

#define PRIME_UB 34000000

std::vector<int> calcPrimes(int maxN)
{
    std::vector<int> primes;
    primes.reserve(1000000);

    primes.push_back(2);
    for (int i = 3; i < maxN; i += 2) {
        int ub = std::sqrt(i) + 1;
        bool primeFlag = true;
        for (auto p : primes) {
            if (p > ub)
                break;

            if (i % p == 0) {
                primeFlag = false;
                break;
            }
        }

        if (primeFlag)
            primes.push_back(i);
    }

    return primes;
}

long long cvtToBase(int x, int base)
{
    long long ret = 0;
    for (int i = 0; i < 31; ++i)
        ret += ((x >> i) & 1) * std::pow(base, i);

    return ret;
}

void solve(int n, int cnt)
{
    int m = n - 2;
    auto primes = calcPrimes(PRIME_UB);
    int nJamcoins = 0;

    for (int i = 0; i < (1 << m); ++i) {
        int target = (1 << (n - 1)) | (i << 1) | 1;
        // std::cout << i << " " << std::bitset<16>(target) << std::endl;
        bool primeFlag = false;
        for (int j = 2; j <= 10 && !primeFlag; ++j) {
            auto x = cvtToBase(target, j);
            long long ub = std::sqrt(x) + 1;
            for (auto p : primes) {
                if (p > ub) {
                    primeFlag = true;
                    break;
                }

                if (x % p == 0)
                    break;
            }
        }

        if (!primeFlag) {
            ++nJamcoins;
            std::cout << cvtToBase(target, 10) << " ";
            for (int i = 2; i <= 10; ++i) {
                auto x = cvtToBase(target, i);
                for (auto p : primes)
                    if (x % p == 0) {
                        std::cout << p;
                        break;
                    }

                if (i != 10)
                    std::cout << " ";
            }
            std::cout << std::endl;
            if (nJamcoins >= cnt)
                return;
        }
    }
}

int main()
{
    int t, n, j;
    std::cin >> t >> n >> j;
    std::cout << "Case #" << t << ":" << std::endl;
    solve(n, j);

    return 0;
}
