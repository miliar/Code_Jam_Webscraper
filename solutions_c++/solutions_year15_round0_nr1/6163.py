//
//  main.cpp
//  CodeJamA
//
//  Created by Calin Bindea on 11/04/15.
//  Copyright (c) 2015 siphongific. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int GetMaxFriends(const string &shiness)
{
    int currentUp = 0,
        extraNeeded = 0;
    for (int i = 0; i < shiness.size(); i++)
    {
        if (shiness[i] == '0')
            continue;
        if (currentUp < i)
        {
            extraNeeded += (i - currentUp);
            currentUp = i;
        }
        currentUp += shiness[i] - '0';
    }
    return extraNeeded;
}

int main(int argc, const char * argv[])
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for (int i = 0; i < T; i++)
    {
        int sz;
        fin >> sz;
        string shiness;
        fin >> shiness;
        fout << "Case #" << i << ": " << GetMaxFriends(shiness) << endl;
    }
    fout.close();
    fin.close();
    return 0;
}

