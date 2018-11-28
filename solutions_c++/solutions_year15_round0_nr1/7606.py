//
//  main.cpp
//  Shyness
//
//  Created by Chris Jung on 11/04/15.
//  Copyright (c) 2015 Chris Jung. All rights reserved.
//

#include <cstdio>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    
    FILE* input, *output;
    input = fopen ("input.in","r");
    output = fopen ("output.out", "w");
    int numCases;
    char useless;
    fscanf(input, "%d", &numCases);
    fscanf(input, "%c", &useless);
    for(int i = 0; i < numCases; i++){
        int peopleNeeded = 0;
        int maxShyness;
        int peopleStanding = 0;
        fscanf(input, "%d", &maxShyness);
        fscanf(input, "%c", &useless);
        for(int j = 0; j < maxShyness + 1; j++){
            char currDigit;
            fscanf(input, "%c", &currDigit);
            int currInt = currDigit - '0';
            if(!(peopleStanding >= j)){
                peopleStanding++;
                peopleNeeded++;
            }
            peopleStanding += currInt;
        }
        fprintf(output, "Case #%d: %d\n", i + 1, peopleNeeded);
    }
    fclose(input);
    fclose(output);
    return 0;
}
