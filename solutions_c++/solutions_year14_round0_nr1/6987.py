//
//  main.cpp
//  GoogleCodeJam2014
//
//  Created by Hisai Toru on 2014/04/12.
//  Copyright (c) 2014年 Kronecker's Delta Studio. All rights reserved.
//

#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <list>

void problem_a()
{
    int t;
    std::cin >> t;
    
    for (int i = 0; i < t; i++) {
        int row1;
        std::cin >> row1;
        int card[4][4];
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                std::cin >> card[r][c];
            }
        }
        std::set<int> choosed1(&card[row1 - 1][0], &card[row1 - 1][4]);

        int row2;
        std::cin >> row2;
        int card2[4][4];
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                std::cin >> card2[r][c];
            }
        }

        std::set<int> choosed2(&card2[row2 - 1][0], &card2[row2 - 1][4]);
//        std::list<int> output;
//        std::set_intersection(choosed1.begin(), choosed1.end(), choosed2.begin(), choosed2.end(),
//                                                  output.begin());
        std::set<int> output;
        std::set_intersection(choosed1.begin(), choosed1.end(), choosed2.begin(), choosed2.end(),
                              std::inserter(output, output.end()));

        std::cout << "Case #" << i + 1 << ": ";
        if (output.size() == 0) {
            std::cout << "Volunteer cheated!";
        } else if(output.size() == 1) {
            std::cout << *output.begin();
        } else {
            std::cout << "Bad magician!";
        }
        std::cout << std::endl;
    }
}


int main(int argc, const char * argv[])
{

    // insert code here...
//    std::cout << "Hello, World!\n";
    problem_a();
    return 0;
}

