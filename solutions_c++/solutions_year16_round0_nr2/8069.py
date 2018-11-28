//
//  main.cpp
//  pancake_revenge
//
//  Created by YIQI CAI on 4/9/16.
//
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int min_flip(string s)
{
    if(s.empty())
        return 0;
    
    int count = 0;
    for(int i=1; i<s.size(); i++)
    {
        if(s[i] != s[i-1])
            count++;
    }
    if(s[s.size()-1] == '-')
        count++;
    return count;
}

int main()
{
    ifstream ifile("B-large.in");
    ofstream ofile("B-large_Practice.out");
    int n_test;
    ifile >> n_test;
    for(int i=0; i<n_test; i++)
    {
        string s;
        ifile >> s;
        ofile << "Case #" << i+1 << ": " << min_flip(s) << endl;
        //cout << s <<endl;
        //cout << min_flip(s) << endl;
    }
    ofile.close();
    return 0;
}

