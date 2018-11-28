//
//  main.cpp
//  codejam
//
//  Created by Iulian Popescu on 09/04/16.
//  Copyright © 2016 Iulian Popescu. All rights reserved.
//

#include <fstream>
#include <vector>
#include <set>
using namespace std;

const string INPUT = "/Users/iulian_popescu/Desktop/codejam/codejam/input.in";
const string OUTPUT = "/Users/iulian_popescu/Desktop/codejam/codejam/output.in";

ifstream fin(INPUT);
ofstream fout(OUTPUT);

void solve(int T) {
    int n = 0;
    set<long long> usedNumbers;
    vector<bool> found(10, false);
    int digitsFound = 0;
    bool finished = false;
    fin >> n;
    long long actualN = n;
    usedNumbers.insert(n);
    while (!finished) {
        long long x = actualN;
        while (x > 9) {
            int digit = x % 10;
            if(!found[ digit] ) {
                found[digit] = true;
                digitsFound ++;
                if (digitsFound == 10) {
                    finished = true;
                }
            }
            x /= 10;
        }
        
        if(x < 10) {
            if(!found[x] ) {
                found[x] = true;
                digitsFound ++;
                if (digitsFound == 10) {
                    finished = true;
                }
            }
        }
        
        if(!finished) {
            actualN += n;
            if (usedNumbers.find(actualN) != usedNumbers.end()) {
                finished = true;
            } else {
                usedNumbers.insert(actualN);
            }
        }
    }
    
    if (digitsFound != 10) {
        fout << "Case #" << T << ": INSOMNIA\n";
    } else {
        fout << "Case #" << T << ": " << actualN << "\n";
    }
}

int main(int argc, const char * argv[]) {
    int T;
    fin >> T;
    for(int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}
