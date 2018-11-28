//
//  main.cpp
//  p2
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
#include <cstring>
#include <queue>
using namespace std;
#define MA 120005
int str[MA];
//int left[MA];
//int right[MA];
int mp[5][5] = {0,0,0,0,0, 0,1,2,3,4, 0,2,-1,4,-3, 0,3,-4,-1,2, 0,4,3,-2,-1};
int l,x;
/*
int check(int l, int r, int total){
    //c r
    if (l < 0)
        total = -total;
    for (int i = 1; i <= 4; ++i){
        if (abs(mp[abs(l)][i]) == abs(total)){
            //total = i;
            if(mp[abs(l)][i] != total)
                total = -i;
            else
                total = i;
        }
    }
    
    if (r < 0)
        total = -total;
    for (int i = 1; i <= 4; i++){
        if (abs(mp[i][abs(r)]) == abs(total)){
            if (mp[i][abs(r)] != total)
                total = -i;
            else
                total = i;
        }
    }
    return total;
}
 */
int main(int argc, const char * argv[]) {
    //freopen("/Users/momo/Desktop/xcode_data/in.txt", "r", stdin);
    freopen("/Users/momo/Desktop/xcode_data/C-small-attempt2.in", "r", stdin);
    freopen("/Users/momo/Desktop/xcode_data/out.txt", "w", stdout);
    
    //ifstream fin = ifstream("/Users/momo/Desktop/userProfile/user_profile1.txt");
    int cas;
    cin >> cas;
    int cc = 0;
    while (cc++ < cas){
        cin >> l >> x;
        int times;
        string s;
        cin >> s;
        if (x < 12){
            times = x;
            //for (int i = 0; i < l; ++i)
        }
        else{
            times = 8 + x % 4;
        }
        times = x;
        int n = 0;
        for (int i = 0; i < times; ++i){
            for (int j = 0; j < l; ++j){
                int val;
                if (s[j] == 'i')
                    val = 2;
                else if (s[j] == 'j')
                    val = 3;
                else
                    val = 4;
                str[n] = val;
                n++;
            }
        }
        int ans = 1;
        for (int i = 0; i < n; ++i){
            int tans = abs(ans);
            int small = 0;
            if (ans < 0)
                small = 1;
            ans = mp[tans][str[i]];
            if (small == 1){
                ans = -ans;
            }
        }
        //cout << ans << endl;
        if (ans != -1){
            printf("Case #%d: NO\n", cc);
            continue;
        }
        int fromright = 1;
        int siteright = n - 1;
        while (siteright >= 0){
            int small = 0;
            if (fromright < 0)
                small = 1;
            fromright = mp[str[siteright]][abs(fromright)];
            if (small == 1)
                fromright = -fromright;
            
            if (fromright == 4)
                break;
            siteright--;
        }
        //cout << siteright<< endl;
        if (siteright <= 0)
        {
            printf("Case #%d: NO\n", cc);
            continue;
        }
        
        int fromleft = 1;
        int ok = 0;
        for (int i = 0; i < 4 * l && i < siteright; ++i){
            int samll = 0;
            if (fromleft < 0)
                samll = 1;
            fromleft = mp[abs(fromleft)][str[i]];
            if (samll == 1)
                fromleft = - fromleft;
            if (fromleft == 2){
                //cout << i << endl;
                ok = 1;
                break;
            }
        }
        if (ok){
            printf("Case #%d: YES\n", cc);
        }
        else{
            printf("Case #%d: NO\n", cc);

        }
        
    }
    return 0;
}








