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
#include <queue>
using namespace std;
#define MA 1005

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, Worsadld!\n";
    freopen("/Users/momo/Desktop/xcode_data/A-large.in", "r", stdin);
    freopen("/Users/momo/Desktop/xcode_data/A-small-attempt0.out", "w", stdout);

    //ifstream fin = ifstream("/Users/momo/Desktop/userProfile/user_profile1.txt");
    int cas;
    cin >> cas;
    int cc = 0;
    while (cc++ < cas){
        int len;
        cin >> len;
        string str;
        cin >> str;
        int maxx = 0;
        int now = 0;
        for (int i = 0; i <= len; ++i){
            maxx = max(i - now, maxx);
            now += str[i] - '0';
        }
        printf("Case #%d: %d\n", cc, maxx);
    }
}
