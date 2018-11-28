//
//  main.cpp
//  C
//
//  Created by Nikifor Zhao on 15/5/30.
//  Copyright (c) 2015年 Nikifor Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <unordered_set>
#include <unordered_map>
#include <string>
using namespace std;

//short hhash(string s){
//    short x = 0;
//    for (int i = 0; i < s.size(); i ++) {
//        x = (x * 89393 + s[i]);
//    }
//    return x;
//    
//}

int main(int argc, const char * argv[]) {
    int T;
    FILE *fp1 = fopen("C-small-attempt2.in", "r");
    FILE *fp2 = fopen("output.txt", "w");
    
    fscanf(fp1, "%d", &T);
    for (int ti = 1; ti <= T; ++ ti) {
        //cout << ti << endl;
        int ans = 2e9;;
        int n;
        unordered_map<string, int> m;
        m.clear();
        
        fscanf(fp1, "%d", &n);
        char cttt;
        fscanf(fp1, "%c", &cttt);
        for (int i = 0; i < n ; i ++) {
            char c[100000] = {0};
            int p = 0;
            
            while (1) {
                fscanf(fp1, "%c", &c[p]);
                if (c[p] == '\n') break;
                p ++;
            }
            //cout << c << endl << endl;
            for (int j = 0; j <= p; j ++) {
                if (c[j] == ' ' || c[j] == '\n') c[j] = 0;
            }
            for (int j = 0; j <= p; j ++) {
                if (j == 0 || c[j-1] == 0) {
                    string s = string(c+j);
                    //cout << m[string(c+j)] << endl;
                    m[string(c+j)] =  (m[string(c+j)] | (1 << (i)));
                    //cout << m[string(c+j)] << endl;
                }
            }
        }
//        for (auto it = m.begin(); it != m.end(); ++ it) {
//            cout << it->first << " " << it->second << endl;
//        }
        for (int x = 0; x < (1 << (n - 2)); x ++) {
            int tans = 0;
            for (auto it = m.begin(); it != m.end(); it ++) {
                int t = it->second, t2;

                t2 = (t >> 2);
                //cout << t << " " << x << endl;
                if ((t & 1) != 0 && (t & 2) != 0) tans ++;
                else if ( (t2 & x) && (t2 & (~x))) tans ++;
                else if ( (t2 & x) && (t & 1)) tans ++;
                else if ( (t2 & (~x)) && (t & 2)) tans ++;

            }
            if (tans == 2) cout << " " << " " << x << endl;;
            if (tans < ans) ans = tans;
        }
        fprintf(fp2, "Case #%d: %d\n", ti, ans);
    }
    return 0;
}
