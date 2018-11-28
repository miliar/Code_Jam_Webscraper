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
    string path = "/Users/fq_bright/Desktop/A-large.in";
    string out_path = "/Users/fq_bright/Desktop/ret.txt";
    ifstream ifs;
    ofstream ofs;
    ofs.open(out_path.c_str());
    ifs.open(path.c_str());
    int T;
    string tt = "Case #";
    ifs >> T;
    int time = 1;
    while (time <= T) {
        int k;
        ifs >> k;
        string num;
        ifs >> num;
        int a[10000];
        for (int i = 0; i < k; ++i) {
            a[i] = num[i] - '0';
        }
        int sum = a[0];
        int ret = 0;
        for (int i = 1; i <= k; ++i) {
            if (i > sum) {
                ret += i - sum;
                sum += i - sum;
            }
            sum += a[i];
        }
        cout << ret << endl;
        ofs << tt;
        ofs << time++;
        ofs << ": ";
        ofs << ret << endl;
        //ofs << tt + (time++) + ": " + sum << endl;
    }
    ifs.close();
    ofs.close();
    system("pause");
}










