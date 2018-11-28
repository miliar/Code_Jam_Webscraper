//
//  main.cpp
//  codejam
//
//  Created by Alexandru Grigoroi on 12/04/2014.
//  Copyright (c) 2014 Alexandru Grigoroi. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[])
{
    int t;
    cin>>t;
    int n;
    int rows[4][4];
    int good[2][4];
    for(int qw =1;qw<=t;qw++) {
        for(int q=0;q<2;q++) {
            cin>>n;
            for(int i=0;i<4;i++)
                for(int j=0;j<4;j++) {
                    cin>>rows[i][j];
                    if(i+1 == n)
                        good[q][j] = rows[i][j];
            }
        }
        vector<int> matches;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(good[0][i] == good[1][j])
                    matches.push_back(good[0][i]);
        cout<<"Case #"<<qw<<": ";
        if(matches.size() == 0)
            cout<<"Volunteer cheated!\n";
        else if(matches.size() == 1)
            cout<<matches[0]<<'\n';
        else
            cout<<"Bad Magician!\n";
    }
}

