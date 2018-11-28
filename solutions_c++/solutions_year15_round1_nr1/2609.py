//
//  mushroom.cpp
//  Round1A
//
//  Created by Ethan Kim on 4/17/15.
//  Copyright (c) 2015 Ethan Kim. All rights reserved.
//

#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int getMethod2Result(int plates[], int size, int eatSpeed);

int main(int argc, const char * argv[]) {
    
    char* filename = (char*)argv[1];
    ifstream infile(filename);
    
    string line;
    int caseTotal = 0, lineNum = 0, size = 0;
    while (getline(infile, line))
    {
        if (lineNum == 0) {
            caseTotal = stoi(line);
        } else if (lineNum%2 == 1) {
            size = stoi(line);
        } else {
            // check input line here
            int plates[size];
            int method1 = 0, method2 = 0;
            int maxDiff = 0;
            
            istringstream iss(line);
            for(int idx = 0; idx < size; idx++)
            {
                iss >> plates[idx];
                if (idx > 0) {
                    if (plates[idx] < plates[idx-1]) {
                        method1 += (plates[idx-1] - plates[idx]);
                    }
                        
                    if (maxDiff < (plates[idx-1] - plates[idx])) {
                        maxDiff = (plates[idx-1] - plates[idx]);
                    }
                }
            }
            method2 = getMethod2Result(plates, size, maxDiff);
           cout << "Case #" << lineNum/2 << ": " <<  method1 << " " << method2 << endl;
       }
           lineNum++;
   }
    // check total line check here
    return 0;
}
               
int getMethod2Result(int plates[], int size, int eatSpeed) {
   
   int method2 = 0;
   
   for (int idx = 0; idx < size - 1; idx++)
   {
       if (eatSpeed > plates[idx]) {
           method2 += plates[idx];
       } else {
           method2 += eatSpeed;
       }
   }
   
   return method2;
}