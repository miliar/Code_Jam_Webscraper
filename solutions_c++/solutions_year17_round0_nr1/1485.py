//
//  1.cpp
//  gcj_Qualification
//
//  Created by didi on 2017/4/8.
//  Copyright © 2017年 didi. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream in("/Users/didi/Desktop/gcj_Qualification/gcj_Qualification/A-large.in");
ofstream out("/Users/didi/Desktop/gcj_Qualification/gcj_Qualification/A-large.out");

void rev(string &str, int s, int k){
    for (int i = 0; i < k; i++){
        if (str[s+i] == '+'){
            str[s+i] = '-';
        }else{
            str[s+i] = '+';
        }
    }
}

int check(string str, int k){
    int ret = 1;
    for (int i = str.length() - k; i < str.length(); i++){
        if (str[i] == '-'){
            ret = 0;
            break;
        }
    }
    return ret;
}

void solve(int test){
    string str;
    int K;
    in >> str >> K;
    int sum = 0;
    for (int i=0; i <= str.length() - K; i++){
        if (str[i] == '+'){
            continue;
        }else{
            sum += 1;
            rev(str,i,K);
        }
    }
    out << "Case #" << test << ": ";
    if (check(str, K)){
        out << sum << endl;
    }else{
        out << "IMPOSSIBLE" << endl;
    }
}

int main(int argc, const char * argv[]) {
    int test = 0,T;
    in >> T;
    while (test++<T){
        solve(test);
    }
    in.close();
    out.close();
    return 0;
}
