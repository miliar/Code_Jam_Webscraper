//
//  main.cpp
//  A
//
//  Created by Kotsur on 03.05.14.
//  Copyright (c) 2014 Dmytro Kotsur. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

ifstream in("/Users/userMac/Projects/Contests/Google Code Jam 2014/Round 1B/A/A/in_small.txt");
ofstream out("/Users/userMac/Projects/Contests/Google Code Jam 2014/Round 1B/A/A/out_small.txt");

int T, N;
string str;

int solve(vector<string> &s);

int main(int argc, const char * argv[])
{
    in >> T;
    for (int t = 1; t <= T; ++t) {
        in >> N;
        vector<string> s;
        s.reserve(N);
        
        for (int n = 0; n < N; ++n) {
            in >> str;
            s.push_back(str);
        }
        
        out << "Case #" << t << ": ";
        
        int result = solve(s);
        if (result == -1) {
            out << "Fegla Won" << endl;
        } else {
            out << result << endl;
        }
        
    }
    
    return 0;
}


int solve(vector<string> &s) {
    
    int result = 0;
    vector<int> pointers;
    vector<int> lengths;
    
    pointers.resize(s.size(), 0);
    lengths.resize(s.size(), 0);
    
    while (true) {
        
        // stop condition
        bool stop = true;
        for (int i = 0; i < pointers.size(); ++i) {
            stop = stop && pointers[i] == s[i].length();
        }
        
        if (stop)
            break;
        
        // check
        char ch = '\0';
        for (int i = 1; i < pointers.size(); ++i) {
            if (s[i-1][pointers[i-1]] != s[i][pointers[i]]) {
                return -1;
            } else {
                ch = s[i][pointers[i]];
            }
        }
        
        // move pointers and count lengths
        for (int i = 0; i < pointers.size(); ++i) {
            while (pointers[i] < s[i].length() && s[i][pointers[i]] == ch) {
                pointers[i]++;
                lengths[i]++;
            }
        }
        
        double avg_length = 0.0;
        for (int i = 0; i < lengths.size(); ++i) {
            avg_length += (double)lengths[i];
        }
        avg_length /= (double)lengths.size();
        
        int prec_length = round(avg_length);
        for (int i = 0; i < lengths.size(); ++i) {
            result += abs(prec_length - lengths[i]);
        }
        
        fill(lengths.begin(), lengths.end(), 0);
        
    }
    
    return result;
    
}
