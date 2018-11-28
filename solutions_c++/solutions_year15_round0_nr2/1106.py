#include <stdio.h>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>


const unsigned MAX_NUM_PLATES = 1000;
const unsigned MAX_NUM_PANCAKES = 1000;
unsigned pancakes[MAX_NUM_PANCAKES + 10];

int main()
{
    unsigned num_test = 0;
    scanf("%u", &num_test);
    for (unsigned T = 0; T < num_test; ++T) {
        unsigned num_plates = 0;
        scanf("%u", &num_plates);
        unsigned min_time = 0;
        memset(pancakes, 0, sizeof(pancakes));
        for (unsigned i = 0; i < num_plates; ++i) {
            unsigned num_pancakes = 0;
            scanf("%u", &num_pancakes);
            ++pancakes[num_pancakes];
            min_time = std::max(min_time, num_pancakes);
        }
        for (unsigned max_pancakes = 1; max_pancakes <= MAX_NUM_PANCAKES; ++max_pancakes) {
            unsigned current_time = max_pancakes;
            for (unsigned i = 1; i <= MAX_NUM_PANCAKES; ++i) {
                if (i > max_pancakes) {
                    current_time += pancakes[i] * ((i + max_pancakes - 1) / max_pancakes - 1); 
                }
            }
            if (current_time < min_time) {
                min_time = current_time;
            }
        }
        printf("Case #%u: %u\n", T + 1, min_time);
    }
    return 0;
}
