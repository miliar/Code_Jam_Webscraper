//
//  main.cpp
//  r1bp1
//
//  Created by Raymond Tse on 4/30/16.
//  Copyright © 2016 Raymond Tse. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;


int main(int argc, const char * argv[]) {
    std::ifstream inFp(argv[1]);
    
    if (!inFp.is_open())
    {
        fprintf(stderr, "Can't open the file");
        exit(1);
    }
    
    std::ofstream outFp("out.txt");
    
    int numInputs;
    std::string n;
    vector<string> english = {"ZERO","TWO","FOUR","SIX","EIGHT","ONE","THREE","FIVE","SEVEN","NINE"};
    map<string,int> letterToNum = {{"ZERO",0},{"ONE",1},{"TWO",2},{"THREE",3},{"FOUR",4},{"FIVE",5},{"SIX",6},{"SEVEN",7},{"EIGHT",8},{"NINE",9}};
    
    inFp >> numInputs;
    
    for (int i = 0; i < numInputs; i++)
    {
        std::vector<int> nums = {0,0,0,0,0,0,0,0,0,0};
        inFp >> n;
        string tempname = n;
        sort(tempname.begin(), tempname.end());
        int eIndex = 0;
        while (true) {
            vector<int> indicies = {};
            string temp = tempname;
            for (auto c: english[eIndex]) {
                int loc = temp.find(c);
                if (loc != -1) {
                    temp[loc] = '.';
                    indicies.push_back(loc);
                } else {
                    break;
                }
            }
            if (indicies.size() == english[eIndex].length()) {
                nums[letterToNum[english[eIndex]]]++;
                for (auto c: indicies) {
                    tempname[c] = '_';
                }
            } else {
                eIndex++;
            }
            if (eIndex >= 10) { break;}
        }
        string answer = "";
        for (int z = 0; z < 10; z++) {
            for (int y = 0; y < nums[z];y++) {
                answer.append(to_string(z));
            }
        }
        outFp << "Case #" + std::to_string(i+1) + ": " + answer +"\n";
    }
    
    inFp.close();
    outFp.close();
    
    return 0;
}

