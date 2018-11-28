//
//  main.cpp
//  CodeJam2
//
//  Created by Wade Norris on 4/12/13.
//  Copyright (c) 2013 norris. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <locale>
#include <sstream>
#include <math.h>
using namespace std;

bool isPalindrome(int number)
{
    ostringstream convert;
    convert << number;
    string str = convert.str();
    
    int i = 0;
    int j = static_cast<int>(str.length()) - 1;
    
    while(i < j)
    {
        if(str[i] != str[j])
            return false;
        i++;
        j--;
    }
    
    return true;
}

int main (int argc, char* argv[]) {
    string line;
    ifstream myfile (argv[1]);
    
    if (!myfile.is_open())
    {
        cout << "Error opening file!" << endl;
        return 0;
    }
    
    getline (myfile,line);
    
    int numTestCases = atoi(line.c_str());
    
    cout << "Num tests: " << numTestCases << endl;
    
    for(int i=0; i<numTestCases; i++)
    {
        int high;
        int low;
        
        myfile >> low;
        myfile >> high;
        
        myfile.ignore(10000, '\n');
        
        int count = 0;
        
        for(int j=ceil(sqrt(low)); j<=floor(sqrt(high)); j++)
            if(isPalindrome(j) && isPalindrome(j*j))
                count++;
        
        cout << "Case #" << i+1 << ": " << count << endl;
     
    }
    
    myfile.close();
    
    return 0;
}


