#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;

long long prime_table50[50] = {
       2,  3,  5,  7, 11, 13, 17, 19, 23, 29,
      31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
      73, 79, 83, 89, 97,101,103,107,109,113,
     127,131,137,139,149,151,157,163,167,173,
     179,181,191,193,197,199,211,223,227,229
};

vector<long long> prime_table(prime_table50, prime_table50 + 50);

// 0 indicates prime
long long find_divisor(long long in) {
    for(long long cur = 0; cur < prime_table.size(); ++cur) {
        if (in % prime_table[cur] == 0)
            return prime_table[cur];
        if (prime_table[cur] >= sqrt(in))
            break;
    }
    return 0;
}

void precompute_prime(long long max) {
    for (long long i = prime_table.back(); i < max; i += 2) {
        bool found = false;
        long long divi = find_divisor(i);
        if (divi == 0)
            prime_table.push_back(i);
    }
}

long long base_table[10][40];

void precompute_base() {
    for (int i = 2; i <= 10; ++i) {
        for (int j = 0; j < 32; ++j) {
            base_table[i][j] = pow(i, j);
        }
    }
}

long long convert(long long in, long long base) {
    if (base == 2) return in;
    long long ret = 0;
    int pow = 0;
    while(in > 0) {
        ret += in % 2 * base_table[base][pow++];
        in /= 2;
    }
    return ret;
}

void print_coin(long long in, int n) {
//    cout << "Coin: " << endl;
    for(int i = n - 1; i >= 0; --i) {
        cout << in / base_table[2][i]; 
        in %= base_table[2][i];
    }
//    cout << endl;
}

int main() {
    precompute_base();
    precompute_prime(sqrt(pow(2, 32)));
    int t;
    cin >> t;
    for (int round = 1; round <= t; ++round) {
        int n, j;
        int cnt = 0;
        cin >> n >> j;

        int count = 0;
        long long divisors[10000][11];
        for (long long i = pow(2, n - 1) + 1; i <= pow(2, n) - 1; i += 2) {
            bool matched = true;
            divisors[cnt][0] = i;
//            print_coin(i);
            for(int k = 2; k <= 10; ++k) {
                long long tar = convert(i, k);
//                cout << "Convert: " << tar << endl;
                divisors[cnt][k] = find_divisor(tar);
//                cout << divisors[cnt][k] << endl;
                if (divisors[cnt][k] == 0) {
                    matched = false;
                    break;
                }
            }
            if (matched)
                cnt++;
            if (cnt == j) break;
        }

        cout << "Case #" << round << ":" << endl;
        for (int i = 0; i < cnt; ++i) {
            print_coin(divisors[i][0], n);
            for (int j = 2; j <= 10; ++j) {
                cout << " " << divisors[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
