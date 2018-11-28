#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <stdio.h>
#include <gmp.h>
#include <cassert>
#include <cstring>

using namespace std;

bool isPalindrome(mpz_t number){
    char numString[102];
    mpz_get_str(numString, 10, number);
    unsigned int length = strlen(numString);
    for(unsigned int i = 0; i < length/2; ++i){
        if(numString[i] != numString[length-1-i]){
            return false;
        }
    }
    return true;
}

int main(){
    ifstream in;
    string inputString = "C-small-attempt0.in";
    in.open(inputString.c_str());
    int numCases;
    int numSquares;
    int low, up;
    in >> numCases;

    mpz_t lowerBound, upperBound, iter, iterSquared, upperRoot;
    mpz_init(lowerBound);
    mpz_init(upperBound);
    mpz_init(upperRoot);
    mpz_init(iter);
    mpz_init(iterSquared);
    
    for(int i = 0; i < numCases; ++i){
        numSquares = 0;
        in >> low >> up;
        mpz_set_si(lowerBound, low);//assertion
        mpz_set_si(upperBound, up);//assertion
        
        //square root lowerbound, if truncated then add one
        if(!mpz_root(iter, lowerBound, 2)){
            mpz_add_ui(iter, iter, 1);
        };
        mpz_root(upperRoot, upperBound, 2);
        while(mpz_cmp(iter, upperRoot) <= 0){
            if(isPalindrome(iter)){
                mpz_pow_ui(iterSquared, iter, 2);
                if(isPalindrome(iterSquared)){
                    ++numSquares;
                }
            }
            mpz_add_ui(iter, iter, 1);
            
        }
        
        cout << "Case #" << i+1 << ": " << numSquares << "\n";
    }

    mpz_clear(lowerBound);
    mpz_clear(upperBound);
    mpz_clear(upperRoot);
    mpz_clear(iter);
    mpz_clear(iterSquared);
    in.clear();
    in.close();
    return 0;
}
