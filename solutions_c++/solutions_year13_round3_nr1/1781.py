//
//  main.cpp
//  CodeJam
//
//  Created by Wade Norris on 4/26/13.
//  Copyright (c) 2013 norris. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

bool nValue(string name, int n, int i, int j)
{
    int count = 0;
    for(int k=i; k<=j; k++)
    {
        if(name[k] == 'a' || name[k] == 'e' || name[k] == 'i' || name[k] == 'o' || name[k] == 'u')
        {
            count = 0;
        }
        else
        {
            count++;
            if(count>=n)
                return true;
        }
    }
        
    return false;
}

int main(int argc, const char * argv[])
{
    if(argc < 2)
        return -1;
    
    ifstream myfile;
    myfile.open(argv[1]);
    
    int numTestCases;
    myfile >> numTestCases;
    
    for(int i=0; i<numTestCases; i++)
    {
        string name;
        int n;
        
        myfile >> name;
        myfile >> n;
        
        int count = 0;
        
        for(int i=0; i<name.length()-(n-1); i++)
        {
            for(int j=i+(n-1); j<name.length(); j++)
            {
                if(nValue(name, n, i, j))
                    count++;
            }
        }
        
        cout << "Case #" << i+1 << ": " << count << endl;
    }
    
    myfile.close();
    return 0;
}

