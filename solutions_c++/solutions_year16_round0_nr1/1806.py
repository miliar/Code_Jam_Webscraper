//
//  main.cpp
//  CodeJam2016Qualification-A
//
//  Created by Michael Walker on 4/8/16.
//  Copyright © 2016 Michael Walker. All rights reserved.
//

#include <iostream>
#include <fstream>

int array[10];

bool checkArray();
void clearArray();

int main(int argc, const char * argv[]) {
    freopen("/Users/Michael/Desktop/A-large.in", "r", stdin);
    std::ofstream out("/Users/Michael/Desktop/output");
    
    
    int T;
    int N;
    int tempN;
    int caseNum = 1;
    int index;
    bool done;
    scanf("%i", &T);
    
    while(T--) {
        scanf("%i", &N);
        out << "Case #" << caseNum++ << ": ";
        index = 1;
        
        if (N == 0) {
            out << "INSOMNIA\n";
            continue;
        }
        
        while (1) {
            tempN = N * index;
            
            while (tempN != 0) {
                array[tempN % 10] = 1;
                tempN /= 10;
            }
            
            if (checkArray()) {
                break;
            }
            index++;
        }
        
        
        out << N * index << "\n";
        clearArray();
    }
    
    
    out.close();
    return 0;
}

bool checkArray() {
    for (int i = 0; i < 10; ++i) {
        if (array[i] == 0) {
            return false;
        }
    }
    return true;
}

void clearArray() {
    for (int i = 0; i < 10; ++i) {
        array[i] = 0;
    }
}