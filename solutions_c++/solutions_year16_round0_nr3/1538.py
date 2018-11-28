/*
 * abeakkas
 * Google CodeJam 2016 - Qualification Round
 * Problem C
 * Hello random stalker!
 */
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

typedef long long ll;
typedef unsigned long long ull;

// #define pr pair<ll,ll>
// #define vpr vector<pair<ll,ll> >

// Code snippets:
// (int*)calloc(1000000, sizeof(int));
// (int*)malloc(1000000 * sizeof(int));
// cout << setprecision(20);

using namespace std; 
ifstream fin("C.in");
ofstream fout("C.out");

const ull primen = 100;
ull primes[primen];

ull bitmod(ull bits, ull base, ull mod) {
    ull modsum = 0;
    ull exp = 1;
    for(ull i = 0; i < 32; i++) {
        if(bits & 1 << i) {
            modsum = (modsum + exp) % mod;
        }
        exp = (exp * base) % mod;
    }
    return modsum;
}

int primetest(ull bits, int print) {
    for(int i = 2; i <= 10; i++) {
        int flag = 1;
        for(int j = 0; j < primen; j++) {
            if(bitmod(bits, i, primes[j]) == 0) {
                flag = 0;
                if(print) {
                    fout << " " << primes[j];
                }
                break;
            }
        }
        if(flag) {
            return 0;
        }
    }
    return 1;
}

void printbits(ull x) {
    int flag = 0;
    for(int i = 63; i >= 0; i--) {
        if(flag) {
            fout << ((x >> i) & 1);
        } else {
            if((x / ((ull)1 << i)) & 1) {
                fout << 1;
                flag = 1;
            }
        }
    }
}

int main() {
    primes[0] = 2;
    int i = 1;
    for(ull x = 3; i < primen; x += 2) {
        int flag = 1;
        for(int j = 0; j < i; j++) {
            if(x % primes[j] == 0) {
                flag = 0;
                break;
            }
        }
        if(flag) {
            primes[i++] = x;
        }
    }
    int T, N, J;
    fin >> T >> N >> J;
    fout << "Case #1:" << endl;
    ull x = ((ull)1 << (N - 1)) + 1;
    for(int i = 0; i < J; i++) {
        while(!primetest(x, 0)) {
            x += 2;
        }
        printbits(x);
        primetest(x, 1);
        fout << endl;
        x += 2;
    }
	return 0;
}