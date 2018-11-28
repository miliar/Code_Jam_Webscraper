//
//  lastOne.cpp
//  OmerQureshi
//
//  Created by Hamza Arshad on 12/04/2015.
//  Copyright (c) 2015 Hamza Arshad. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;


int abs(int a, int b, int c)
{
    
    if(b == 1 && c==1)
    {
        return 1;
    }
    else if((b == 1 && c==2) || (b == 2 && c==1))
    {
        return 1;
    }
    else if((b == 1 && c==3) || (b == 3 && c==1))
    {
        return 0;
    }
    else if((b == 1 && c==4) || (b == 4 && c==1))
    {
        if(a==2)
            return 1;
        else
            return 0;
    }
    else if(b == 2 && c==2)
    {
        if(a == 2)
            return 1;
        else
            return 0;
    }
    else if((b == 2 && c==3) || (b == 3 && c==2))
    {
        if(a==2 || a==3)
            return 1;
        
    }
    else if((b == 2 && c==4) || (b == 4 && c==2))
    {
        if(a==2)
            return 1;
        else if(a == 4)
            return 0;
    }
    else if(b == 3 && c==3)
    {
        if(a==3)
            return 1;
    }
    else if((b == 3 && c==4)||(b == 4 && c==3))
    {
        return 1;
    }
    
    return 1;
}

int main()
{
    ifstream fin("file.in");
    if(!fin)
        return 1;
    
    ofstream fout("file.out");
    if(!fout)
        return 1;
    
    int total = 0;
    fin>>total;
    for(int i=1; i<=total; i++)
    {
        fout<<"Case #"<<i<<": ";
        
        int a,b,c;
        fin>>a;
        fin>>b;
        fin>>c;
        
        int st = b*c;
        if(a==1)
        {
            fout<<"GABRIEL"<<endl;
            continue;
        }
        if(st%a != 0)
        {
            fout<<"RICHARD"<<endl;
            continue;
        }
        
        int ab = abs(a,b,c);
        
        if(ab == 0)
            fout<<"RICHARD"<<endl;
        else
            fout<<"GABRIEL"<<endl;
        
    }
    
    return 0;
}
