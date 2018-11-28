//
//  main.cpp
//  CodeJam
//
//  Created by Wade Norris on 4/26/13.
//  Copyright (c) 2013 norris. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

long long sizeOfCircle(long long innerR)
{
    return ((innerR+1)*(innerR+1) - innerR*innerR);
}

int main(int argc, const char * argv[])
{
    if(argc < 2)
        return -1;
    
    ifstream myfile;
    myfile.open(argv[1]);
    
    int numTestCases;
    myfile >> numTestCases;
    
    for(int i=0; i<numTestCases; i++)
    {
        long long firstR;
        long long paintAmt;
        
        myfile >> firstR;
        myfile >> paintAmt;
        
        long long count = 0;
        long long runningAmt = 0;
        while(runningAmt <= paintAmt)
        {
            runningAmt += sizeOfCircle(firstR+count*2);
            count++;
        }
        
        cout << "Case #" << i+1 << ": " << count-1 << endl;
    }
    
    myfile.close();
    return 0;
}

