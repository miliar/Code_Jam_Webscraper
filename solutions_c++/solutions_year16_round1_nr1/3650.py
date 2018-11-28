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
#include <algorithm>
#include <set>

using namespace std;

string check(string s){
    string res;
    
    for(char c:s){
        if(res.size() == 0){
            res = res + c;
        }else{
            if(c >= res[0]){
                res = c + res;
            }else{
                res = res + c;
            }
        }
    }
    return res;
}

int main(int argc, const char * argv[]) {
    std::ifstream infile("A-large.in");
    std::ofstream outfile("A-large.out");
    std::string line;
    std::getline(infile, line);
    int total = atoi(line.c_str());
    
    for (int i = 0; i < total; ++i){
        std::getline(infile, line);
        
        string ans = check(line);
        outfile << "Case #" << i+1 << ": " << ans << endl;
    }
}
