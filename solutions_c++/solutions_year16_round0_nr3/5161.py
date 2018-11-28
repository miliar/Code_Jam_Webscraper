//
//  main.cpp
//
//
//  Created by Aaron Ruel on 3/11/16.
//  Copyright (c) 2016 AAR. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <vector>
#include <math.h>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <stdint.h>
#include <stdlib.h>

#define ASCII_OFFSET 48

bool isprime(unsigned long long n);

int main(int nargs, char** argv)
{
    int getCount, length, TC;
    std::cin >> getCount >> length >> TC;
    
    int k = 0;

    for(; k < getCount; ++k){
        std::vector<uint64_t> acc;
        std::vector<uint64_t> intermed;
        std::cout << "Case #1:\n";
        int p = 0;
        primeflag:for(; p < TC; ++p){
            intermed.clear();
            std::string eval = "1" + std::bitset<64>(p).to_string() + "1";
            eval.erase(eval.begin()+1, eval.begin()+65-(length-2));
            std::reverse(eval.begin(), eval.end());
            for (int i = 2; i <= 10; ++i){
                uint64_t sum = 0;
                for(int j = 0; j < eval.length(); ++j) {
                    if(eval[j] == '1') {
                        uint64_t o = pow(i, j);
                        acc.push_back(o);
                    }
                }
                //sum = std::accumulate(acc.begin(), acc.end(), 0);
                for(int e = 0; e < acc.size(); ++e){
                    sum += acc[e];
                }
                acc.clear();
                if(isprime(sum)){
                    ++TC;
                    ++p;
                    intermed.clear();
                    goto primeflag;
                }
                intermed.push_back(sum);
                sum = 0;
            }
            std::reverse(eval.begin(), eval.end());
            std::cout << eval << " ";
            for(int x = 0; x < intermed.size(); ++x){
                uint64_t y = 2;
                unsigned long long temp;
                while(intermed[x] % y != 0){
                    temp = intermed[x];
                    ++y;
                }
                std::cout << y;
                if(x != 8) std::cout << " ";
            }
            std::cout << '\n';
        }
    }
}

bool isprime(unsigned long long n){
        if (n <= 1)
            return false;
        if (n == 2)
            return true;
        for (unsigned int i = 2; i <= sqrt(n); ++i)
            if (n % i == 0)
                return false;
        return true;
    }