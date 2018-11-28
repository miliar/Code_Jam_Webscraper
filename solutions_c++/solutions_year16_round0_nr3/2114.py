#include <iostream>
#include <bitset>
#include <cstdint>
#include <map>
using namespace std;

#include <InfInt.h>

#include <stdlib.h>

map<InfInt, InfInt> divs;

static const int LIMIT = 1000;

bool isPrime(const InfInt& v, InfInt& divisor)
{
    divisor = 2;
    if(divs.find(v) != divs.end()) divisor = divs[v];
    int count = 0;
    while(divisor < v) {
        if(v % divisor == 0) {
            divs[v] = divisor;
            return false;
        }
        divisor += InfInt::one;
        if(count++ == LIMIT) return true;
    }
    return true;
}

int main(int argc, char** argv) {
    const int num = atoi(argv[1]);
    const int len = 32;
    int cnt = 0;
    uint32_t i = (1 << (len-1)) + 1;
    cout << "Case #1:" << endl;
    while(cnt < num) {
        bitset<len> bs(i);
        bool prime = false;
        InfInt divisors[9];
        // cout << bs << " ";
        for(int base = 2; base <= 10; ++base) {
            InfInt v = InfInt::one;
            InfInt tmp = InfInt::one;
            for(int idx = 1; idx < len; ++idx) {
                tmp *= base;
                if(bs[idx]) v += tmp;
            }
            divisors[base-2] = InfInt::zero;
            // cout << base << ":" << v << " ";
            if(isPrime(v, divisors[base-2])) {
                prime = true;
                break;
            }
        }
        // cout << endl;
        if(!prime) {
            cout << bs;
            for(int j = 0; j < 9; ++j) cout << " " << divisors[j];
            cout << endl;
            cnt++;
        }
        i += 2;
    }
}
