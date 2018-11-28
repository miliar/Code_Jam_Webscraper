//
//  main.cpp
//  CodeJam.2013.2.B
//
//  Created by Maxim Piskunov on 01.06.2013.
//  Copyright (c) 2013 Maxim Piskunov. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

class testCase {
    int logN;
    long long P;
    long long maximum;
    long long minimum;
    
public:
    long long worstPlace(long long N, long long place) {
        if (place == 0) return 0;
        long long newPlace = (place-1)/2;
        return worstPlace(N/2, newPlace) + N/2;
    }
    
    long long bestPlace(long long N, long long place) {
        return N-1 - worstPlace(N, N-1 - place);
    }
    
    void solve() {
        P -= 1;
        
        long long low = 0, high, total = 1;
        for (int i = 0; i < logN; i++) total *= 2;
        high = total - 1;
        
        while (high - low > 1) {
            long long middle = (high + low)/2;
            if (worstPlace(total, middle) <= P) low = middle;
            else high = middle;
        }
        if (worstPlace(total, high) <= P) low = high;
        else high = low;
        minimum = high;
        
        
        
        low = 0;
        high = total-1;
        
        while (high - low > 1) {
            long long middle = (high + low)/2;
            if (bestPlace(total, middle) <= P) low = middle;
            else high = middle;
        }
        if (bestPlace(total, high) <= P) low = high;
        else high = low;
        maximum = high;
    }
    
    void read(istream &in) {
        in >> logN >> P;
    }
    
    void write(ostream &out) {
        out << minimum << " " << maximum;
    }
    
};

vector <testCase> read() {
    ifstream in("input.txt");
    
    int T;
    in >> T;
    vector <testCase> tests(T);
    for (int i = 0; i < tests.size(); i++) {
        tests[i].read(in);
    }
    
    in.close();
    
    return tests;
}

void write(vector <testCase> tests)
{
    ofstream out("output.txt");
    
    for (int i = 0; i < tests.size(); i++) {
        out << "Case #" << i+1 << ": ";
        tests[i].write(out);
        if (i != tests.size()-1) out << endl;
    }
    
    out.close();
}

void solve(vector <testCase> &tests) {
    for (int i = 0; i < tests.size(); i++) {
        tests[i].solve();
    }
}

int main(int argc, const char * argv[])
{
    vector <testCase> tests = read();
    solve(tests);
    write(tests);
    return 0;
}