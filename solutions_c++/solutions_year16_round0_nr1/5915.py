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

using namespace std;

typedef long long int LL;

LL cal(LL n) {
    bool t[10];
    memset(t, 0, sizeof(t));
    int i = 1;
    
    while (true) {
        LL x = i * n;
        while (x) {
            int y = x % 10;
            t[y] = true;
            x /= 10;
        }
        bool ok = true;
        for (int j = 0; j < 10; j++) {
            if (!t[j]) {
                ok = false;
                break;
            }
        }
        if (ok) return i * n;
        i++;
    }
    return -1;
}

int main(int argc, const char * argv[]) {

    ifstream cin("/Users/like/Downloads/A-large.in");
    ofstream cout("/Users/like/Desktop/Github/googlecodejam/codejam/codejam/A-large.out");
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        LL n;
        cin >> n;
        cout << "Case #" << i << ": ";
        if (n == 0) cout << "INSOMNIA" << endl;
        else cout << cal(n) << endl;
    }
    
    return 0;
}
