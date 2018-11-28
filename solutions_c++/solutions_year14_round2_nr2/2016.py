//
//  main.cpp
//  New Lottery Game
//
//  Created by Dylan Stenico on 03/05/14.
//  Copyright (c) 2014 Dylan Stenico. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

double calcolaFabbriche(int nFabbriche, double cost, double extra, double total);

int main(int argc, const char * argv[])
{
    ifstream input("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/New Lottery Game/B-small-attempt0.in.txt");
    ofstream output("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/New Lottery Game/B-small-practice.ou.txt");

    
    int cases;
    input >> cases;
    
    for(int i = 0; i < cases; i++)
    {
        int combinations = 0;
        int a, b, k;
        input >> a;
        input >> b;
        input >> k;
        
        for(int y = 0; y < k; y++)
        {
            for(int j = 0; j < a; j++)
            {
                for(int z = 0; z < b; z++)
                {
                    if((j & z) == y)
                    {
                        combinations++;
                    }
                }
            }
        }
        cout << i << endl;
        output << "Case #" << i + 1<< ": " <<combinations << endl;
    }
}