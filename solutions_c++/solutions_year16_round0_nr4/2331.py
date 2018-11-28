//
//  main.cpp
//  c
//
//  Created by hyspace on 4/8/16.
//  Copyright © 2016 hyspace. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;


int main(int argc, const char * argv[]) {
    std::ifstream infile("D-small-attempt0.in");
    std::ofstream outfile("D-small-attempt0.out");
    std::string line;
    std::getline(infile, line);
    int total = atoi(line.c_str());
    
    for (int i = 0; i < total; ++i){
        std::getline(infile, line);
        
        int K, C, S;
        sscanf(line.c_str(), "%d %d %d", &K, &C, &S);
        
        outfile << "Case #" << i+1 << ": ";
        for (int j = 1; j <= S; ++j){
            outfile << j << " ";
        }
        outfile << endl;
    }
}
