//
//  main.cpp
//  Test
//
//  Created by Abhiraj Khare on 4/9/16.
//  Copyright © 2016 Abhiraj Khare. All rights reserved.
//

#include <iostream>
using namespace std;

void flip(string &str, int end, char ch);

int main() {
    int T;
    cin>>T;
    string S;
    for(int testCase=0; testCase<T; testCase++)
    {
        int flipCount = 0;
        cin>>S;
        for(int i=0; i<S.length()-1; i++)
        {
            if(S[i] != S[i+1])
            {
                flip(S, i, S[i+1]);
                flipCount++;
            }
        }
        
        int ascii = S[S.length()-1];
        if(ascii == 45)
            flipCount++;
        
        cout<<"Case #"<<testCase+1<<": "<<flipCount<<endl;
    }
    return 0;
}

void flip(string &str, int end, char ch)
{
    for(int i=0; i<end; i++)
    {
        str[i] = ch;
    }
}
