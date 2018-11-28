//
//  main.cpp
//  Magic Tric
//
//  Created by Kotsur on 12.04.14.
//  Copyright (c) 2014 Dmytro Kotsur. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <set>

int T;
int q1, q2;
int m1[4][4], m2[4][4];


using namespace std;

void solve();

ifstream in("/Users/userMac/Projects/Contests/Google Code Jam 2014/Qualification_Round/Magic Tric/google_test.txt");
ofstream out("/Users/userMac/Projects/Contests/Google Code Jam 2014/Qualification_Round/Magic Tric/out.txt");

int main(int argc, const char * argv[])
{
    
    in >> T;
    for (int t = 1; t <= T; ++t) {
        in >> q1;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                in >> m1[i][j];
            }
        }
        in >> q2;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                in >> m2[i][j];
            }
        }
        
        out << "Case #" << t << ": ";
        solve();
        
    }
    
    return 0;
}

void solve() {
    
    set<int> cards;
    for (int i = 0; i < 4; ++i) {
        cards.insert(m1[q1-1][i]);
    }
    
    int index = 0;
    int count = 0;
    set<int>::iterator it;
    for (int i = 0; i < 4; ++i) {
        it = cards.find(m2[q2-1][i]);
        if (it != cards.end()) {
            count++;
            index = *it;
        }
    }
    if (count == 0) {
        out << "Volunteer cheated!" << endl;
    } else if (count == 1) {
        out << index << endl;
    } else {
        out << "Bad magician!" << endl;
    }
}

