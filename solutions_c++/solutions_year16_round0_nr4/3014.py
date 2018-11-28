//
//  main.cpp
//  Fractiles
//
//  Created by Dylan Stenico on 10/04/16.
//  Copyright © 2016 Dylan Stenico. All rights reserved.
//
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int main(int argc, const char * argv[])
{
    
    ifstream input("/Users/dylanstenico/Documents/School/InformationTechnology/2016/GoogleCodeJam/Fractiles/D-small.in.txt");
    ofstream output("/Users/dylanstenico/Documents/School/InformationTechnology/2016/GoogleCodeJam/Fractiles/D-small.ou.txt");
    
    
    int ncases;
    input >> ncases;
    for(int i = 1; i<= ncases ; i++)
    {
        int k,c,s;
        input >> k;
        input >> c;
        input >> s;
        output << "Case #" << i <<": " ;
        
        if(c ==1 || k == 1)
        {
            output << "1 ";
        }
        for(int j = 2; j <=k; j++)
        {
            output << j <<" ";
        }
        output << endl;
    }
    return 0;
}
