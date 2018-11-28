//
//  main.cpp
//  A
//
//  Created by Jonas Blåsås Lønnum on 09.04.2016.
//  Copyright © 2016 blasas. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

void registerNumbers(bool array[], int num) {
    int tens = 1;
    while(tens <= num) {
        int index = (num / tens) % 10;
        
        //cout << endl << "INDEX: " << index << endl;
        
        array[index] = true;
        
        tens = (tens*10);
    }
}


int main(int argc, const char * argv[]) {
    
    FILE *fin = freopen("/Users/Jonas/Documents/Development/C++/CodeJam/QualRound2016/A/A/A-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("/Users/Jonas/Documents/Development/C++/CodeJam/QualRound2016/A/A/A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        
        bool numbers[10];
        
        for(int i = 0; i < 10; i++) numbers[i] = false;
        
        int N;
        cin >> N;
        
        string res = "INSOMNIA";
        string lastNumber = "";
        bool isAllTrue = false;
        int currentNumber = N;
        int prevNumber = N-1;
        
        for(int i = 1; i < 1000 && !isAllTrue && prevNumber != currentNumber; i++) {
            
            if(i > 1) {
                prevNumber = currentNumber;
            }
            
            currentNumber = (i * N);
            
            //cout << endl << endl << "CURRENT NUMBER: " << currentNumber << endl << endl;
            
            registerNumbers(numbers, currentNumber);
            
            isAllTrue = true;
            for(int j = 0; j < 10; j++) {
                if(!numbers[j]) {
                    isAllTrue = false;
                }
            }
            
            if(isAllTrue) {
                lastNumber = to_string(currentNumber);
            }
        }
        
        if(lastNumber != "") {
            res = lastNumber;
        }
        
        cout << res << endl;
    }
    //cout << "FINISH!" << endl;
    return 0;
}
