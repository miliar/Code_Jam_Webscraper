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

int arr[26];
int total,n;

bool done() {
    for (int i=0; i<n; i++) {
        if (arr[i] != 0) {
            return true;
        }
    }
    return false;
}

int getHeightest() {
    
    int max = arr[0];
    int index = 0;
    for (int i=0; i<n; i++) {
        if (arr[i] > max) {
            max = arr[i];
            index =i;
        }
    }
   
    return index;
}

bool checkMajority(int index) {
    
    if (total == 1) {
        if (arr[index] == 1) {
            return false;
        }
        else {
            return true;
        }
    }
    
    for (int i=0; i<n; i++) {
        int num = arr[i];
        int tot = total - 1;
        if (index == i) {
            num--;
        }
        
        if (((num*100)/tot) > 50) {
            return true;
        }
    }
    return false;
}

void main2() {
    
    cin>>n;
    
    int number;
    for (int i=0; i<n; i++) {
        cin>>number;
        total += number;
        arr[i] = number;
    }

    char c;
    while (total>0) {
        int one = getHeightest();
        arr[one]--;
        total--;
        
        c = 'A'+one;
        cout<<c;
        for (int i=0; i<n; i++) {
            if (!checkMajority(i)) {
                arr[i]--;
                total--;
                c = 'A'+i;
                cout<<c;
                break;
            }
        }
        if (total != 0 ) {
            cout<<" ";
        }
    }
    
}

int main() {
    freopen("/Users/udit/Downloads/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.out", "w", stdout);
    
    int test_cases;
    
    cin>>test_cases;
    
    for (int i=1;i<=test_cases ; i++) {
        cout<<"Case #"<<i<<": ";
        main2();
        cout<<endl;
    }
    
    return 0;
}
