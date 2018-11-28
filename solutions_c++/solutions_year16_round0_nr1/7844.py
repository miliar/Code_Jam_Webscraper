//
//  main.cpp
//  Counting Sheep
//
//  Created by Jun Hao Xia on 09/04/16.
//  Copyright © 2016 Robotex. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <set>

int main(int argc, const char * argv[]) {
    // insert code here...
    if (argc != 2)
    {
        std::cout << "Pass the test case as argument" << std::endl;
        return 1;
    }
    
    std::ifstream fin(argv[1]);
    std::ofstream fout("output.txt");
    unsigned int T;
    unsigned int N;
    
    fin >> T;
    for (unsigned i = 1; i <= T; ++i)
    {
        std::set<unsigned int> digits;
        unsigned int k = 0;
        
        fin >> N;
        
        if (N > 0)
        {
            while (digits.size() < 10)
            {
                ++k;
                unsigned int digitsToParse = k * N;
                unsigned int digitExtracted;
                while (digitsToParse != 0)
                {
                    digitExtracted = digitsToParse % 10;
                    digitsToParse /= 10;
                    digits.insert(digitExtracted);
                }
            }
        }
        
        fout << "Case #" << i << ": ";
        
        if (digits.size() == 10)
            fout << k * N << std::endl;
        else
            fout << "INSOMNIA" << std::endl;
    }
    return 0;
}
