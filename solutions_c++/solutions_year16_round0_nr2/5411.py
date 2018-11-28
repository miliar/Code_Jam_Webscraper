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

int arr[100];

int getFlipIndex(int length) {
    for (int i=length-1; i>=0; i--) {
        if (arr[i] == -1) {
            return i;
        }
    }
    return -1;
}

int getPositiveIndex(int index) {
    while (index >= 0) {
        if(arr[index] == 1) {
            return index;
        }
        index--;
    }
    return -1;
}

void flip(int index) {
    int start_index = 0;
    int end_index = index;
    
    while (start_index < end_index) {
        int a = arr[start_index];
        int b = arr[end_index];
        
        arr[start_index] = b * (-1);
        arr[end_index] = a * (-1);
        
        start_index++;
        end_index--;
    }
    
    if (start_index ==  end_index) {
        arr[start_index] = arr[start_index] * -1;
    }
}


int main() {

    freopen("/Users/udit/Documents/Progs/Cpp/Cpp/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.txt", "w", stdout);
    
    int test_cases;
    
    cin>>test_cases;
    
    
    for (int tc=1; tc<=test_cases; tc++) {
        
        string str;
        
        cin>>str;
        
        int length = str.length();
        
        for (int i=0; i<length; i++) {
            if (str[i] == '+') {
                arr[i] = 1;
            }
            else {
                arr[i] = -1;
            }
        }
        
        int count = 0;
        while (1) {
            int flipIndex = getFlipIndex(length);
            if (flipIndex == -1) {
                break;
            }
            if (arr[0] == 1) {
                count++;
                int postiveIndex = getPositiveIndex(flipIndex);
                flip(postiveIndex);
            }
            
            count++;
            flip(flipIndex);
        }
        
        cout<<"Case #"<<tc<<": "<<count<<endl;
    }
    
    return 0;
}
