//
//  main.cpp
//  Codejam2015Qualifier
//
//  Created by Krishnan Nakul on 11/04/15.
//  Copyright (c) 2015 Krishnan Nakul. All rights reserved.
//

#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    // insert code here...
    int tests, tc = 1;
    scanf("%d", &tests);
    while (tc <= tests) {
        int s_max, ans = 0;
        std::string shyness_level;
        std::cin >> s_max >> shyness_level;
        int cur_cnt = shyness_level[0] - '0';
        for (int k = 1; k < s_max + 1; k++) {
            if((shyness_level[k] - '0' > 0) and (cur_cnt < k)) {
                ans += (k-cur_cnt);
                cur_cnt += (k-cur_cnt);
            }
            cur_cnt += shyness_level[k] - '0';
        }
        printf("Case #%d: %d\n", tc, ans);
        tc++;
    }
    return 0;
}
