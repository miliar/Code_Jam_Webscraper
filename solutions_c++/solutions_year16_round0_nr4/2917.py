//
//  model.cpp
//  
//
//  Created by Luca Arnaboldi on 13/04/15.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>

using namespace std;

ifstream fin("D-small-attempt0.in.txt");
ofstream fout("output.txt");

int T,K;

int main() {
    fin>>T;
    for (int i=1; i<=T; i++) {
        fin>>K>>K>>K;
        fout<<"Case #"<<i<<":";
        for (int i=1; i<=K; i++) fout<<" "<<i;
        fout<<endl;
    }
}