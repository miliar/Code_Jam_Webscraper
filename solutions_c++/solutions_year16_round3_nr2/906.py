//
//  main.cpp
//  pb2
//
//  Created by Rongbin Li on 5/8/16.
//  Copyright © 2016 Rongbin Li. All rights reserved.
//

#include <iostream>
#include <cassert>
#include <fstream>
#include <vector>
using namespace std;
using Lint = unsigned long long;
using Metrix = vector <vector<int> >;
ifstream fin("B-large.in");
ofstream fout("pb-large.out");

void print(const Metrix &m) {
    for (int i=0; i<m.size(); i++) {
        for (int j=0; j<m[i].size(); j++) {
            fout << m[i][j];
        }
        fout << endl;
    }
}

void printAns(int n, Lint m) {
    Metrix ans(n);
    for (int i=0; i<n; i++) {
        ans[i].resize(n, 0);
    }
    
    int k = 0;
    while ( (((Lint) 1) << k) <= m ) {
        k++;
    }
    k--;
    for (int i=0; i<=k; i++) {
        for (int j=i+1; j<=k+1; j++) {
            ans[i][j] = 1;
        }
    }
    
    for (int i=0; i<=k; i++) {
        Lint one = 1;
        if ((m & (one << i)) != 0) {
            if (i+1 != n-1) {
                ans[i+1][n-1] = 1;
            }
        }
    }
    
    print(ans);
}

int main(int argc, const char * argv[]) {
    assert(fin);
    assert(fout);
    int test;
    fin >> test;
    for (int k=1; k<=test; k++) {
        int n;
        Lint m;
        fin >> n >> m;
        fout << "Case #" << k << ": ";
        if ((((Lint) 1) << (n-2)) < m) {
            fout << "IMPOSSIBLE" << endl;
        } else {
            fout << "POSSIBLE" << endl;
            printAns(n, m);
        }
    }
    fin.close();
    fout.close();
    return 0;
}
