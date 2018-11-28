//
//  main.cpp
//  acm
//
//  Created by JackieZhu on 14-4-12.
//  Copyright (c) 2014年 JackieZhu. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <stack>
#include <sstream>
#include <cmath>
#include <queue>
#include <memory.h>
using namespace std;

int main()
{
    freopen("/Users/JackieZhu/Documents/work/Job hunting/prectise/acm/B-large.in", "r", stdin);
    freopen("/Users/JackieZhu/Documents/work/Job hunting/prectise/acm/output.out", "w", stdout);
    int T;
    cin >> T;
    cout.precision(7);
    for (int cas=1; cas<=T; cas++) {
        double C, F, X; //2.0 persecnod
        cin >> C >> F >> X;
        double ret = 1e10, usedTime = 0;
        for (int i=0; i*C<=X; i++) {
            ret = min(ret, X/(2.0+F*i)+usedTime);
            usedTime += C / (2.0+F*i);
        }
        cout << "Case #" << cas << ": ";
        cout << fixed << ret << endl;
    }
    return 0;
}