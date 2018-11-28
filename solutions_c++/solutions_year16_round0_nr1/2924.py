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

bool check(int num, int * ans){
    if(num == 0)return false;
    set<int> all = {0,1,2,3,4,5,6,7,8,9};
    int num2 = num;
    int res = 0;
    int i = 1;
    while(!all.empty()){
        while(num2 > 0){
            auto ii = all.find(num2 % 10);
            if(ii != all.end()){
                all.erase(ii);
            }
            num2 = num2 / 10;
        }
        res = num * i;
        num2 = num * ++i;
    }
    *ans = res;
    return true;
}

int main(int argc, const char * argv[]) {
    std::ifstream infile("A-large.in");
    std::ofstream outfile("A-large.out");
    std::string line;
    std::getline(infile, line);
    int total = atoi(line.c_str());
    
    for (int i = 0; i < total; ++i){
        std::getline(infile, line);
        int a = atoi(line.c_str());
        int ans;
        bool is = check(a, &ans);
        if(is){
            outfile << "Case #" << i+1 << ": " << ans << endl;
        }else{
            outfile << "Case #" << i+1 << ": INSOMNIA" << endl;
        }
    }
}
