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

struct Num{
    unsigned long long num;
    unsigned long long dividers[9];
};

unsigned long long find_div(unsigned long long n){
    
    unsigned long long square_root = sqrt(n); // use math.h
    unsigned long long toggle = 0;
    for(unsigned long long i = 2; i <= square_root; i++){
        if(n%i==0){
            toggle = i;
            break;
        }
    }
    
    if(toggle == 0)
        return 0;
    else
        return toggle;
    
}

bool check(Num & n){
    unsigned long long test_num[9] = {0};
    test_num[0] = n.num;
    for(int i = 3; i <= 10; ++i){
        unsigned long long nn = n.num;
        unsigned long long unit = 1;
        while(nn > 0){
            if (nn & 0b1)
                test_num[i - 2] += unit;
            nn = nn >> 1;
            unit = unit * i;
        }
    }
    for(int i = 0; i < 9; ++i){
        unsigned long long a;
        a = find_div(test_num[i]);
        if(a == 0){
            return false;
        }else{
            n.dividers[i] = a;
        }
    }
    
    return true;
}

void printn(Num & n, std::ofstream& f){
    unsigned long long nn = n.num;
    string res;
    while(nn > 0){
        if (nn & 0b1)
            res = "1" + res;
        else
            res = "0" + res;
        nn = nn >> 1;
    }
    cout << res << " ";
    f << res << " ";
    for (int i = 0; i < 9; ++i){
        cout << n.dividers[i] << " ";
        f << n.dividers[i] << " ";
    }
    cout << endl;
    f << endl;
}

int main(int argc, const char * argv[]) {
    std::ifstream infile("C-small.in");
    std::ofstream outfile("C-small.out");
    std::string line;
    std::getline(infile, line);
    int total = atoi(line.c_str());
    
    for (int i = 0; i < total; ++i){
        std::getline(infile, line);
        
        int count, digits;
        sscanf(line.c_str(), "%d %d", &digits, &count);
        
        unsigned long long num = 0b1;
        
        num = num << (digits - 1);
        ++num;
        
        vector<Num> res;
        
        
        while(res.size() < count){
            Num n;
            n.num = num;
            if(check(n)){
                res.push_back(n);
            }
            num += 0b10;
        }
        
        cout << "Case #1:\n";
        outfile << "Case #1:\n";
        
        for(Num n: res)
            printn(n, outfile);
    }
}
