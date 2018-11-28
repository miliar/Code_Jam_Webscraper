/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Sid
 *
 * Created on April 9, 2016, 6:59 PM
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
vector<int> getOutput(int a_k, int a_c, int a_s);

int main(int argc, char** argv) {
    
    int nCases;
    vector<int> input_k, input_c, input_s;
    vector< vector<int> > output;

    ifstream iStream("D-small-attempt0.in");

    if (iStream.fail()) {
        cerr << "Unable to read input" << endl;
        exit(1);
    }
    
    iStream >> nCases;
    input_k.resize(nCases);
    input_c.resize(nCases);
    input_s.resize(nCases);
    output.resize(nCases);
    int iCount = 0;
    while (!iStream.eof()){
        iStream >> input_k[iCount] >> input_c[iCount] >> input_s[iCount];  
        iCount++;
    }
    
    for (int i=0; i<nCases; ++i)
    {
//        binVect = getBinaryVector(input[i]);
        output[i] = getOutput(input_k[i],input_c[i],input_s[i]);
    }
    
    
    ofstream oStream("output.txt");
    for (int i=0; i<output.size(); ++i){
        oStream << "Case #" << i+1 << ":  ";
        for (int j=0; j<output[i].size(); ++j)
        {
            oStream << (output[i])[j] << "  ";
        }
        oStream << endl;
    }

    return 0;
}

vector<int> getOutput(int a_k, int a_c, int a_s)
{
    vector<int> retVal;
    retVal.resize(a_s);
    for (int i=0; i<a_s; ++i)
    {
        retVal[i] = i+1;
    }
    return retVal;
}
