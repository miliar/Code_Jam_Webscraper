//
//  main.cpp
//  Pancakes
//
//  Created by Dylan Stenico on 09/04/16.
//  Copyright © 2016 Dylan Stenico. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define RIGHT '+'
#define WRONG '-'

int main(int argc, const char * argv[])
{
    int cases;
    string faces;
    ifstream input("/Users/dylanstenico/Documents/School/InformationTechnology/2016/GoogleCodeJam/Pancakes/B-large.in.txt");
    ofstream output("/Users/dylanstenico/Documents/School/InformationTechnology/2016/GoogleCodeJam/Pancakes/B-large.ou.txt");
    input >> cases;
    for(int i = 0; i < cases; i ++)
    {
        int changes = 0;
        input >> faces;
        
        for(int j = 0; j < faces.length() - 1; j++)
        {
            if(faces[j] != faces[j + 1])
            {
                changes++;
            }
        }
        if(faces[faces.length() -1] == WRONG)
        {
            changes++;
        }
        output << "Case #" << i + 1 << ": " << changes << endl;
        cout << "Case #" << i + 1 << ": " << changes << endl;
        
    }
}