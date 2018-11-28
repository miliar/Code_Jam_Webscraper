//
//  main.cpp
//  gcj
//
//  Created by Anoop Ramachandra Hallur on 4/17/15.
//  Copyright (c) 2015 anoop. All rights reserved.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <inttypes.h>
#include <string>
#include <fstream>

#define MIN(a,b) (((a)<(b))?(a):(b))

using namespace std;


int main(int argc, const char * argv[]) {
    // insert code here...
    string path = "/afs/andrew.cmu.edu/usr15/ahallur/Workspace/gcj/gcj/";
    string file = path + "A-small-attempt0.in";
    string outfile = path + "A-small-attempt0.out";
    ifstream fs(file, ios::in);
    ofstream ofs(outfile, ios::out);
    int T,N,i,j,t, fr, sr, diff, max;
    vector<int> list;
    fs >> T;
    for(i = 1; i <= T ; i++){
        fs >> N;
        fr = 0; sr = 0;max = 0;
        list.clear();
        for(j = 0 ; j < N ; j++){
            fs >> t;
            list.push_back(t);
        }
        for(j = 1 ; j < N ; j++){
            diff = list[j-1]-list[j];
            if(diff > max)max = diff;
            if(diff > 0)
                fr += diff;
        }

        for(j = 0 ; j < N -1 ; j++){
            sr += MIN(max, list[j]);
        }
        ofs << "Case #" << i << ": " << fr << " " << sr << endl;

    }
    fs.close();
    ofs.close();
    return 0;
}