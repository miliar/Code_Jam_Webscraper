//
//  GCJ2015QR1.cpp
//  playground
//
//  Created by Adam Chang on 2015/4/11.
//  Copyright (c) 2015年 Adam Chang. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <set>
#include <stack>
#include <cmath>

using namespace std;

int main(){
    int caseCnt = 0;
    cin >> caseCnt;
    for (int ci = 1; ci <= caseCnt; ci++) {
        vector<int> seq;
        int n = 0;
        cin >> n;
        for (int i = 1; i <= n; i++) {
            int tmp;
            cin >> tmp;
            seq.push_back(tmp);
        }
        sort(seq.begin(), seq.end());
        int res = 1000;
        for (int i = 1; i <= seq[seq.size()-1]; i++) {
            int cnt = 0;
            for (int j = 0;j < seq.size(); j++) {
                if (seq[j] > i) {
                    cnt += (int)ceil(((double)seq[j]-(double)i)/i);
                }
            }
            res = min(res,i+cnt);
        }
        cout << "Case #" << ci << ": " << res << endl;
    }
    return 0;
}
