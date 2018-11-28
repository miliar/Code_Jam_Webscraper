/* 
 * File:   main.cpp
 * Author: juro
 *
 * Created on April 10, 2016, 12:19 AM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <math.h>
#include <string.h>
#include "BigIntegerLibrary.hh"

using namespace std;

/*
 * 
 */
vector<long long> primes;

void sieve(long long n, int primes[]) {
    for (int i = 0; i < n; i++) primes[i] = 1;
    primes[0] = 0;
    primes[1] = 0;
    for (int i = 2; i < sqrt(n); i++) {
        for (int j = i*i; j < n; j += i) {
            primes[j] = 0;
        }
    }
}

BigInteger convert(long long n, int base) {
    BigInteger mult = 1;
    BigInteger res = 0;
    while (n > 0) {
        res += (n%2 == 0 ? 0 : mult);
        mult = mult * base;
        n /= 2;
    }
    return res;
}

string binary(long long n) {
    if (n == 0) return "0";
    if (n == 1) return "1";
    return binary(n/2) + to_string(n%2);
}

long long min(long long a, long long b) {
    return a < b ? a : b;
}

long long find_divisor(BigInteger num) {
    for (int i = 0; i < min(primes.size(), 50); i++) {
        BigInteger pr((long int) primes[i]);
        if (num%pr == 0) return primes[i];
    }
    return 0;
}

vector<long long> test_num(long long num) {
    vector<long long> res;
    for (int base = 2; base <= 10; base++) {
        BigInteger c = convert(num, base);
        long long divisor = find_divisor(c);
        if (divisor == 0) break;
        res.push_back(divisor);
    }
    return res;
}

int main(int argc, char** argv) {

    int n, j, t;
    cin >> t >> n >> j;    
    
    long long top = (1 << n);
    int *prsieve = new int[65536];
    
    sieve(65536, prsieve);

    for (int i = 0; i < 65536; i++) {
        if (prsieve[i] == 1) primes.push_back(i);
    }
    
    long long start = (1LL << (n-1));
    long long found = 0;
        
    cout << "Case #1:" << endl;
    
    for (long long i = start+1; i < (start << 1); i += 2) {
        vector<long long> divisors = test_num(i);
        if (divisors.size() == 9) {
            cout << binary(i) << " ";
            for (long long divisor : divisors) cout << divisor << " ";
            cout << endl;
            found++;
            if (found == j) return 0;
        }
    }
    
    return 0;
}

