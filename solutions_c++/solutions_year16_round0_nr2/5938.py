//
//  main.cpp
//  Pancake
//
//  Created by YOUQingfei on 4/10/16.
//  Copyright © 2016 YOUQingfei. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int T;
vector<string> cakes;

void LoadFromFile();
void Compute(string s, int i);

int main(int argc, const char * argv[]) {
    LoadFromFile();
    int len =  (int) cakes.size();
    for (int i = 0; i < len ; ++i)
    {
        Compute(cakes[i], i+1);
    }
    return 0;
}

void LoadFromFile()
{
    cin >> T;
    string s;
    for (int i = 0 ; i < T; ++i)
    {
        cin >> s;
        cakes.push_back(s);
    }
}

void Compute (string s , int i )
{
    int len = (int) s.size();
    int count = 0;
    for (int i = 1; i < len; ++i)
    {
        if (s[i-1] != s[i]) count++;
    }
    
    if (((s[0] == '-') && (count & 1) == 0)
        || ((s[0] == '+') && ((count & 1) == 1))) count++;

    
    cout << "Case #" << i << ": " << count << endl;
}
