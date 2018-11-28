//
//  B.cpp
//  gcj2016
//
//  Created by Qicai Shi on 4/9/16.
//  Copyright © 2016 Qicai Shi. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(int argc, const char * argv[]) {
    
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    string s;
    int switchCount;
    for (int i = 1; i <= T; i++) {
        cin >> s;
        switchCount = 1;
        for(int j = 1; j < s.size(); j++) {
            if (s[j] != s[j - 1]) switchCount++;
        }
        if (s[s.size() - 1] == '+') {
            switchCount--;
        }
        printf("Case #%d: %d\n", i, switchCount);
    }
    return 0;
}
