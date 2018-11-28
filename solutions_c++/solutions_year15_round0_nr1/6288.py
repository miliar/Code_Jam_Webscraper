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

int main(int argc, const char * argv[]) {
    int T;
    ofstream fout;
    fout.open("A-large.out");
    ifstream fin;
    fin.open("A-large.in");
    
    fin >> T;
    for (int i=0; i<T; i++) {
        int N;
        string s;
        fin >> N >> s;
        int arr[N+1];
        for (int j=0; j<N+1; j++) {
            arr[j] = s[j]-'0';
        }
        int cursum = arr[0];
        int added = 0;
        for (int j = 1; j<N+1; j++) {
            if (cursum < j && arr[j] != 0) {
                added += j - cursum;
                cursum=j;
            }
            cursum += arr[j];
        }
        fout<<"Case #"<<i+1<<": "<<added<<endl;
    }
    return 0;
}
