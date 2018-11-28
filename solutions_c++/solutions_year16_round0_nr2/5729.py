//
//  main.cpp
//  codejam
//
//  Created by Iulian Popescu on 09/04/16.
//  Copyright © 2016 Iulian Popescu. All rights reserved.
//

#include <fstream>
#include <vector>
#include <string>
using namespace std;

const string INPUT = "/Users/iulian_popescu/Desktop/code jam A - ok/codejam/input.in";
const string OUTPUT = "/Users/iulian_popescu/Desktop/code jam A - ok/codejam/output.in";

ifstream fin(INPUT);
ofstream fout(OUTPUT);

void solve(int T) {
    int moves = 0;
    string sequence;
    getline(fin, sequence);
    sequence += '+';
    for (int i = 0; i < sequence.size() - 1;  ++i) {
        if (sequence[i] == '-' && sequence[i+1] == '+') {
            moves += 2;
        }
    }
    if (sequence[0] == '-') {
        moves --;
    }
    fout << "Case #" << T << ": " << moves << "\n";
}

int main(int argc, const char * argv[]) {
    int T;
    fin >> T;
    string empty;
    getline(fin, empty);
    for(int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}
