//
//  main.cpp
//  Code_Jam_2015
//
//  Created by Tony on 4/11/15.
//  Copyright (c) 2015 Tony. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
using std::string;
class Solution {
public:
    int standing_ovation(int smax, string s) {
        int ans = 0;
        int cnt = 0;
        for (int i = 0; i < smax; i++) {
            int t0 = (int)(s[i] - '0');
            if (cnt + t0 < i + 1) {
                ans += i + 1 - (cnt + t0);
                cnt += i + 1 - (cnt + t0);
            }
            cnt += t0;
        }
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    
    int t;
    Solution a;
    ifstream infile;
    ofstream outfile;
    infile.open ("/Users/Tony/Desktop/input.txt");
    outfile.open ("/Users/Tony/Desktop/output.txt");
    infile >> t;
    for (int i = 0; i < t; i++) {
        int sm;
        string str;
        infile >> sm >> str;
        outfile << "Case #" << i+1 << ": " <<a.standing_ovation(sm, str) << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
