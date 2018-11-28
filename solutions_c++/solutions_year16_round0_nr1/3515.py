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

ifstream fin("A-large.in.txt");
ofstream fout("output.txt");

int T;
long long int N;
bool digit[10];

bool findDigit(long long int K) {
    while (K!=0) {
        digit[K%10]=1;
        K/=10;
    }
    bool all=1;
    for (int i=0; i<10; i++) all=(all && digit[i]);
    return all;
}

int main() {
    fin>>T;
    for (int i=0; i<T; i++) {
        cout<<"Running: "<<i+1<<endl;
        fill(digit,digit+10,0);
        fin>>N;
        if(N==0) {
            fout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }
        long long int limit=pow(2,62)/N;
        for (long long int j=1;; j++) {
            if(findDigit(j*N)) {
                fout<<"Case #"<<i+1<<": "<<j*N<<endl;
                break;
            }
            if (j==limit) {
                fout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
                break;
            }
        }
        
    }
}