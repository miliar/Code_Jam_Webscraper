//
//  main.cpp
//  A
//
//  Created by Nikifor Zhao on 15/5/30.
//  Copyright (c) 2015年 Nikifor Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

char g[200][200];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};
int main(int argc, const char * argv[]) {
    int T;
    fin >> T;
    for (int ti = 1; ti <= T; ++ ti) {
        //cout << ti << endl;
        int ans = 0;
        int r, c;
        fin >> c >> r;
        for (int j = 0; j < c; j ++) {
            for (int i = 0; i < r; i ++) {
                fin >> g[i][j];
            }
        }
        int bad = 0;
        for (int i = 0; i < r; i ++) {
            for (int j = 0; j < c; j ++) {
                int x = i, y = j;
                int d = -1;
                if (g[i][j] == '.') continue;
                if (g[i][j] == '^') d = 1;
                if (g[i][j] == 'v') d = 3;
                if (g[i][j] == '<') d = 2;
                if (g[i][j] == '>') d = 0;
                //cout << d << endl;
                int f = 0;
                while(1) {
                    x += dx[d]; y += dy[d];
                    //cout << x << " " << y << endl;
                    if (x < 0 || x >= r || y < 0 || y >= c) break;
                    //cout << x << " " << y << " " << g[x][y] << endl;
                    if (g[x][y] != '.') {
                        f = 1;
                        break;
                    }
                }
                if (f == 1) continue;
                f = 0;
                for (int d = 0; d < 4; d ++) {
                    x = i; y = j;
                    while(1) {
                        x += dx[d]; y += dy[d];
                        if (x < 0 || x >= r || y < 0 || y >= c) break;
                        if (g[x][y] != '.') {
                            f = 1;
                            break;
                        }
                    }
                    if (f == 1) break;
                }
                if (f == 1) ans ++;
                else {
                    bad = 1;
                    
                }
            }
        }
        if (bad == 1) fout << "Case #" << ti << ": IMPOSSIBLE" <<endl;
        else fout << "Case #" << ti << ": " << ans  <<endl;

    }
    return 0;
}
