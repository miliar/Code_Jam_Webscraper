//
//  main.cpp
//  t2
//
//  Created by Jasper Jia on 13-4-13.
//  Copyright (c) 2013年 Jasper Jia. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[])
{
    int T;
    int n, m;
    int valid = 2;
    int a[100][100];
    ifstream fin("/Volumes/Documents/t2/t2/B-large.in");
    ofstream fout("/Volumes/Documents/t2/t2/B-large.out");
    fin >> T;
    for (int i=0; i<T; i++) {
        for(int r = 0;r<100;r++)
            for(int c = 0;c<100;c++)
                a[r][c] = 0;
        fin>>n>>m;
        for(int r = 0;r<n;r++)
            for(int c = 0;c<m;c++)
                fin >> a[r][c];
        
        valid = 2;
        for(int r = 0;r<n && valid;r++){
            for(int c = 0;c<m && valid;c++){
                valid = 2;
                int t = a[r][c];
                if(t > 100) valid = 0;
                for(int rr = 0;rr<n;rr++) if(a[rr][c] > t) {valid --; break;}
                for(int cc = 0;cc<m;cc++) if(a[r][cc] > t) {valid --; break;}
            }
        }
        if(valid) fout<<"Case #"<<i+1<<": YES\n";
        else fout<<"Case #"<<i+1<<": NO\n";
    }
    return 0;
}

