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
#include <unistd.h>

using namespace::std;

int arr[10];

bool allFound() {
    for (int i=0; i<10; i++) {
        if(arr[i] == 0) {
            return false;
        }
    }
    return true;
}

void reset() {
    for (int i=0; i<10; i++) {
        arr[i] = 0;
    }
}

int main() {
    
    freopen("/Users/udit/Documents/Progs/Cpp/Cpp/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.txt", "w", stdout);
    
    int test_cases;
    
    cin>>test_cases;
    
    for (int tc=1; tc<=test_cases; tc++) {
        long long int number;
        cin>>number;
        
        if (number == 0) {
            cout<<"Case #"<<tc<<": INSOMNIA"<<endl;
            continue;
        }
        
        reset();
        
        long long int total = number;
        long long int temp_total;
        
        while (1) {
            temp_total = total;
            while (temp_total > 0) {
                arr[(temp_total%10)] = 1;
                temp_total = temp_total/10;
            }
            if (allFound()) {
                break;
            }
            total = total + number;
        }
        cout<<"Case #"<<tc<<": "<<total<<endl;
    }
    
    return 0;
}
