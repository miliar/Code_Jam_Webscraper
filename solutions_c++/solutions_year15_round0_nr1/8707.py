//
//  main.cpp
//  CodeJam
//
//  Created by William Balance on 11/04/2015.
//  Copyright (c) 2015 William Balance. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int test(0);
    string two;
    int amis(0);
    int one(0);
    int nbPersonne(0);
    int tab[100];
    
    cin >> test;
    
    for (int i(0); i < test; i++)
    {
        cin >> one >> two;
        
        amis = 0;
        nbPersonne = 0;
        
        for (int j(0); j < one; j++)
        {
            nbPersonne+= two[j] - 48;
            
            if (nbPersonne < j+1)
            {
                amis++;
                nbPersonne++;
                
            }
            
        }
        tab[i] = amis;
    }
    
    for (int i(0); i < test; i++)
    {
        cout << "Case #" << i+1 << ": " << tab[i] << endl;
    }
    
    return 0;
}
