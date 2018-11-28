#define _CRT_SECURE_NO_WARNINGS

#include<stack>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <fstream>
#include <istream>

using namespace std;

void main() {
    ofstream out;
    out.open("output.txt");
    //ifstream cin("B-large.in");
    //if (!cin.is_open())
        //return;

    int T;
    cin >> T;
    for (int testc = 1; testc <= T; testc++) {
        int x, r, c;
        cin >> x >> r >> c;
        
        int richard = 0;
        
        int smallside = min(r, c);

        if ((r * c) % x != 0) {
            richard = 1;
        }
        for (int i = 1; i <= x; i++) {
            if (i > smallside && x - i + 1 > smallside) {
                richard = 1;
            }
        }
        if (x > max(r, c)) {
            richard = 1;
        }

        if (x == 4 && ((r == 2 && c == 4) || (r == 4 && c == 2))) {
            richard = 1;
        }
        

        if (richard) {
            out << "Case #" << testc << ": RICHARD" << endl;
        }
        else {
            out << "Case #" << testc << ": GABRIEL" << endl;
        }
    }
}