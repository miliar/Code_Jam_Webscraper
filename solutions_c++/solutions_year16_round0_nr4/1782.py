//
// Created by Yuxiang LI on 09/04/16.
//
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int T;
int K,C,S;

int main(){
    ifstream in("D.in");
    ofstream out("output.out");
    in >> T;
    for(int cases = 1; cases <= T; cases++){
        in >> K >> C >> S;
        if (C*S < K){
            out << "Case #" << cases << ": IMPOSSIBLE" << endl;
            continue;
        }
        out << "Case #" << cases << ":";
        if (C == 1){
            for(int i = 1; i <= K; i++)
                out << ' ' << i;
            out << endl;
            continue;
        }
        long long current = 1;
        bool allmaped = false;
        while(!allmaped){
            long long t = current;
            for(int i = 1; i < C; i++){
                current++;
                allmaped = (current >=K);
                current = current > K ? 1:current;
                t = (t-1)*K+current;
            }
            out << ' ' << t;
        }
        out << endl;
    }
    in.close();
    out.close();
    return 0;
}

