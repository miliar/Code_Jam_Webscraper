//
//  main.cpp
//  GoogleJam
//
//  Created by Isira Samarasekera on 3/13/16.
//  Copyright (c) 2016 Isira Samarasekera. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

bool allPositive(vector<char>& c)
{
    for(int i=0; i < c.size(); i++)
    {
        if(c[i] !='+')
            return false;
    }
    return true;
}

void flip(vector<char>& c)
{
    char previous = c[0];
    int i= 1;
    for(; i < c.size(); i++)
    {
        if(previous != c[i])
        {
            break;
        }
    }
    
    for(int j = 0 ; j < i; j++)
    {
        c[j]== '+' ? c[j]= '-' : c[j]= '+';
    }
}

int RangeOfPancakes(string s)
{
    int f = 0;
    int size =s.size();
    vector<char> c;
    for(int i= 0; i < size; i++)
    {
        c.push_back(s[i]);
    }
    while(!allPositive(c) )
    {
        flip(c);
        f++;
    }
    return f;
    
}


int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream in("/Users/isira/Documents/B-large.in");
    ofstream out("/Users/isira/Documents/B-small-practice.out");
    string line;
    getline(in, line);
    
    int nTests =0;
    nTests = stoi(line);
    for(int i= 0; i < nTests; i++)
    {
        getline(in, line);
        
        
        out<<"Case #"<<i+1 <<": "<<RangeOfPancakes(line);
        out<<endl;

    }

    in.close();
    out.close();

    return 0;
}
