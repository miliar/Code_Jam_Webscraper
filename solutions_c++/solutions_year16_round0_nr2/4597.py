//
//  main.cpp
//  RevengePancakes
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
#include <bitset>

using namespace std;

int main(int argc, const char * argv[]) {
    ofstream ofs;
    ifstream ifs;
    ofs.open("/Users/dengjc/Desktop/B-small");
    ifs.open("/Users/dengjc/Desktop/B-small-attempt0.in");
    if (!ofs.is_open()||!ifs.is_open()) {
        cout<<"打开文件出错"<<endl;
        return 1;
    }
    
    int T;
    ifs>>T;
    
    for (int i=1; i<=T; i++) {
        bitset<100> bset;
        
        string s;
        ifs>>s;
        size_t len = s.length();
    
        for (int j=0; j<len; j++) {
            if (s[j] == '+') {
                bset.set(j);
            }
        }
        
        int result = 0;
        while (bset.count()!=len) {
            if (bset.test(0)) {
                int pos = 0;
                int endpos = len;
                for (int j=0; j<len; j++)
                {
                    if (!bset.test(j)) {
                        pos=j;
                        break;
                    }
                }
                
                for (int j=pos; j<len; j++)
                {
                    if (bset.test(j)) {
                        endpos=j;
                        break;
                    }
                }
                
                for (int j=pos; j<endpos; j++) {
                    bset.flip(j);
                }
                result+=2;

            } else {
                int endpos = len;
                for (int j=0; j<len; j++)
                {
                    if (bset.test(j)) {
                        endpos=j;
                        break;
                    }
                }
                
                for (int j=0; j<endpos; j++) {
                    bset.flip(j);
                }
                result++;
            }
            
        }
        ofs<<"Case #"<<i<<": "<<result<<endl;
    }
    
    return 0;
}
