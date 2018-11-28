//
//  main.cpp
//  googleJam
//
//  Created by Kevin Hon on 11/4/2015.
//  Copyright (c) 2015年 aaa. All rights reserved.
//

#include <iostream>
#include <math.h>

int findMax(int arr[], int size);
int findMaxPos(int arr[], int size);

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    //freopen(const char *, "r", "stdin");
    //freopen(<#const char *#>, "w", "stdout" );
    
    int totalCases = 0;
    std::cin >> totalCases;
    
    for (int i=0; i<totalCases; i++) {
        int needed = 0;
        int numPpl = 0;
        int counted = 0;
        
        int max = 0;
        int shyStat = 0;
        std::cin >> max;
        std::cin >> shyStat;
        
        for (int j=0; j<max+1; j++) {
            numPpl = shyStat / pow(10, max-j);
            shyStat -= numPpl * pow(10, max-j);
            
            if (j==0) {
                counted = numPpl;
                continue;
            }
            
            if (counted + needed < j) {
                needed += j-counted-needed;
            }
            
            counted += numPpl;
        }
        
        std::cout << "Case #" << i+1 <<": " << needed << "\n";
    }
    
    
    /* B. Infinite House of Pancakes
    int totalCases = 0;
    std::cin >> totalCases;
    
    for (int i=0; i<totalCases; i++) {
        int numDiner = 0;
        int * numCake;
        
        std::cin >> numDiner;
        numCake = new int[numDiner];
        
        for (int j=0; j<numDiner; j++) {
            std::cin >> numCake[j];
            
        }
        
        int steps = 0;
        int min = findMax(numCake, numDiner);
        
        while (findMax(numCake, numDiner+steps) > 2){
            
            //distribute cake
            steps++;
            int *newNumCake = new int[numDiner+steps];
            for (int k=0; k<numDiner+steps-1; k++) {
                newNumCake[k] = numCake[k];
            }
            newNumCake[numDiner+steps-1] = numCake[findMaxPos(numCake, numDiner+steps-1)]/2;
            newNumCake[findMaxPos(numCake, numDiner+steps-1)] -= newNumCake[numDiner+steps-1];
            
            numCake = newNumCake;
            
            //check if smallest steps
            if (steps+findMax(numCake, numDiner+steps) < min) {
                min = steps+findMax(numCake, numDiner+steps);
            }
            
        }
        
        std::cout << "Case #" << i+1 <<": " << min << "\n";
        
    }
     */
    
    
    return 0;
}


//for B
int findMax(int arr[], int size){
    int max = 0;
    
    for (int i=0; i<size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    return max;
}

//for B
int findMaxPos(int arr[], int size){
    
    for (int i=0; i<size; i++) {
        if (arr[i] == findMax(arr, size)) {
            return i;
        }
    }

    
    return 0;
}
