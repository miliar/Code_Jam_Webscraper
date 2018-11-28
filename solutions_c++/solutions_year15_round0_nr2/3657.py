//
//  main.cpp
//  Code Jam Files
//
//  Created by Viacheslav Romanov on 4/11/15.
//  Copyright (c) 2015 Viacheslav Romanov. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const string path = "/Users/mac/Documents/cpp/Code Jam/";

int main() {
    ifstream cin(path + "B-large.in.txt");
    ofstream cout(path + "B-large.out.txt");
    
    int T;
    cin >> T;
    for (int CT = 1;  CT <= T; CT ++) {
        cout << "Case #" << CT << ": ";
        
        int d;
        cin >> d;
        
        vector<int> p(d, 0);
        for (int i = 0; i < d; i ++) {
            cin >> p[i];
        }
        
        int res = 1000;
        for (int r = 1; r <= 1000; r ++) {
            int t = 0;
            for (int i = 0; i < p.size(); i ++)
                t += (p[i] + r - 1) / r - 1;
            
            res = min(res, t + r);
        }
        
        cout << res << endl;
    }
    
    
    return 0;
}
