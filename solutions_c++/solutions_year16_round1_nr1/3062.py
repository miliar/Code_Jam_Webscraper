//
//  q1.cpp
//  CodeJam_2016
//
//  Created by Snehil Vishwakarma on 4/15/16.
//  Copyright © 2016 Indiana University Bloomington. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    int T,i,j;
    string NS;
    ifstream f1;
    f1.open("IS1_2016.in");
    ofstream f2;
    f2.open("OS1_2016.out");
    f1>>T;
    getline(f1,NS,'\n');
    for(i=0;i<T;i++)
    {
        string N;
        getline(f1,N,'\n');
        vector<char> S;
        S.push_back(N.at(0));
        for(j=1;j<N.length();j++)
        {
            if(N.at(j)>=S[0])
                S.insert(S.begin(),N.at(j));
            else
                S.push_back(N.at(j));
        }
        f2<<"Case #"<<(i+1)<<": ";
        for(j=0;j<S.size();j++)
        {
            f2<<S[j];
        }
        f2<<"\n";
    }
    f1.close();
    f2.close();
    return 0;
}