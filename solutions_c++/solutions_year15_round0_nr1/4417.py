//
//  SaleItem.cpp
//  OmerQureshi
//
//  Created by Hamza Arshad on 07/04/2015.
//  Copyright (c) 2015 Hamza Arshad. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    ifstream fin("/Users/pyschoCoder/A-large.in.txt");
    if(!fin)
        return 1;
    
    ofstream fout("/Users/pyschoCoder/output2.txt");
    if(!fout)
        return 1;
    
    int total = 0;
    fin>>total;
    for(int i=1; i<=total;i++)
    {
        fout<<"Case #"<<i<<": ";
        
        int sMax=0;
        string kase = "";
        
        fin>>sMax;
        fin>>kase;
        int f=false;
        int count = 0;
        int tot = 0;
        for(int i=0; i<kase.length(); i++)
        {
            tot += (kase[i]-48);
            if(kase[i] == '0' && tot <= i)
            {
                tot++;
                count++;
            }
        }
        
        fout<<count<<endl;
    }
    
    return 0;
}
