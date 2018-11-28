//
//  main.cpp
//  codejam
//
//  Created by 李科 on 16/4/9.
//  Copyright © 2016年 李科. All rights reserved.
//

#include <iostream>
#include <string.h>
#include <fstream>
#include <sstream>

using namespace std;

typedef long long int LL;


string getstring(int k, int n) {
    ostringstream s1;
    int d[30];
    for (int i = n; i >= 0; i--) {
        d[i] = k % 2;
        k = k / 2;
    }
    d[0] = d[n + 1] = 1;
    for (int i = 0; i <= n + 1; i++) {
        s1 << d[i];
    }
    return s1.str();
}


int main(int argc, const char * argv[]) {
    
    ifstream cin("/Users/like/Downloads/C-small-attempt2.in");
    ofstream cout("/Users/like/Desktop/Github/googlecodejam/codejam/codejam/C-small-attempt0.out");
    

    
    int t;
    cin >> t;
    
    for (int tt = 1; tt <= t; tt++) {
        int N, J;
        
        cin >> N >> J;
        
        cout << "Case #" << tt << ":" << endl;
        
        for (int k = 0; k < (1 << (N - 2)) && J; k++) {
            string s = getstring(k, N - 2);
            LL d[50];
            bool ok = true;
            
            for (int i = 2; i <= 10; i++) {
                LL v = 0;
                for (int j = 0; j < s.size(); j++) {
                    v = v * i + (s[j] - '0');
                }
                bool isprime = true;
                for (LL h = 2; h * h <= v; h++) {
                    if (v % h == 0) {
                        isprime = false;
                        d[i] = h;
                        break;
                    }
                }
                if (isprime) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                cout << s << " ";
                for (int h = 2; h <= 10; h++) {
                    cout << d[h];
                    if (h < 10) cout << " ";
                    else cout << endl;
                }
                J--;
            }
        }
    }
    
    return 0;
}
