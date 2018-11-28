
#include "BigUnsigned.hh"
#include "BigUnsigned.cc"
 
#include <iostream>
#include <fstream>
#include <vector>
#include <climits>
#include <stdio.h>
using namespace std;

typedef unsigned int INT;
typedef BigUnsigned BIGINT;

vector<INT> compute_prime_numbers(INT limit) {
    vector<INT> result(1, 2);
    vector<char> sieve(limit / 2);
    for (INT i = 3; i < limit; i += 2) {
        if (sieve[i >> 1]) continue;
        result.push_back(i);
        unsigned long long j;
        for (j = i; j < limit; j += i * 2)
            sieve[j >> 1] = 1;
    }
    return result;
}

template<class T>
INT get_divisor(const vector<INT> &prime, const T &x, size_t size) {
    if (!size)
        size = prime.size();
    for (size_t i = 0; i < size; i++) {
        T c(prime[i]);
        if (x % c == 0) return prime[i];
        if (c > x / 2) break;
    }
    return 0;
}

int main() {
    int T, N, J;
    cin >> T >> N >> J;
    vector<INT> prime;
    INT limit = (N < 32) ? (1 << N) : INT(-1);
    size_t size = (N < 32) ? 0 : 10000;

    char path[] = "pXX.bin";
    sprintf(path + 1, "%02d", N);
    path[3] = '.';
    ifstream in(path, ios::binary | ios::ate);
    size_t fsize = in.tellg();
    if (fsize != -1) {
        prime.resize(fsize / sizeof(INT));
        in.seekg(0);
        for (size_t i = 0; i < prime.size(); i++)
            in.read((char*)&prime[i], sizeof(INT));
    } else {
        prime = compute_prime_numbers(limit);
        ofstream out(path, ios::binary);
        for (size_t i = 0; i < prime.size(); i++)
            out.write((char*)&prime[i], sizeof(INT));
        out.close();
    }

    cout << "Case #1:" << endl;
    int total = 0;
    vector<INT> divs(9);
    for (INT i = (1 << (N - 1)) + 1; i < limit; i += 2) {
        INT d = get_divisor(prime, i, size);
        if (!d) continue;
        divs[0] = d;
        for (int base = 3; base <= 10; base++) {
            BIGINT x = 0, r = 1;
            for (int j = 0; j < N; j++, r *= base)
                if (i & (1 << j))
                    x += r;
            d = get_divisor(prime, x, size);
            if (!d) break;
            divs[base - 2] = d;
        }
        if (d) {
            for (int t = N - 1; t >= 0; t--)
                cout << ((i & (1L << t)) ? '1' : '0');
            for (int t = 0; t < 9; t++)
                cout << ' ' << divs[t];
            cout << endl;
            cerr << total << endl;
            if (++total == J) break;
        }
    }
    return 0;
}
