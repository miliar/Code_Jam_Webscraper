//
//  main.cpp
//  codejam
//
//  Created by Todor Lyubomirov Bonchev on 1/1/16.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

int n, j;

int jc[33];

// returns divisor if the number is not prime
// else returns 0
long long isPrimeInBase(int base) {
    long long numInBase = 0;
    for (int i=0;i<n;++i) {
        numInBase *= base;
        numInBase += jc[i];
    }
    long long sqrtN = ceil(sqrtl(numInBase));
    bool isPrime = true;
    long long divisor = -1;
    for (long long test = 2; test < sqrtN; ++test) {
        if (numInBase % test == 0) {
            isPrime = false;
            divisor = test;
            break;
        }
    }
    if (isPrime) {
        return 0;
    }
    return divisor;
}
int printed = 0;
void isJam() {
    // ceck if jc is jamcoin
    // return if it is not
    // else print it with its devisors in each base
    vector<long long> divisors;
    for (int base=2; base<=10; base++) {
        long long divisor = isPrimeInBase(base);
        if (divisor == 0) {
            return;
        }
        divisors.push_back(divisor);
    }
    printed++;
    for (int i = 0; i < n; ++i) {
        printf("%d",jc[i]);
    }
    for (int i=0;i<divisors.size();++i) {
        printf(" %lld", divisors[i]);
    }
    putchar('\n');
}

bool shouldStop = false;
void gen(int idx) {
    if (shouldStop) return;
    if (idx == n-1) {
        isJam();
        if (printed == j) {
            shouldStop = true;
        }
        return;
    }
    jc[idx]=1;
    gen(idx+1);
    if (shouldStop) return;
    jc[idx]=0;
    gen(idx+1);
    if (shouldStop) return;
}

void solve() {
    cin >> n >> j;
    jc[0]=jc[n-1]=1;
    gen(1);
}

int main(int argc, const char * argv[]) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);
    for (int test=1;test<=tests;++test) {
        printf("Case #%d:\n", test);
        solve();
    }

    return 0;
}
