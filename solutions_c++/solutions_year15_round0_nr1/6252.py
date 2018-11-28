//
//  Ovation.cpp
//  Qualification-2015
//
//  Created by Ethan Kim on 4/11/15.
//  Copyright (c) 2015 Ethan Kim. All rights reserved.
//


#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int getFriends(int shyness[], int size);

int main(int argc, const char * argv[]) {
    
    char* filename = (char*)argv[1];
    ifstream infile(filename);

    string line;
    int caseTotal = 0, lineNum = 0;
    while (getline(infile, line))
    {
        if (lineNum == 0) {
            caseTotal = stoi(line);
        } else {
            // check input line here
            
            int size = stoi(line.substr(0,line.find_first_of(" "))) + 1;
            string charArray = line.substr(line.find_first_of(" ")+1);

            int audience[size];
            for(int idx = 0; idx < size; idx++)
            {
                audience[idx] = charArray[idx] - '0';
            }
            
            cout << "Case #" << lineNum << ": " <<  getFriends(audience, size) << endl;
        }
        lineNum++;
    }
    // check total line check here
    
    return 0;
}

int getFriends(int shyness[], int size) {
    
    int standed = 0;
    int friends = 0;
    
    for (int level = 0; level < size; ++level)
    {
        if (level > standed) {
            friends = friends + level - standed;
            standed = standed + level - standed;
        }
        standed += shyness[level];
    }
    
    return friends;
}
