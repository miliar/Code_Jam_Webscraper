//
//  main.cpp
//  codejam
//
//  Created by Iulian Popescu on 16/04/16.
//  Copyright © 2016 Iulian Popescu. All rights reserved.
//

#include <fstream>
#include <deque>
#include <vector>
using namespace std;

ifstream fin("/Users/iulian_popescu/Desktop/codejam/codejam/input.in");
ofstream fout("/Users/iulian_popescu/Desktop/codejam/codejam/output.out");


void solve(int t) {
    string s;
    fin >> s;
    string sCopy = string(s);
    int val[10];
    for (int i = 0; i < 10; ++i) {
        val[i] = 0;
    }
    for (int i = 0; i < sCopy.length() && s.length() > 0; ++i) {
        if (sCopy[i] == 'Z') { // handle zero
            s.erase(s.begin() + s.find('Z'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('R'));
            s.erase(s.begin() + s.find('O'));
            val[0]++;
        } else if (sCopy[i] == 'W') { //handle two
            s.erase(s.begin() + s.find('T'));
            s.erase(s.begin() + s.find('W'));
            s.erase(s.begin() + s.find('O'));
            val[2]++;
        } else if (sCopy[i] ==  'X') { //handle si
            s.erase(s.begin() + s.find('S'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('X'));
            val[6]++;
        } else if(sCopy[i] == 'G'){ //handle eight
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('G'));
            s.erase(s.begin() + s.find('H'));
            s.erase(s.begin() + s.find('T'));
            val[8]++;
        }
    }
    sCopy = string(s);
    for (int i = 0; i < sCopy.length() && s.length() > 0; ++i) {
        if (sCopy[i] == 'T') { // handle three
            s.erase(s.begin() + s.find('T'));
            s.erase(s.begin() + s.find('H'));
            s.erase(s.begin() + s.find('R'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('E'));
            val[3]++;
        } else if (sCopy[i] == 'S') { //handle seven
            s.erase(s.begin() + s.find('S'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('V'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('N'));
            val[7]++;
        }
    }
    
    sCopy = string(s);
    for (int i = 0; i < sCopy.length() && s.length() > 0; ++i) {
        if (sCopy[i] == 'V') { // handle five
            s.erase(s.begin() + s.find('F'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('V'));
            s.erase(s.begin() + s.find('E'));
            val[5]++;
        }
    }
    
    sCopy = string(s);
    for (int i = 0; i < sCopy.length() && s.length() > 0; ++i) {
        if (sCopy[i] == 'F') { // handle four
            s.erase(s.begin() + s.find('F'));
            s.erase(s.begin() + s.find('O'));
            s.erase(s.begin() + s.find('U'));
            s.erase(s.begin() + s.find('R'));
            val[4]++;
        }
    }
    
    sCopy = string(s);
    for (int i = 0; i < sCopy.length() && s.length() > 0; ++i) {
        if (sCopy[i] == 'O') { // handle one
            s.erase(s.begin() + s.find('O'));
            s.erase(s.begin() + s.find('N'));
            s.erase(s.begin() + s.find('E'));
            val[1]++;
        }
    }

    sCopy = string(s);
    for (int i = 0; i < sCopy.length() && s.length() > 0; ++i) {
        if (sCopy[i] == 'N') { // handle nine
            s.erase(s.begin() + s.find('N'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('N'));
            s.erase(s.begin() + s.find('E'));
            val[9]++;
        }
    }

    fout << "Case #" << t << ": ";
    for (int i = 0; i < 10; ++i) {
        for (int j = 1; j <= val[i]; ++j) {
            fout << i;
        }
    }
    fout << "\n";
}

int main(int argc, const char * argv[]) {
    int t;
    fin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
