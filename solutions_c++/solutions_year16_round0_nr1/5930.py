/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Sid
 *
 * Created on April 9, 2016, 1:26 AM
 */

#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

/*
 * 
 */
int getOutput(int a_input);
vector<int> getDigits(int a_in);

int main(int argc, char** argv) {

    int nCases;
    vector<int> input,output;

    ifstream iStream("A-large.in");

    if (iStream.fail()) {
        cerr << "Unable to read input" << endl;
        exit(1);
    }
    
    iStream >> nCases;
    input.resize(nCases);
    output.resize(nCases);
    int iCount = 0;
    while (!iStream.eof()){
        iStream >> input[iCount];  
        iCount++;
    }

   
   for (int i=0; i<input.size(); ++i){
        output[i] = getOutput(input[i]);
    }

  
    ofstream oStream("output.txt");
    for (int i=0; i<output.size(); ++i){
        if (output[i] == 0){
            oStream << "Case #" << i+1 << ":  "<< "INSOMNIA" << endl;
        }
        else {
            oStream << "Case #" << i+1 << ":  "<< output[i] << endl;
        }
        
    }
    return 0;
}

int getOutput(int a_in)
{
    if (a_in == 0) return 0;
    int retVal = a_in;
    vector<int> target;
    vector<int> digits;
    int iCount = 1;
    digits = getDigits(retVal);
    target.push_back(digits[0]);

    
    for (int i=1; i < digits.size(); ++i)
    {
        if (std::find(target.begin(), target.end(), digits[i]) == target.end())
        {
            target.push_back(digits[i]);
        }
    }

    int iSize = target.size();
    while (true)
    {
        iCount++;
        retVal = iCount*a_in;
        digits = getDigits(retVal);
        
        for (int i=0; i < digits.size(); ++i)
        {
            if (std::find(target.begin(), target.end(), digits[i]) == target.end())
            {
                target.push_back(digits[i]);
            }
        }
        if (target.size() >= 10 || iCount >= 100) break;
    }
    if (iCount <=100) return retVal;
    else return 0;
}

vector<int> getDigits(int a_in)
{
    vector<int> digits;
    for(; a_in > 0; a_in/=10) digits.push_back(a_in%10);
    std::reverse(digits.begin(),digits.end());
    return digits;
}