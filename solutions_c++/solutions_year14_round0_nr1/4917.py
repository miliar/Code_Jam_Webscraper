//
//  main.cpp
//  1
//
//  Created by Nikifor Zhao on 14-4-12.
//  Copyright (c) 2014年 Han Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("A-small-attempt3.in");
ofstream fout("out.txt");
int t[17] = {0};
int g[4][4];
int main(int argc, const char * argv[])
{

    int n;
    fin >> n;
    for (int ni = 0; ni < n; ni++){
        for (int i = 0; i < 17; i++) t[i] = 0;
        int a;
        fin >> a;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) fin >> g[i][j];
        }
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (i == a - 1) t[g[i][j]] ++;
            }
        }
        fin >> a;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) fin >> g[i][j];
        }
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (i == a - 1) t[g[i][j]] ++;
            }
        }
        int c = 0, ans = -1;
        for (int i = 0; i < 17; i++) {
            if (t[i] == 2) {
                c ++;
                ans = i;
            }
        }
        fout << "Case #" << ni + 1 << ": ";
        if (c == 1) fout << ans << endl;
        else if (c >= 2) fout << "Bad magician!" << endl;
        else fout << "Volunteer cheated!" << endl;
    }
    return 0;
}

