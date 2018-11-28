//
//  main.cpp
//  Codeforces
//
//  Created by Taygrim on 20.03.13.
//  Copyright (c) 2013 Taygrim. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
    ifstream cin("B-large.in.txt");
    ofstream cout("output.txt");
    long t;
    cin>>t;
    
    for(long qq=0; qq<t; qq++)
    {
        long n, m;
        cin>>n>>m;
        vector<vector<long> > mass(n, vector<long>(m,0));
        
        for(long i=0; i<n; i++)
            for(long j=0; j<m; j++)
                cin>>mass[i][j];
        
        vector<vector<bool> > cut(n, vector<bool> (m, false));
        
        for(long k=1; k<=100; k++)
            for(long i=0; i<n; i++)
                for(long j=0; j<m; j++)
                    if (mass[i][j] == k)
                    {
                        bool flag1 = true;
                        for(long q=0; q<m; q++)
                            if(mass[i][q] != k && !cut[i][q])
                            {
                                flag1 = false;
                                break;
                            }
                        if(flag1)
                            for(long q=0; q<m; q++)
                                cut[i][q] = true;
                        
                        flag1 = true;
                        for(long q=0; q<n; q++)
                            if(mass[q][j] != k && !cut[q][j])
                            {
                                flag1 = false;
                                break;
                            }
                        
                        if(flag1)
                            for(long q=0; q<n; q++)
                                cut[q][j] = true;

                    }
        
        bool flag = true;
        
        for(long i=0; i<n; i++)
            for(long j=0; j<m; j++)
                if(!cut[i][j])
                    flag = false;
        
        if(flag)
            cout<<"Case #"<<qq+1<<": "<<"YES\n";
        else
            cout<<"Case #"<<qq+1<<": "<<"NO\n";
        
    }
}

















