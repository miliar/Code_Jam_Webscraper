//
//  main.cpp
//  Counting Sheep
//
//  Created by Liang on 16/4/9.
//  Copyright © 2016年 Liang. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;
bool is_have[11];

void solve_num(long long num) {
    while(num) {
        int x = num%10;
        num/=10;
        is_have[x] = 1;
    }
}

bool check() {
    for (int i = 0; i <= 9; i++) {
        if (is_have[i] == 1) {
            continue;
        } else {
            return 0;
        }
    }
    return 1;
}

int main(int argc, const char * argv[]) {
    
    freopen("/Users/baidu/Desktop/Counting Sheep/A-large.in","r",stdin);
    freopen("/Users/baidu/Desktop/Counting Sheep/A-large.out","w",stdout);
    
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        int num;
        cin >> num;
        memset(is_have, 0, sizeof(is_have));
        bool is_get = 0;
        int newnum = num;
        for (int k = 1; k <= 100; k++) {
            newnum = num*k;
            solve_num(newnum);
            if (check() == 1) {
                is_get = 1;
                break;
            }
        }
        if (is_get == 1)
            cout << "Case #" << ca <<": " << newnum << endl;
        else
            cout << "Case #" << ca <<": " << "INSOMNIA" << endl;
        
    }
    return 0;
}
