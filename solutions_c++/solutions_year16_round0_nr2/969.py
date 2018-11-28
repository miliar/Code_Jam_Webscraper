//  main.cpp
//  Qualification Round B
//
//  Created by 苏炜 on 2016/4/9.

#include <iostream>
#include <string>

int main() {
    int T = 0;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::string S;
        std::cin >> S;
        
        int counter = 0;
        auto pre = S.begin();
        for (auto it = S.begin(); it != S.end(); ++it) {
            if (*it != *pre) {
                ++counter;
            }
            pre = it;
        }
        
        if (*pre == '-') {
            ++counter;
        }
        
        std::cout << "Case #" << t << ": " << counter << std::endl;
    }
    return 0;
}
