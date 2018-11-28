//
//  main.cpp
//  p1
//
//  Created by 默默 on 15-4-2.
//  Copyright (c) 2015年 默默. All rights reserved.
//
#include <iostream>
#include <iostream>
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
#define MA 1005
int num[MA];

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, Worsadld!\n";
    freopen("/Users/momo/Desktop/xcode_data/B-large.in", "r", stdin);
    freopen("/Users/momo/Desktop/xcode_data/out.txt", "w", stdout);

    //ifstream fin = ifstream("/Users/momo/Desktop/userProfile/user_profile1.txt");
    int cas;
    cin >> cas;
    int cc = 0;
    while (cc++ < cas){
        int n;
        cin >> n;
        memset(num, 0, sizeof(num));
        
        for (int i = 0; i < n; ++i)
        {
            int t;
            cin >> t;
            num[t]++;
        }
        //int start = 0;
        int right = 1000;
        while (num[right] == 0){
            --right;
        }
        int step = right;
        for (int i = 1; i <= right; ++i){
            int nowstep = 0;
            for (int j = i + 1; j <= right; ++j){
                if (num[j] != 0){
                    nowstep += ((j + i - 1) / i - 1) * num[j];
                }
            }
            step = min(step, nowstep + i);
        }
        
        printf("Case #%d: %d\n", cc, step);
    }
}
