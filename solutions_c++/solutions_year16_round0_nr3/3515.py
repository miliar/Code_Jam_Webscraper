#include <cassert>
#include <vector>
#include <map>
#include <cstdio>
using namespace std;
int N, J;
bool isprime(long long x) {
    if (x == 2)
        return true;
    if (!(x&1))
        return false;
    for (long long i = 3; i * i <= x; i += 2) {
        if (x % i == 0)
            return false;
    }
    return true;
}

long long bin2base(int val, int base) {
    long long newval = 0;
    for (int i = N - 1; i >= 0; i--) {
        newval = newval * ((long long) base) + ((val >> i) & 1);
    }
    return newval;
}

int main() {
    N = 16; J = 50;
    map<long long, vector<long long>> factors;
    int counter = 0;
    for (int i = 0; i < (1 << (N - 2)); i++) {
        int value = (1 << (N - 1)) + 1;
        for (int j = 0; j < (N - 2); j++) {
            if (i & (1 << j))
                value |= (1 << (j + 1));
        }
       
        bool hasprime = false;
        for (int base = 2; base <= 10; base++) {
            long long basevalue = bin2base(value, base);
            if (isprime(basevalue)) {
                hasprime = true;
                break;
            }
        }

        if (!hasprime) {
            for (int base = 2; base <= 10; base++) {
                long long basevalue = bin2base(value, base);
                for (long long factor = 3; factor * factor <= basevalue; factor += 2) {
                    if (basevalue % factor == 0) {
                        factors[value].push_back(factor);
                        break;
                    }
                }
            }
            if (factors[value].size() != 9) {
                factors.erase(value);
            } else {
                ++counter;
            }
            if (counter == J)
                break;
        }
    }
    printf("Case #1:\n");
    for (auto &it : factors) {
        printf("1");
        for (int i = N - 2; i >= 1; i--) {
            printf("%lld", (it.first >> i) & 1);
        }
        printf("1");
        assert(it.second.size() == 9);
        for (int i = 0; i < it.second.size(); i++) {
            printf(" %lld", it.second[i]);
        }
        printf("\n");
    }
    return 0;
}
