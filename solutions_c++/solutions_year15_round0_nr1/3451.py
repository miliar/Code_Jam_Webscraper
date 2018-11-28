//
//  main.cpp
//  GCJ2015-1-1
//
//  Created by 冥途雨中旅 on 15/4/12.
//  Copyright (c) 2015年 Gensokyou. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;


int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("../../../../GCJ2015-1-1/input","r",stdin);
    freopen("../../../../GCJ2015-1-1/output","w",stdout);
    int n;
    cin >> n;
    for(int testNumber = 1;testNumber <= n; ++ testNumber){
        int ninsu;
        cin >> ninsu;
        ninsu++;
        string S;
        cin >> S;
        int already = 0;
        int ans = 0;
        for(int i = 0;i < ninsu; ++i){
            if(i > already)
                ans += i - already, already = i;
            
            already += S[i] - '0';
            
        }
        cout << "Case #" << testNumber << ": " << ans << endl;
    }
    return 0;
}
