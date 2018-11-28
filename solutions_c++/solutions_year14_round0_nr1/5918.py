//
//  A.m
//  GoogleCodeJam2014
//
//  Created by dabao on 14-4-12.
//  Copyright (c) 2014年 Dabaopku. All rights reserved.
//

#import <Foundation/Foundation.h>
#include <stdio.h>
#include <iostream>
using namespace std;

int r1, r2;

int cnt[17];

void input()
{
    int x;
    for (int i = 0; i < 17; ++i) {
        cnt[i] = 0;
    }

    cin>>r1;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin>>x;
            if (i != r1) {
                continue;
            }
            cnt[x]++;
        }
    }

    cin>>r2;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin>>x;
            if (i != r2) {
                continue;
            }
            cnt[x]++;
        }
    }
}

void solve()
{
    int found = 0;
    int n = -1;
    
    for (int i = 1; i < 17; ++i) {
        if (cnt[i] == 2) {
            found++;
            n = i;
        }
    }
    if (found == 1) {
        cout<<n<<endl;
    }
    else if (found == 0) {
        cout<<"Volunteer cheated!\n";
    }
    else {
        cout<<"Bad magician!\n";
    }
}

int main(int argc, const char * argv[])
{
    
    @autoreleasepool {
        
        freopen("/Users/dabao/Desktop/GoogleCodeJam2014/GoogleCodeJam2014/A.in", "r", stdin);
        freopen("/Users/dabao/Desktop/GoogleCodeJam2014/GoogleCodeJam2014/A.out", "w", stdout);
        
        int CaseNum;
        cin>>CaseNum;
        for (int i = 0; i < CaseNum; ++i) {
            printf("Case #%d: ", i + 1);
            input();
            solve();
        }
        
    }
    return 0;
}

