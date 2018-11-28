#include <stdio.h>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>



int main()
{
    unsigned num_test = 0;
    scanf("%u", &num_test);
    for (unsigned T = 0; T < num_test; ++T) {
        unsigned R, C, W;
        scanf("%u %u %u", &R, &C, &W);
        //Find row with ship
        unsigned answer = R * (C / W);
        //Find right border
        if (C % W > 0) {
            answer += 1;
        }
        //Kill ship 
        answer += W - 1;
        printf("Case #%u: %u\n", T + 1, answer);
    }
    return 0;
}
