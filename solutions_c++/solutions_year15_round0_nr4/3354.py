#include <algorithm>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <queue>
#include <vector>

using namespace std;
typedef unsigned int u32;

int main() {
	ios_base::sync_with_stdio(false);
    ifstream fin("D-small-attempt0.in");
    ofstream fout("omino.out");
    u32 t;
    fin >> t;
    for (u32 i = 1; i <= t; i++) {
        u32 x, r, c;
        fin >> x >> r >> c;
        string winner;
        //make rows always >= cols
        if (c > r) {
            u32 temp = c;
            c = r;
            r = temp;
        }
        if ((r * c) % x == 0) {
            if (x == 1 || x == 2) {
                winner = "GABRIEL";
            } else if (x == 3) {
                if (c == 1) {
                    winner = "RICHARD";
                } else if (c == 2) {
                    if (r == 3) {
                        winner = "GABRIEL";
                    } else {
                        winner = "RICHARD";
                    }
                } else if (c == 3) {
                    winner = "GABRIEL";
                } else {
                    winner = "RICHARD";
                }
            } else {
                if (c == 1 || c == 2) {
                    winner = "RICHARD";
                } else {
                    winner = "GABRIEL";
                }
            }
        } else {
            winner = "RICHARD";
        }
        fout << "Case #" << i << ": " << winner << '\n';
    }
    return 0;
}