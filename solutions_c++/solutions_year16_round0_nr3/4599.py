//
//  main.cpp
//  codejam3
//
//  Created by Raphael Sampaio on 4/9/16.
//  Copyright © 2016 Raphael Sampaio. All rights reserved.
//
#include <vector>
#include <cmath>
#include <map>
#include <utility>
#include <stdint.h>
#include <iostream>

std::map<__uint128_t, std::pair<bool, __uint128_t>> prime;


bool is_prime(__uint128_t n, __uint128_t* divisor) {
    if (prime.find(n) == prime.end()) {
        __uint128_t sq = ceil(sqrt(n));
        if (n == 0 || n == 1)
            return true;
        for (__uint128_t i = 2; i <= sq; i++) {
            if (n % i == 0) {
                *divisor = i;
                prime[n] = std::make_pair(false, i);
                return false;
            }
        }
        prime[n] = std::make_pair(true, 0);
        return true;
    } else {
        *divisor = prime[n].second;
        return prime[n].first;
    }
}

__uint128_t get_number(int base, std::vector<int> n) {
    __uint128_t base10 = 0;
    int size = (int)n.size();
    
    for (int i = size - 1; i >= 0; i--) {
        base10 += (pow(base, i) * n[i]);
    }
    return base10;
}

std::vector<int> get_base2(__uint128_t n, __uint128_t max) {
    std::vector<int> number;
    __uint128_t div = n;
    __uint128_t res;
    number.push_back(1);
    while (div != 0) {
        res = div % 2;
        div = div / 2;
        number.push_back(res);
    }
    for (__uint128_t i = (int)number.size(); i < max - 1; i++) {
        number.push_back(0);
    }
    number.push_back(1);
    return number;
}

void jamcoin(int N, int J) {
    __uint128_t size = pow(2, N-2);
    std::vector<int> current_b2;
    __uint128_t current;
    __uint128_t div;
    int n = 0;
    bool all;
    int divisors[9];
    for (__uint128_t i = 0; i < size; i++) {
        current_b2 = get_base2(i, N);
        all = true;
        for(__uint128_t j = 2; j <= 10; j++) {
            current = get_number(j, current_b2);
            
            if (is_prime(current, &div)) {
                all = false;
                break;
            }
            else {
                divisors[j - 2] = div;
            }
        }
        if (all) {
            for (int i = N - 1; i >= 0; i--) {
                printf("%d", current_b2[i]);
            }
            for(int j = 2; j <= 10; j++) {
                printf(" %d", divisors[j - 2]);
            }
            printf("\n");
            if (++n == J) {
                return;
            }
        }
    }
}

int main(int argc, const char * argv[]) {
    
    int max, N, J;
    std::cin >> max;
    for(int i = 0; i < max; ++i)
    {
        std::cin >> N;
        std::cin >> J;
        
        printf("Case #%d: \n", i + 1);
        jamcoin(N, J);
    }
    
    return 0;
}
