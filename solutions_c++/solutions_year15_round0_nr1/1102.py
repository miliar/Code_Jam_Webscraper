#include <stdio.h>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>


int main()
{
    unsigned num_test = 0;
    scanf("%u", &num_test);
    for (unsigned T = 0; T < num_test; ++T) {
        unsigned max_shyness = 0;
        scanf("%u ", &max_shyness);
        unsigned answer = 0;
        unsigned sum = 0;
        char chr = '\0';
        for (unsigned i = 0; i < max_shyness + 1; ++i) {
            scanf("%c", &chr);
            if (sum < i) {
                const unsigned diff = i - sum;
                answer += diff;
                sum += diff;
            }
            sum += (chr - '0');
        }
        printf("Case #%u: %u\n", T + 1, answer);
    }
    return 0;
}
