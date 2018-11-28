#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <complex>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <ctime>

using namespace std;

typedef pair<int,int> point;

typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef signed short int16_t;
typedef unsigned short uint16_t;
typedef signed int int32_t;
typedef unsigned int uint32_t;

void output_binary(uint32_t b, size_t N) {
    for(size_t i = N; i != 0; --i) {
        printf("%d", ((b >> (i-1)) & 1));
    }
}

void output_jamcoin(uint32_t b, size_t N, const vector<uint64_t> &ntd) {
    
    output_binary(b, N);

    vector<uint64_t>::const_iterator it2 = ntd.begin();
    for(;it2 != ntd.end(); ++it2) {
        printf(" ");
        printf("%llu", *it2);
    }
    printf("\n");
}

void init(uint32_t &b, size_t N) {
    b |= 1;
    b |= (1 << (N - 1));
}
bool next(uint32_t &b, size_t N) {
    uint32_t max = 0;
    for(uint32_t i = 0; i < N; ++i) {
        max |= (1 << i);
    }

    uint32_t mask = 0;
    mask |= 1;
    mask |= (1 << (N - 1));

    while(true) {
        if(b == max) {
            return false;
        }
        b++;
        if((b & mask) == mask) {
            return true;
        }
    }
    //size_t num = count(b.begin(), b.end(), false);
    //if(num == 0) {
    //    return false;
    //}
    //
    //uint32_t digit = 0;
    //size_t pos = 0;
    //for(vector<bool>::reverse_iterator rit = b.rbegin(); rit != b.rend(); ++rit) {
    //    digit |= ((*rit) ? 1 : 0) << pos;
    //    pos++;
    //}

}

uint64_t has_non_trivial_divisor(uint64_t num, uint64_t start) {
    for(uint64_t i = start; i <= num / i; i += 2) {
        if(num % i == 0) {
            return i;
        }
    }
    return 0;
}

uint64_t jamcoin2num(uint32_t digit, size_t N, uint32_t base) {
    uint64_t num = 0;
    for(size_t i = 0; i < N; ++i) {
        bool b = (digit >> i) & 1;
        if(b) {
            num += pow(base, i);
        }
    }
    return num;
}

//uint64_t check_jamcoin(uint32_t digit, size_t N, uint32_t base) {
//    uint64_t start = 3;
//
//    uint64_t ret = has_non_trivial_divisor(num, start);
//
//    return ret;
//}

void solve(size_t t, size_t N, size_t J) {

    printf("Case #%lu:\n", t);

    size_t j = 0;
    uint32_t digit = 0;
    init(digit, N);
    do {
        bool is_jamcoin = true;
        vector<uint64_t> non_trivial_divisors;
        //output_binary(digit , N); printf("\n");//// test
        for(uint32_t base = 2; base <= 10; ++base) {

            uint64_t num = jamcoin2num(digit, N, base);
            //printf("%llu\n", num); ////

            uint64_t first_non_trivial_divisor = 0;

            uint64_t start = 3;
            first_non_trivial_divisor = has_non_trivial_divisor(num, start);

            if(!first_non_trivial_divisor) {
                is_jamcoin = false;
                break;
            } else {
                non_trivial_divisors.push_back(first_non_trivial_divisor);
            }
        }
        if(is_jamcoin) {
            output_jamcoin(digit, N, non_trivial_divisors);
            j++;
        }
    } while(next(digit, N) && j < J);
}

int main() {
    
    size_t T, N, J;
    cin >> T;
    for(size_t t = 0; t < T; ++t) {
        cin >> N >> J;
        solve(t+1, N, J);
    }

    return 0;
}
