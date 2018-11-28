//
//  main.cpp
//  2013 - Qual - Fair and Square
//
//  Created by Pontus Ahlqvist on 4/13/13.
//  Copyright (c) 2013 Pontus Ahlqvist. All rights reserved.
//
//  By simply multiplying out a palindrome you can see that without carrying, the result is alway a palindrome. Thus we must find when carrying occurs. In
//  particular, the largest column equals \sum d_i ^2 where d_i is the ith digit. We thus find that we can have at most 10 digits and also at most two 2s and no
//  3s unless that three is by itself. The first few roots are thus 1, 2, 3, 11, 111, 121, 1111, 1221, 11111, 12121, ... with squares 1, 4, 9, 121, 12321, and so on.
//  We can easily enumerate the roots.

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int power(int base, int exp){
    if(exp == 0) return 1;
    int halfPower = power(base,exp/2);
    if(exp%2 == 0) return halfPower*halfPower;
    return base*halfPower*halfPower;
}

int main(){
    ifstream inputFile("C-small-attempt0.in");
    ofstream outputFile("googleCodeJamOUTPUTsmall.txt");
    int numExamples;
    inputFile >> numExamples;
    vector<long> roots;
    
    roots.push_back(1);
    roots.push_back(2);
    roots.push_back(3);
    int baseValue = 11;
    int numDigits = 2;
    while(numDigits < 10){
        //no 2s
        roots.push_back(baseValue);
        
        //One 2 in the middle only if odd number of digits. E.g. 11211 = 11111 + 10^2
        if(numDigits%2 == 1 && numDigits + 3 < 10){
            roots.push_back(baseValue + power(10,numDigits/2));
        }
        
        //The 2s symmetrically around center. Only if numdigits+6 < 10, i.e. only the numbers 22 and 212.
        if(baseValue == 11) roots.push_back(22);
        if(baseValue == 111) roots.push_back(212);
        
        //increment baseValue and numDigits
        baseValue *= 10;
        baseValue += 1;
        numDigits++;
    }
    //now square these to get the palindromes we're interested in.
    vector<long> palindromes;
    for(int i = 0; i < roots.size(); i++) palindromes.push_back(roots[i]*roots[i]);
    
    for(int i = 0; i < numExamples; i++){
        int A, B;
        inputFile >> A;
        inputFile >> B;
        int count = 0;
        //simply go through the palindromes and check if they are within range
        for(int j = 0; j < palindromes.size(); j++){
            if(palindromes[j] >= A && palindromes[j] <= B) count++;
        }
        outputFile << "Case #" << i+1 << ": " << count << endl;
    }
    return 0;
}

