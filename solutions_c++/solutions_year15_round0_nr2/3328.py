//
//  main.cpp
//  GCJ2015-1-1
//
//  Created by 冥途雨中旅 on 15/4/12.
//  Copyright (c) 2015年 Gensokyou. All rights reserved.
//

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int bucket[2000];
int tb[2000];

int main(int argc, const char * argv[]) {
    freopen("../../../../GCJ2015-1-1/input","r",stdin);
    freopen("../../../../GCJ2015-1-1/output","w",stdout);
    int T;
    cin >> T;
    for(int i = 0; i < T; ++i){
        int n;
        cin >> n;
        
        for(int i = 0;i < n; ++i)
            cin >> tb[i];
        int ans = 2000;
        for(int tt = 1;tt <= 1000;++tt){
            int tmp = 0;
            for(int i = 0;i < n; ++i)
                tmp += (tb[i] - 1)/tt;
            ans = min(ans, tmp + tt);
            
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    
    return 0;
}
