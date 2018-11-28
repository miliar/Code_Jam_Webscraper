//
//  main.cpp
//  codejam
//
//  Created by 원재 정 on 2016. 4. 9..
//  Copyright © 2016년 Anthony Jung. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdint>
#include <cmath>

std::vector<unsigned long> find_fractiles(int k, int c, int s) {
    std::vector<unsigned long> result;
    if ((k - 1 > s) || (c == 1 && k > s)) {
        return result;
    }
    
    if (c == 1 || k == 1)
        result.push_back(1);
    
    for (int i = 2; i <= k; ++i) {
        result.push_back(i);
    }
    return result;
}

int main(int argc, const char * argv[]) {
    int t;
    std::ifstream fin("D-small-attempt1.in");
    std::ofstream fout("D-small-attempt1.out");
    fin >> t;
    for (int i = 1; i <= t; ++i) {
        int k, c, s;
        fin >> k >> c >> s;
        auto result = find_fractiles(k, c, s);
        fout << "Case #" << i << ": ";
        if (result.empty()) {
            fout << "IMPOSSIBLE" << std::endl;
        } else {
            for (auto& num : result) {
                fout << num << " ";
            }
            fout << std::endl;
        }
    }
    fin.close();
    fout.close();
    
    return 0;
}
