//
//  main.cpp
//  RankAndFile
//
//  Created by Raymond Tse on 4/15/16.
//  Copyright © 2016 Raymond Tse. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>


int main(int argc, const char * argv[]) {
    std::ifstream inFp(argv[1]);
    
    if (!inFp.is_open())
    {
        fprintf(stderr, "Can't open the file");
        exit(1);
    }
    
    std::ofstream outFp("out.txt");
    
    int numInputs;
    int n;
    int num;
    

    
    
    inFp >> numInputs;
    
    for (int i = 0; i < numInputs; i++)
    {
        std::vector<int> missingRow;
        std::map<int,int> allNums;
        inFp >> n;
        for (int x = 0; x < ((n * 2) -1)*n; x++) {
            inFp >> num;
            auto iter = allNums.find(num);
            if (iter == allNums.end()) {
                allNums[num] = 1;
            } else {
                allNums[num] = (iter->second) + 1;
            }
        }
        for(auto const &number : allNums) {
            if (number.second % 2 == 1) {missingRow.push_back(number.first);}
        }
        
        std::sort(missingRow.begin(),missingRow.end());
        std::string answer = "";
        for (int temp:missingRow) {answer = answer + std::to_string(temp) + " ";}
        outFp << "Case #" + std::to_string(i+1) + ": " + answer +"\n";
    }
    
    inFp.close();
    outFp.close();
    
    return 0;
}
