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

std::tuple<std::string, int, int, int> dfs(int current, int depth) {
    if (depth == 0) {
        if (current == 0) {
            return { "P", 1, 0, 0 };
        }
        if (current == 1) {
            return { "R", 0, 1, 0 };
        }
        return { "S", 0, 0, 1 };
    }
    auto lhs = dfs(current, depth - 1);
    auto rhs = dfs((current + 1) % 3, depth - 1);
    
    auto l = std::get<0>(lhs);
    auto r = std::get<0>(rhs);
    
    auto result = std::min(l + r, r + l);
    return { result,
        std::get<1>(lhs) + std::get<1>(rhs),
        std::get<2>(lhs) + std::get<2>(rhs),
        std::get<3>(lhs) + std::get<3>(rhs)
    };
}

std::string solve(int n, int papers, int rocks, int scissors) {
    std::string result = "IMPOSSIBLE";
    
    for (int i = 0; i < 3; ++i) {
        auto v = dfs(i, n);
        auto k = std::get<0>(v);
        auto p = std::get<1>(v);
        auto r = std::get<2>(v);
        auto s = std::get<3>(v);
        if (p == papers && r == rocks && s == scissors) {
            if (result == "IMPOSSIBLE" || result > k) {
                result = k;
            }
        }
    }
    
    return result;
}

int main() {
    std::freopen("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/in", "r", stdin);
    std::freopen("/Volumes/Setup/Android/projects/mep/mepcpp/mepcpp/out", "w", stdout);
    
    int tn;
    std::cin >> tn;
    
    for (int ti = 1; ti <= tn; ++ti) {
        int n, rocks, papers, scissors;
        std::cin >> n >> rocks >> papers >> scissors;
        
        std::cout << "Case #" << ti << ": " << solve(n, papers, rocks, scissors) << std::endl;
    }
}