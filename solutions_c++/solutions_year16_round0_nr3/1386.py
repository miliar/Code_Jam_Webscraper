#include <algorithm>
#include <cstdio>
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>

static uint64_t MAX_FACTOR = 512;

/// -1 if 'prime'
uint64_t find_divisor(int a, uint64_t bit_pattern)
{
    uint64_t lim = MAX_FACTOR;
    
    for(uint64_t i = 2; i < lim; ++i)
    {
        uint64_t modulo_sum = 0;
        uint64_t modulo_power = 1;
        uint64_t bit = 1;
        while(bit <= bit_pattern)
        {
//             printf("lol %llu %llu\n", bit, bit_pattern);
            if((bit_pattern & bit) != 0)
                modulo_sum += modulo_power % i;
            bit *= 2;
            modulo_power = (a*modulo_power) % i;
        }
        
        if(modulo_sum % i == 0)
            return i;
    }
    return -1;
}

void solve(uint64_t N, uint64_t J)
{
    uint64_t start = (1ULL << uint64_t(N - 1ULL)) + 1ULL;
    uint64_t end = (1ULL << N);
//     printf("Solve %llu %llu\n", start, end);
    int answers = 0;
    for(uint64_t i = start; i < end; i += 2)
    {
//         printf("%llu\n", i);
        std::vector<uint64_t> divisors;
        bool found = true;
        for(int base = 2; base <= 10; ++base)
        {
            uint64_t div = find_divisor(base, i);
            if(div == -1)
                found = false;
            divisors.push_back(div);
//             printf("\t%d %llu\n", base, div);
        }
        
        if(found)
        {
            answers++;
            uint64_t bits = i;
            std::string bitstr = "";
            while(bits)
            {
                char x = (bits % 2 == 1) ? '1' : '0';
                bitstr.push_back(x);
                bits/=2;
            }
            std::reverse(bitstr.begin(), bitstr.end());
            printf("%s ", bitstr.c_str());
            for(auto x : divisors)
                printf("%llu ", x);
            printf("\n");
            
            if(answers == J)
                return;
        }
    }
}

void solve_small()
{
    solve(16, 50);
}

void solve_large()
{
    solve(32, 500);
}

int main(int argc, char** argv)
{
    printf("Case #1:\n");
    solve_large();
}