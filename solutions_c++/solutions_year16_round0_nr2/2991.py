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
#include <set>

using namespace std;

int check(string& num){
    if(num[num.size() - 1] == '+'){
        bool now = true;
        int res = 0;
        for(int i = (int)num.size() - 1; i >=0; --i){
            if((num[i] == '+') != now){
                now = !now;
                res++;
            }
        }
        return res;
    }else{
        bool now = false;
        int res = 1;
        for(int i = (int)num.size() - 1; i >=0; --i){
            if((num[i] == '+') != now){
                now = !now;
                res++;
            }
        }
        return res;
    }
}

int main(int argc, const char * argv[]) {
    std::ifstream infile("B-large.in");
    std::ofstream outfile("B-large.out");
    std::string line;
    std::getline(infile, line);
    int total = atoi(line.c_str());
    
    for (int i = 0; i < total; ++i){
        std::getline(infile, line);
        int ans = check(line);
        cout << "Case #" << i+1 << ": " << ans << endl;
        outfile << "Case #" << i+1 << ": " << ans << endl;
    }
}
