/* 
 * File:   main.cpp
 * Author: tbporter
 *
 * Created on April 13, 2013, 2:16 AM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>

using namespace std;



//returns if it's a palindrome, reverses the number then compares to itself
bool isPal(unsigned long long *num){
    unsigned long long temp = *num;
    unsigned long long rev = 0;
    int d;
    while(temp>0){
        d = temp % 10;
        rev = rev * 10 + d;
        temp = temp /10;
    }
    return *num == rev;
}

//returns if it's a square, also saves the square in the parameter's address
bool isSquare(unsigned long long *num){
    float f =sqrt(*num);
    *num = sqrt(*num);
    if(*num==f)
        return true;
    return false;
}

int main(int argc, char** argv) {
    string line;
    int tests;
    unsigned long long lowerLim,upperLim,temp;
    std::ifstream inFile("C-small-attempt0.in");
    std::ofstream oFile("out");
    
    inFile >> line;
    
    tests = atoi(line.c_str());
    for(int curTest = 0; curTest < tests; curTest++ ){
        int count = 0;
        inFile >> line;
        lowerLim = atoi(line.c_str());
        inFile >> line;
        upperLim = atoi(line.c_str());
        for(;lowerLim<upperLim+1;lowerLim++){
            if(isPal(&lowerLim)){
                temp = lowerLim;
                if(isSquare(&temp)){
                    if(isPal(&temp)){
                        count++;
                    }
                }
            }
        }
        oFile << "Case #" << curTest+1 << ": " << count << "\n";
    }
    
    return 0;
}

