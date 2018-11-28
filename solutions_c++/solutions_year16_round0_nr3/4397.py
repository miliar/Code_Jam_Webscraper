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

int arr[50];
int divv[11];
int length;
int j;

void printDiv() {
    for (int i=2; i<11; i++) {
        cout<<divv[i];
        if (i != 10) {
            cout<<" ";
        }
    }
}

bool primeNumber(int baseIndex, long long int number) {
    int square_root = sqrt(number);
    for (int i=2; i<=square_root; i++) {
        if (number%i == 0) {
            divv[baseIndex] = i;
            return false;
        }
    }
    return true;
}

bool checkForALL() {
    
    for (int i=2; i<=10; i++) {
        long long int number = 0;
        
        for (int j=length-1;j>=0;j--) {
            number += arr[j]*pow(i, length-1-j);
        }
        
        if (primeNumber(i, number)) {
            return false;
        }
    }
    return true;
}

void incToArr(long long int inc) {
    int l = length-2;
    while (inc > 0) {
        if (inc & 1) {
            arr[l] = 1;
        }
        else {
            arr[l] = 0;
        }
        inc >>= 1;
        l--;
    }
}

int main() {
    
    freopen("/Users/udit/Documents/Progs/Cpp/Cpp/input.in", "r", stdin);
    freopen("/Users/udit/Downloads/output.txt", "w", stdout);
    
    int test_cases;
    
    cin>>test_cases;
    
    cout<<"Case #1:"<<endl;
    
    cin>>length>>j;
    
    arr[0] = 1;
    arr[length-1] = 1;
    
    for (int i=1; i<length-1; i++) {
        arr[i] = 0;
    }
    
    long long int incrementor = 0;
    
    int i=0;
    while (i<j) {
        if(checkForALL()) {
            i++;
            for (int k=0; k<length; k++) {
                cout<<arr[k];
            }
            cout<<" ";//<<divisors;
            printDiv();
            cout<<endl;
        }
        incrementor++;
        incToArr(incrementor);
    }
    
    return 0;
}
