//
//  main.cpp
//  4
//
//  Created by Nikifor Zhao on 14-4-12.
//  Copyright (c) 2014年 Han Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
ifstream fin("D-small-attempt0.in");
ofstream fout("out.txt");

int t;
double a[10000], b[10000];
int mark[10000];
int main(int argc, const char * argv[])
{
    fin >> t;
    for (int ni = 0; ni < t; ni++){
        int n;
        fin >> n;
        for (int i = 0; i < n; i++) fin >> a[i];
        for (int i = 0; i < n; i++) fin >> b[i];
        sort(a, a + n);
        sort(b, b + n);
        int ans1 = 0, ans2 = 0;
        
        for (int i = 0; i < n; i++) mark[i] = 0;
        for (int i = 0; i < n; i++) {
            int found, bj;
            found = 0;
            for (int j = 0; j < n; j++) {
                if (mark[j] == 1) continue;
                if (b[j] > a[i]) {
                    found = 1;
                    bj = j;
                    break;
                }
            }
            if (found) {
                mark[bj] = 1;
            }else{
                ans2++;
                for (int j = 0; j < n; j++) {
                    if (mark[j] == 0) {
                        mark[j] = 1;
                        break;
                    }
                }
            }
        }
        
        int p = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] > b[p]){
                ans1 ++;
                p++;
            }
        }
        fout << "Case #" << ni+1 << ": " << ans1 << " " << ans2 << endl;
    }
    
    return 0;
}

