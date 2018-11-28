//
//  main.cpp
//  Code Jam Files
//
//  Created by Viacheslav Romanov on 4/11/15.
//  Copyright (c) 2015 Viacheslav Romanov. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam Files/";

int main() {
    ifstream cin(path + "A-large.in.txt");
    ofstream cout(path + "A-large.out.txt");
    
    int T;
    cin >> T;
    for (int CT = 1;  CT <= T; CT ++) {
        cout << "Case #" << CT << ": ";
        
        int S;
        string s;
        cin >> S >> s;
        
        int res = 0, standing = 0;
        for (int i = 0; i <= S; i ++) {
            if (standing < i) {
                res += i - standing;
                standing = i;
            }
            standing += s[i] - '0';
        }
        cout << res << endl;
    }
    
    
    return 0;
}
