//
//  fox.cpp
//  mepcpp
//
//  Created by Zinge on 5/28/16.
//  Copyright © 2016 MEP. All rights reserved.
//

#include <algorithm>
#include <atomic>
#include <array>
#include <cassert>
#include <cstring>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <sstream>
#include <stack>
#include <string>
#include <thread>
#include <tuple>
#include <typeindex>
#include <utility>
#include <vector>
#include <regex>

int main() {
    std::freopen("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/in", "r", stdin);
    std::freopen("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/out", "w", stdout);
    
    int tn;
    std::cin >> tn;
    
    for (int ti = 1; ti <= tn; ++ti) {
        int n, k;
        std::cin >> n >> k;
        
        std::vector<double> probs(n);
        
        for (int i = 0; i < n; ++i) {
            std::cin >> probs[i];
        }
        
        double answer = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            int bits = 0;
            for (int t = mask; t; t &= t - 1) {
                bits++;
            }
            if (bits == k) {
                std::vector<double> dp(k * 2 + 1);
                dp[k] = 1;
                for (int i = 0; i < n; ++i) {
                    std::vector<double> temp(k * 2 + 1);
                    if ((mask >> i) & 1) {
                        for (int j = 1; j + 1 < dp.size(); ++j) {
                            if (dp[j] > 0) {
                                temp[j + 1] += dp[j] * probs[i];
                                temp[j - 1] += dp[j] * (1 - probs[i]);
                            }
                        }
                        dp.swap(temp);
                    }
                }
                answer = std::max(answer, dp[k]);
            }
        }
        std::cout << "Case #" << ti << ": " << answer << std::endl;
    }
}