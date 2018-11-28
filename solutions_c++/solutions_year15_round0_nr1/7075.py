//
//  A.cpp
//  CodeJam
//
//  Created by Sidharth Juyal on 11/04/15.
//
#include <cassert>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

int main(int argc, const char * argv[]) {
    
    assert(argc == 2);
    
    std::ifstream fin(argv[1]);
    
    std::string line;
    for (int caseNo = 0; std::getline(fin, line); ++caseNo) {
        if (caseNo > 0) {
            std::stringstream stream(line);
            int smax;
            std::string groups;
            if (stream >> smax >> groups) {
                int missingCount = 0;
                int activeCount = 0;
                for (int shyness = 0; shyness < groups.size(); ++shyness) {
                    int requiredCount = shyness - activeCount;
                    if (requiredCount > 0) {
                        missingCount++;
                        activeCount += requiredCount;
                    }
                    activeCount += (groups[shyness] - '0');
                }
                std::cout << "Case #" << caseNo << ": " << missingCount << std::endl;
            }
        }
    }
    
    return 0;
}
