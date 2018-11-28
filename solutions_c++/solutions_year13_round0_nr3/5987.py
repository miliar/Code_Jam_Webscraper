//
//  fairAndSquare.cpp
//  Test
//
//  Created by Aya on 4/13/13.
//  Copyright (c) 2013 Aya. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <cmath>
#include <sstream>

using namespace std;

template <typename T>

string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}


int main ()
{
    ifstream infile ("C-small-attempt0.in");
    ofstream outfile("output.out");
    
    int T;
    infile>> T;
    
    for (int i=0; i < T ; i++)
    {
        int A, B;
        infile >> A >> B;
        int j = A;
        int fairAndSquareCounter = 0;
        double sqRoot = sqrt(j);
        double intCheck = floor(sqRoot);
        double fraction = modf(sqRoot, &intCheck);
        if ( fraction != 0)
            j = (int)pow(ceil(sqRoot),2);
        while (j <= B){
            double sqRoot = sqrt(j);
            string pCheck = NumberToString(j);
            string reverse = string ( pCheck.rbegin(), pCheck.rend() );
            
            string pSRCheck = NumberToString(sqRoot);
            string sqRootReverse = string ( pSRCheck.rbegin(), pSRCheck.rend() );
            
            if (pCheck == reverse && pSRCheck == sqRootReverse)
                fairAndSquareCounter++;
            j = j + ((2*sqRoot)+1);
        }
        int counter = i + 1;
        outfile << "Case #"<<counter<<": "<<fairAndSquareCounter<<"\n";
    }
    
    return 0;
}