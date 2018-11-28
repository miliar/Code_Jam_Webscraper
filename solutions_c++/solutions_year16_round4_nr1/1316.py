//
//  main.cpp
//  CodeJam2A
//
//  Created by Maxim Piskunov on 5/28/16.
//  Copyright © 2016 Maksim Piskunov. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>

#define filename "A-large"

using namespace std;

struct input {
    int N;
    int R;
    int P;
    int S;
};

struct output {
    string lineup;
};

void read(ifstream &in, input &test) {
    in >> test.N >> test.R >> test.P >> test.S;
}

void write(ofstream &out, output test) {
    out << test.lineup;
}

vector<string> constructString(int level) {
    vector<string> result;
    result.resize(3);
    
    if (level == 0) {
        result[0] = "P";
        result[1] = "R";
        result[2] = "S";
        return result;
    }
    
    vector<string> prevResult = constructString(level - 1);
    
    result[0] = prevResult[0] + prevResult[1];
//    cout << result[0] << endl;
    result[1] = prevResult[0] + prevResult[2];
//    cout << result[1] << endl;
    result[2] = prevResult[1] + prevResult[2];
//    cout << result[2] << endl;
//    cout << endl;
    
    return result;
}

output solve (input test) {
    output result;
    
    vector<string> results = constructString(test.N);
//    cout << results[0] << endl;
//    cout << results[1] << endl;
//    cout << results[2] << endl;
    
    for (int i = 0; i < 3; i++) {
        int pCount = 0;
        int rCount = 0;
        int sCount = 0;
        for (int j = 0; j < results[i].length(); j++) {
            if (results[i][j] == 'P') pCount++;
            else if (results[i][j] == 'R') rCount++;
            else if (results[i][j] == 'S') sCount++;
        }
        if (pCount == test.P && rCount == test.R && sCount == test.S) {
            result.lineup = results[i];
            return result;
        }
    }
    
    result.lineup = "IMPOSSIBLE";
    return result;
}

void readAll(vector <input> &tests) {
    ifstream in("/Users/maxitg/Downloads/" + (string)filename + ".in.txt");
    
    int T;
    in >> T;
    tests.resize(T);
    for (int i = 0; i < T; i++) {
        read(in, tests[i]);
    }
    
    in.close();
}

void writeAll(vector <output> &results) {
    ofstream out("/Users/maxitg/Downloads/" + (string)filename + ".out.txt");
    
    out << "Case #1: ";
    write(out, results[0]);
    for (int i = 1; i < results.size(); i++) {
        out << endl << "Case #" << i+1 << ": ";
        write(out, results[i]);
    }
    
    out.close();
}

void solveAll(vector <input> &tests, vector <output> &results) {
    results.resize(tests.size());
    for (int i = 0; i < tests.size(); i++) results[i] = solve(tests[i]);
}

int main(int argc, const char * argv[]) {
    vector <input> tests;
    vector <output> results;
    
    readAll(tests);
    solveAll(tests, results);
    writeAll(results);
    
    return 0;
}