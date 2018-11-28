#include <iostream>
#include <string>
#include <vector>
#include <bitset>
using namespace std;

int T, J, N, CNT;
vector<long long> primes;
bitset<65536> notPrime;

void preComp() {
    primes.push_back(2);
    for (long long a = 3; a <= 65536; a += 2) {
        if (!notPrime[a]) {
            primes.push_back(a);
            for (long long b = a * a; b <= 65536; b += a)
                notPrime[b] = true;
        }
    }
}

long long isPrime(__uint128_t num) {
    for (int a = 0; a < (int)primes.size(); ++a)
        if (num % primes[a] == 0 && num != primes[a]) {
            return primes[a];
        }
    return -1;
}

__uint128_t conv(__uint128_t mask, __uint128_t base) {
    __uint128_t ans = 0;
    __uint128_t mult = 1;
    for (; mask; mask >>= 1) {
        if (mask & 1)
            ans += mult;
        mult *= base;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    preComp();
    cin >> T >> N >> J;
    cout << "Case #1:\n";
    for (__uint128_t a = 1LL << (N - 1); a < (1LL << N); ++a) { // Start with 1
        if (~ a & 1) continue; // Does not end with one
        vector<long long> TMP;
        bool valid = true;
        for (int b = 2; b <= 10; ++b) {
            __uint128_t num = conv(a, b);
            long long ret = isPrime(num);
            if (ret == -1) {
                valid = false;
                break;
            }
            TMP.push_back(ret); // non-trivial factor
        }
        if (!valid) continue;
        string S = bitset<35>(a).to_string();
        S = S.substr(S.find_first_not_of('0'));
        cout << S;
        for (int b = 0; b < (int)TMP.size(); ++b) {
            cout << " " << TMP[b];
        }
        cout << "\n";
        if (++CNT == J) break;
    }
    return 0;
}
