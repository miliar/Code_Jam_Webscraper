//
//  main.cpp
//  cj2016_qr2
//
//  Created by DongJiaming on 4/9/16.
//  Copyright © 2016 NYU. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    
    freopen("/Users/JiamingDong/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/JiamingDong/Documents/cj2016/qr/B-large.out", "w", stdout);
    
    int n;
    cin >> n;
    for (int tt = 1; tt <= n; tt++) {
        string s;
        cin >> s;
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '-') {
                if (i == 0) {
                    total++;
                }
                else if (s[i - 1] == '+') {
                    total += 2;
                }
            }
        }
        cout << "Case #" << tt << ": " << total << endl;
    }
    
    return 0;
}
