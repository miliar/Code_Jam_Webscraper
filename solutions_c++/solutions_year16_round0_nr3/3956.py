//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by Liang on 16/4/9.
//  Copyright © 2016年 Liang. All rights reserved.
//

#include <iostream>
#include <cstring>
using namespace std;

char s[110];
int main(int argc, const char * argv[]) {
    
    freopen("/Users/baidu/code/Revenge of the Pancakes/B-large.in", "r", stdin);
    freopen("/Users/baidu/code/Revenge of the Pancakes/B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        cin >> s;
        int len = strlen(s);
        s[len]='+';
        int ans = 0;
        for (int i = 0; i < len; i++) {
            if (s[i] != s[i+1])
                ans ++;
        }
        cout << "Case #" << ca << ": " << ans << endl;
    }
    return 0;
}
