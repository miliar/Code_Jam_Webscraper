//
//  main.cpp
//  codejam
//
//  Created by Saurabh Goyal on 09/04/16.
//  Copyright © 2016 saurabhgoyal. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include <xmmintrin.h>

using namespace std;


string lastString(string str){
    vector<char> lastString;

    for (int i=0; i<str.length(); i++) {
        if (i== 0)lastString.push_back(str[0]);
        else{
            if (str[i] >= lastString[0])
                lastString.insert(lastString.begin(), str[i]);
            else
                lastString.push_back(str[i]);
        }
    }
    string str1(lastString.begin(),lastString.end());
    return str1;
}

 int main(int argc, const char * argv[]) {
 // insert code here...
     string line;
     ifstream ifile ("A-large.in-2.txt");
     ofstream ofile;
     ofile.open ("output.txt");
 
     if (ifile.is_open() && ofile.is_open())
     {
         getline (ifile,line);
         int totalCases = stoi(line);
 
         for(int i=1; getline (ifile,line) && i<=totalCases; i++)
         {
             ofile << "Case #" << i <<": " << lastString(line) << endl;
         }
         ifile.close();
         ofile.close();
     }
 
     else cout << "Unable to open file";
 
     return 0;
 }

