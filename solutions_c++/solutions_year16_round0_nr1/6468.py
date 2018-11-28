//
//  main.cpp
//  CountingSheep
//
//  Created by 강대원 on 2016. 4. 9..
//  Copyright © 2016년 강대원. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int coutingSheep(int N) {
    int i, j, n;
    int bFlag = 0;
    n = N;
    bool complete = false;
    string strNum;
    for (i = 1; i <= 100; i++) {
        strNum = to_string(n);
        for (j = 0; j < strNum.length(); j++) {
            bFlag = bFlag | (1 << (strNum[j] - '0'));
        }
        if (bFlag == 1023) {
            complete = true;
            break;
        } else {
            n = N * (i + 1);
        }
    }
    if (complete) return n;
    else {
        return -1;
    }
}

int main(int argc, const char * argv[]) {
    ifstream in("input.in");
    ofstream out("output.out");
    int T, N, i, result;
    in >> T;
    for (i = 0; i < T; i++) {
        in >> N;
        out << "Case #" << i + 1 << ": ";
        result = coutingSheep(N);
        if (result == -1) {
            out << "INSOMNIA";
        } else {
            out << result;
        }
        out << endl;
    }
    return 0;
}
