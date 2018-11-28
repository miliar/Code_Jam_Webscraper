//
//  main.cpp
//  problem_1
//
//  Created by Vansh Pahwa on 4/4/15.
//  Copyright (c) 2015 Vansh Pahwa. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>

using namespace std;
int max(int a,int b)
{
    if (a<b) return b; else return a;
}
int main()
{
    int TT;int highest_shyness;string s;
    ifstream fin("/Users/vansh/Desktop/input.txt");
    ofstream fout("/Users/vansh/Desktop/ans.txt");
    fin>>TT;

    for (int j=1;j<=TT;j++)
    {
        fin>>highest_shyness;
        fin>>s;
        int ans=0,cumulative =0;
        for (int i=0;i<highest_shyness+1;i++)
        {
            
            ans=max(ans,i-cumulative);
            cumulative = cumulative + (s[i]-48);
        }
        fout<<"Case #"<<to_string(j)<<": "<<ans<<"\n";
    }
}
