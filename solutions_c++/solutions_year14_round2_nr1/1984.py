//
//  main.cpp
//  contest
//
//  Created by xianran on 5/4/14.
//  Copyright (c) 2014 xianran. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

struct Rec {
    char c;
    int len;
};

int main(int argc, const char * argv[])
{
    int ntest;

    ofstream fout;
    ifstream fin;
    fout.open("/Users/xianran/Desktop/result.txt", ios::out);
    fin.open("/Users/xianran/Desktop/in.txt", ios::in);
    
        fin >> ntest;
    

    
    for (int nt = 1; nt <= ntest; nt++) {
        char sents[100+1][200] = {};
        Rec recs[100+1][100+1];
        int nRec[100+1] = {0};
        int N;
        fin >> N;
        for (int i = 0; i < N; i++) {
            fin >> sents[i];
            cout << sents[i] << endl;
        }
        for (int i = 0; i < N; i++) {
            int m = 1;
            recs[i][0].c = sents[i][0];
            recs[i][0].len = 1;
            for (int j = 1; j < strlen(sents[i]); j++) {
                if (sents[i][j] == sents[i][j-1])
                    recs[i][m-1].len++;
                else {
                    recs[i][m].c = sents[i][j];
                    recs[i][m].len = 1;
                    m++;
                }
            }
            nRec[i] = m;
        }
        
        int sum = 0;
        int step = 0;
        for (int i = 0; i < N; i++)
            sum += nRec[i];
        if (sum == nRec[0] * N) {
            for (int i = 0; i < nRec[0]; i++) {
                double sum2 = recs[0][i].len;
                for (int j = 1; j < N; j++) {
                    if (recs[j][i].c != recs[0][i].c) {
                        step = -1;
                        goto failed;
                    } else {
                        sum2 += recs[j][i].len;
                    }
                }
                sum2 /= N;
                int intsum = round(sum2);
                for (int j = 0; j < N; j++) {
                    step += abs(recs[j][i].len - intsum);
                }
            }
        } else {
            step = -1;
        }
        
        cout << nt << endl;
        
    failed:
        fout << "Case #" << nt << ": ";
        if (step < 0) {
            fout << "Fegla Won" << endl;
        } else
            fout << step << endl;
    }
    
    fout.close();
    return 0;
}

