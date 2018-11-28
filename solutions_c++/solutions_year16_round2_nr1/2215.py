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
#include <cctype>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

string check(string s){
    return "";
}

int main(int argc, const char * argv[]) {
//    std::ifstream infile("A-small.in");
//    std::ofstream outfile("A-small.out");
    std::ifstream infile("A-large.in");
    std::ofstream outfile("A-large.out");
    std::string line;
    std::getline(infile, line);
    int total = atoi(line.c_str());

    
    for (int i = 0; i < total; ++i){
        std::getline(infile, line);
        
        vector<int> num ={0,0,0,0,0,0,0,0,0,0};
        map<char, int> m = {
            {'Z', 0},
            {'W', 0},
            {'X', 0},
            {'G', 0},
            {'S', 0},
            {'V', 0},
            {'F', 0},
            {'O', 0},
            {'R', 0},
            {'I', 0},
        };
        
        
        for(char c: line){
            if(m.find(c)!=m.end()){
                m[c]++;
            }else{
                m.insert(pair<char, int>(c, 1));
            }
        }
        num[0] = m['Z'];
        
        num[2] = m['W'];
        
        
        
        num[6] = m['X'];
        num[7] = m['S'] - num[6];
        num[5] = m['V'] - num[7];
        num[4] = m['F'] - num[5];
        num[1] = m['O'] - num[0] - num[2] - num[4];
        num[8] = m['G'];
        num[3] = m['R'] - num[4] - num[0];
        num[9] = m['I'] - num[6] - num[5] - num[8];
        
        string ans;
        
        for(int i = 0; i < 10; ++i){
            if(num[i] > 0){
                for(int j = 0; j < num[i]; j++){
                    ans.push_back('0' + i);
                }
            }
        }
        
        outfile << "Case #" << i+1 << ": " << ans << endl;
    }
}
