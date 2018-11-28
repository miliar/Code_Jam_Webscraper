#include <stdio.h>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>


const unsigned MAX_STRING_LENGTH = 10000;
int digits[MAX_STRING_LENGTH * 12 + 10];

int to_idx(const char chr)
{
    switch (chr) {
        case '1' : return 1;
        case 'i' : return 2;
        case 'j' : return 3;
        case 'k' : return 4;
        default : throw 42;
    }
}

int mult_table[4][4] = {
    { 1, 2, 3, 4},
    { 2,-1, 4,-3},
    { 3,-4,-1, 2},
    { 4, 3,-2,-1}
};

int mult(const int a, const int b)
{
    bool sign = ((a < 0) != (b < 0));
    int answer = mult_table[abs(a) - 1][abs(b) - 1];
    return sign ? - answer : answer;
}

const std::string YES = "YES";
const std::string NO = "NO";

int main()
{
    unsigned num_test = 0;
    scanf("%u", &num_test);
    for (unsigned T = 0; T < num_test; ++T) {
        unsigned L = 0;
        unsigned long long X = 0;
        scanf("%u %llu\n", &L, &X);
        const unsigned long long full_length = std::min(X * L, L * (8 + X % 4));
        for (unsigned i = 0; i < L; ++i) {
            char letter = '\0';
            scanf("%c", &letter);
            const int letter_index = to_idx(letter);
            unsigned position = i;
            while (position < full_length) {
                digits[position] = letter_index;
                position += L;
            }
        }
        unsigned position = 0;
        int i_product = 1;
        while (position != full_length && i_product != to_idx('i')) {
            i_product = mult(i_product, digits[position]);
            ++position;
        }
        int j_product = 1;
        while (position != full_length && j_product!= to_idx('j')) {
            j_product = mult(j_product, digits[position]);
            ++position;
        }
        int k_product = 1;
        while (position != full_length) {
            k_product = mult(k_product, digits[position]);
            ++position;
        }
        std::string answer = NO;
        if (i_product == to_idx('i')
            && j_product == to_idx('j')
            && k_product == to_idx('k')) {
            answer = YES;
        }
        printf("Case #%u: %s\n", T + 1, answer.c_str());
    }
    return 0;
}
