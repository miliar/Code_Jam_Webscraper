//
//  main.cpp
//  AlgorithmStudy
//
//  Created by 김태우 on 2015. 12. 30..
//  Copyright © 2015년 김태우. All rights reserved.
//

#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cassert>

using namespace std;

void test();
void solve(ifstream& infile, ofstream& outfile);

int main(int argc, const char * argv[]) {
    string line;
    ifstream infile ("/Users/ted/Downloads/B-large.in.txt");
//    ifstream infile ("/Users/ted/Downloads/test.in.txt");
    if (infile.is_open()) {
        ofstream outfile;
        outfile.open("/Users/ted/Downloads/out.txt");
        solve(infile, outfile);
        outfile.close();
        infile.close();
    } else {
        cout << "Unable to open file";
    }
    return 0;
}

void flip(string& str, int endidx) {
    for (int a=0; a<=endidx/2; a++) {
        if (a == endidx-a) {
            if (str[a] == '+') {
                str[a] = '-';
            } else {
                str[a] = '+';
            }
        } else {
            char left = str[a];
            char right = str[endidx-a];
            if (left == '+') {
                str[endidx-a] = '-';
            } else {
                str[endidx-a] = '+';
            }
            if (right == '+') {
                str[a] = '-';
            } else {
                str[a] = '+';
            }
        }
    }
}

/**
 * Problem B. Revenge of the Pancakes
 * https://code.google.com/codejam/contest/6254486/dashboard#s=p1
 */
void solve(ifstream& infile, ofstream& outfile){
    string line;
    getline(infile, line);
    stringstream ss(line);
    int T;
    ss >> T;
    for (int a=0; a<T; a++) {
        getline(infile, line);
        int res = 0;
        int end = (int)line.length() - 1;
        while (res < 1000) {
            while (end >= 0 && line.at(end) == '+') { // 우측에 +는 제외
                end--;
            }
            if (end < 0) {
                break;
            }
            // 남은영역(우측에 -)에서,
            if (line.at(0) == '-') {
                // 좌측에 -면, 전체 flip
                flip(line, end);
            } else {
                // 좌측에 +면, 우측에 연속 +수가 최대인 상태까지 탐색후, flip
                int maxcnt = 0;
                int maxidx = 0;
                int cnt = 0;
                for (int b=0; b<=end; b++) {
                    if (line.at(b) == '+') {
                        cnt++;
                        if (cnt > maxcnt) {
                            maxcnt = cnt;
                            maxidx = b;
                        }
                    } else {
                        cnt = 0;
                    }
                }
                flip(line, maxidx);
            }
            res++;
        }
        assert(res < 1000);
        cout << "Case #" << (a+1) << ": " << res << endl;
        outfile << "Case #" << (a+1) << ": " << res << endl;
    }
}