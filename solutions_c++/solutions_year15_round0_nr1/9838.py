//
//  ovation.cpp
//  Google Code Jam
//
//  Created by Bryan Gonzales Vega on 4/11/15.
//  Copyright (c) 2015 Renovatio Technologies. All rights reserved.
//

#include <stdio.h>
#include <iostream>

using namespace std;

#define toDigit(c) (c-'0')

int requiredPeople(int maximumShy, string level){
    int people = 0;
    int accumulator = 0;
    
    for (int shynessI = 0;shynessI<=maximumShy; shynessI++) {
        int shyness = toDigit(level[shynessI]);
        if (people >= maximumShy) {
            break;
        }
        if (people < shynessI && shyness>0) {
            accumulator += shynessI-people;
            people += accumulator;
        }
        people += shyness;
    }
    
    return accumulator;
}

int main(){
    int testCases, maximumShy;
    string level;

    cin >> testCases;
    
    for (int testCase = 0; testCase < testCases; testCase++) {

        cin >> maximumShy;
        cin >> level;

        printf("Case #%d: %d\n", testCase+1, requiredPeople(maximumShy, level));
    }
    
    return 0;

}