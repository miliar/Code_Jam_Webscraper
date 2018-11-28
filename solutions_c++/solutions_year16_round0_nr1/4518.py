//
//  main.cpp
//  Counting Sheep
//
//  Created by dengjc on 16/4/9.
//  Copyright © 2016年 dengjc. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <cmath>

using namespace std;

int main(int argc, const char * argv[]) {
    ofstream ofs;
    ifstream ifs;
    ofs.open("/Users/dengjc/Desktop/A-small");
    ifs.open("/Users/dengjc/Desktop/A-small-attempt0.in");
    if (!ofs.is_open()||!ifs.is_open()) {
        cout<<"打开文件出错"<<endl;
        return 1;
    }
    
    int T;
    ifs>>T;
    
    for (int i=1; i<=T; i++) {
        set<int> digits;
        int N;
        ifs>>N;
        int base = N;
        if (N==0) {
            ofs<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        
        while (digits.size()!=10) {
            string num = to_string(base);
            size_t len = num.length();
            for (int j=0; j<len; j++) {
                digits.insert(num[j]);
            }
            base += N;
        }
        ofs<<"Case #"<<i<<": "<<base - N<<endl;
    }
    return 0;

}
