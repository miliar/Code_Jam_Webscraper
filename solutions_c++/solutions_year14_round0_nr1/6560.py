//
//  main.cpp
//  GCJ2014
//
//  Created by Zhu Haifan on 14-4-12.
//  Copyright (c) 2014年 Zhu Haifan. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Users/whshev/Dropbox/Programs/GCJ2014/Data/QR/A-small-attempt0.in", "r", stdin);
    freopen("/Users/whshev/Dropbox/Programs/GCJ2014/Data/QR/A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int row1, row2, map1[4][4], map2[4][4];
    vector<int> s1, s2;
    for (int i = 1; i <= T; ++i) {
        s1.clear(); s2.clear();
        scanf("%d", &row1);
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                scanf("%d", &map1[j][k]);
                if (j == row1 - 1) s1.push_back(map1[j][k]);
            }
        }
        scanf("%d", &row2);
        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                scanf("%d", &map2[j][k]);
                if (j == row2 - 1) s2.push_back(map2[j][k]);
            }
        }
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        vector<int> s{};
        set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(s));
        printf("Case #%d: ", i);
        if (s.size() == 1) {
            printf("%d\n", s[0]);
        } else if (s.size() > 1) {
            printf("Bad magician!\n");
        } else {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}

