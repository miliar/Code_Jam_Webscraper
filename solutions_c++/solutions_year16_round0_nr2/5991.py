/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Sid
 *
 * Created on April 9, 2016, 5:00 AM
 */

#include <cstdlib>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <numeric>

using namespace std;

/*
 * 
 */

int getOutput(string a_binVect);

int main(int argc, char** argv) {

    int nCases;
    vector<string> input;
    vector<int> output,binVect;

    ifstream iStream("B-large.in");

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
   
    for (int i=0; i<nCases; ++i)
    {
//        binVect = getBinaryVector(input[i]);
        output[i] = getOutput(input[i]);
    }
    
    ofstream oStream("output.txt");
    for (int i=0; i<output.size(); ++i){
        oStream << "Case #" << i+1 << ":  "<< output[i] << endl;
    }
  
    return 0;
}

int getOutput(string a_in)
{
    int nFlips = 0;
    string temp = a_in;
    std::reverse(temp.begin(),temp.end());
    for (int index=0; index<temp.size(); ++index)
    {
        if (temp.size() == 1)
        {
            (temp[index] == '-') ? nFlips = 1 : nFlips = 0;
        }
        else 
        {
           if (index != (temp.size() - 1))
           {
               if(temp[index] == '-' && nFlips == 0)
               {
                   nFlips+=1;
               }
               if(temp[index] != temp[index+1])
               {
                   nFlips+=1;
               }       
           }
        }
    }
    return nFlips;
}
