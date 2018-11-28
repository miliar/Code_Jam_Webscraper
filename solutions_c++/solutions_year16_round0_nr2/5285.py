//
//  main.cpp
//  codejam2016A
//
//  Created by Daniel Pompe on 09.04.16.
//  Copyright © 2016 DP. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    FILE *fin = freopen("test.in", "r", stdin);
    FILE *fout = freopen("test.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        string s;
        cin >> s;
        bool good = s[0] == '+';
        int turns = 0;
        for(int i = 1; i<s.length(); ++i)
        {
            const char& c = s[i];
            if(good && c == '+')
                continue;
            if(!good && c == '-')
                continue;
            else
            {
                turns++;
                good = !good;
            }
        }
        if(!good)
            turns++;
        
        cout << turns << endl;
    }
    exit(0);
}
