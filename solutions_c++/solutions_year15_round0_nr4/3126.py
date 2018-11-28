//
//  main.cpp
//  Problem1
//
//  Created by Varun Mohan on 4/11/15.
//  Copyright (c) 2015 VarunMohan. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

string winner(int X, int R, int C) {
    if (X==1){
        return "GABRIEL";
    }
    if (X==2) {
        return ((R*C)%2==0) ? "GABRIEL" : "RICHARD";
    }
    if (X==3) {
        if ((R*C)%3!=0) {
            return "RICHARD";
        }
        if (R==1 || C==1) {
            return "RICHARD";
        }
        return "GABRIEL";
    }
    if ((R*C)%4!=0) {
        return "RICHARD";
    }
    if (R<4 && C<4) {
        return "RICHARD";
    }
    if (R==1 || C==1) {
        return "RICHARD";
    }
    if (R*C == 8) {
        return "RICHARD";
    }
    return "GABRIEL";
}

int main(int argc, const char * argv[]) {
    int T;
    ofstream fout;
    fout.open("D-small-attempt1.out");
    ifstream fin;
    fin.open("D-small-attempt1.in");
    fin >> T;
    for (int i=0; i<T; i++) {
        int X, R, C;
        fin>>X>>R>>C;
        fout<<"Case #"<<i+1<<": "<<winner(X,R,C)<<endl;
    }
}