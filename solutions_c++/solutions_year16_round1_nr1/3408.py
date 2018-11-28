//
//  main.cpp
//  Cpp
//
//  Created by Udit on 5/12/15.
//  Copyright (c) 2015 Udit. All rights reserved.
//

#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <stack>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <unistd.h>

using namespace::std;

void main2() {
    string str;
    cin>>str;
    
    string new_str = "";
    char c;
    c = str[0];
    new_str += c;
    for (int i=1; i<str.length(); i++) {
        if(str[i]<c) {
            new_str = new_str + str[i];
        }
        else {
            new_str = str[i] + new_str;
        }
        c = new_str[0];
    }
    cout<<new_str<<endl;
}

int main() {
    freopen("/Users/udit/Downloads/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.out", "w", stdout);
    
    int test_cases;
    
    cin>>test_cases;
    
    for (int i=1;i<=test_cases ; i++) {
        cout<<"Case #"<<i<<":";
        main2();
    }
    
    return 0;
}
