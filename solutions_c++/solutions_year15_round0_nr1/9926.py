//
//  main.cpp
//  cj1
//
//  Created by Paranj Nimeshbhai Soni on 4/10/15.
//  Copyright (c) 2015 Paranj. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int maxs = 0;
    int inv =0;
    int ova = 0;
    int cases = 0;
    string shy;
    
   
    cin>>cases;
    
    for(int k = 0 ; k<cases; k++)
    {
        ova = 0;
        inv = 0;
        maxs = 0;
        shy = "";
    cin>>maxs;
    cin>>shy;
    int *array = new int[shy.length()];
    
    for(int i = 0; i<shy.length(); i++)
    {
        array[i] = (int)shy[i] - 48;
    }
    
    
    for(int i = 0; i<shy.length(); i++)
    {
        if(ova + inv >= i)
        {
            ova += array[i];
           
        }
        
        else
        {
            inv += (i - ova - inv);
            ova += array[i];
        }
        
    }
    
    cout<<"Case #"<<k+1<<": "<<inv<<endl;
    }
    
    return 0;
}
