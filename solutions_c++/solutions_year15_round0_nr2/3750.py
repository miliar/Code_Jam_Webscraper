//
//  main.cpp
//  Code_Jam_2015
//
//  Created by Tony on 4/11/15.
//  Copyright (c) 2015 Tony. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;
using std::string;
class Solution {
public:

    int infinite_house(int d, vector<int> p, int mx) {
        
        int ans = mx;
        int cnt;
        for (int i = 1; i <= mx; i++) {
            cnt = i;
            for (int j = 0; j < d; j++) {
                if (p[j] > i) {
                    if (p[j]%i) cnt += p[j]/i;
                    else        cnt += (p[j]/i - 1);
                    
                }
            }
            if (cnt < ans) ans = cnt;
        }
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    
    int t;
    Solution a;
    FILE *fin, *fout;
    fin = fopen("/Users/Tony/Desktop/input.txt", "r");
    fout = fopen("/Users/Tony/Desktop/output.txt", "w");
    fscanf(fin, "%d", &t);
    for (int i = 0; i < t; i++) {
        int d, t;
        fscanf(fin, "%d\n", &d);
        vector<int> vec(d, 0);
        int mx = 0;
        for (int j = 0; j < d; j++) {
            fscanf(fin, "%d", &t);
            vec[j] = t;
            if (t > mx) mx = t;
        }
        fprintf(fout, "Case #%d: %d\n", i+1, a.infinite_house(d, vec, mx));
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
