//
//  ProblemB.cpp
//  GoogleCodeJam
//
//  Created by Luan Nguyen on 4/9/16.
//  Copyright © 2016 Luan Nguyen. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

char flip(char c)
{
    return c == '-' ? '+' : '-';
}

void flip(string& S, int to)
{
    for (int i = 0, j = to; i <= j; ++i, j--)
    {
        char u = flip(S[j]);
        char v = flip(S[i]);
        
        S[i] = v;
        
        if (i != j)
            S[j] = u;
    }
}

int solve(string s)
{
    int res = 0;
    
    int end = (int)s.length() - 1;
    while (end >= 0)
    {
        int index = end;
        while (index >= 0 && s[index] == '+')
            index--;
 
        if (index < 0)
            break;
        
        int start = 0;
        while (s[start] == '+')
            start++;
        if (start > 0)
        {
            res++;
            flip(s, start-1);
        }
        
        res++;
        flip(s, index);
        
        end = index;
    }
    
    return res;
}

int main()
{
    ofstream outFile;
    outFile.open("/users/superkinhluan/documents/Xcode projects/GoogleCodeJam/GoogleCodeJam/b-large.out", ios::out);
    
    ifstream inFile;
    inFile.open("/users/superkinhluan/documents/Xcode projects/GoogleCodeJam/GoogleCodeJam/b-large.in", ios::in);
    
    int T;
    inFile >> T;
    
    for (int i = 1; i <= T; ++i)
    {
        string N;
        inFile >> N;
        
        auto res = solve(N);
        //cout << res << endl;
        outFile << "Case #" << i << ": " << res << endl;
    }
    
    outFile.close();
    inFile.close();
    
    cout << "Success";

    return 0;
}