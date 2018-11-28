//
//  main.cpp
//  codejam
//
//  Created by fq_bright on 10/4/15.
//  Copyright (c) 2015 fq_bright. All rights reserved.
//

#include <iostream>
#include <vector>
#include <utility>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main() {
    string path = "/Users/fq_bright/Desktop/C-small-attempt0.in";
    string out_path = "/Users/fq_bright/Desktop/ret.txt";
    ifstream ifs;
    ofstream ofs;
    ofs.open(out_path.c_str());
    ifs.open(path.c_str());
    int T;
    string tt = "Case #";
    ifs >> T;
    int time = 1;
    int map[5][5] = {{},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};  //1->1, i->2, j->3, k->4
    while (time <= T) {
        int L, X;
        ifs >> L >> X;
        if (X > 20) X = 20 + X%4;
        string str;
        ifs >> str;
        bool ret = false;
        int now = 1;
        int nowFinding = 2;
        for (int i = 0; i < X; ++i) {
            for (int j = 0; j < str.length(); ++j) {
                int p = 2;
                if (str[j] == 'j') p = 3;
                else if (str[j] == 'k') p = 4;
                int tmp = map[abs(now)][p];
                if (now < 0) now = -tmp;
                else now = tmp;
                if (nowFinding != -1 && now == nowFinding) {
                    if (nowFinding == 2)
                        nowFinding = 4;
                    else nowFinding = -1;
                }
            }
        }
        if (now == -1 && nowFinding == -1)
            ret = true;
        ofs << tt;
        ofs << time++;
        ofs << ": ";
        if (ret)
        ofs << "YES" << endl;
        else ofs << "NO" << endl;
        //ofs << tt + (time++) + ": " + sum << endl;
    }
    ifs.close();
    ofs.close();
    system("pause");
}










