//
//  main.cpp
//  GCJ
//
//  Created by 祝风翔 on 14-5-11.
//  Copyright (c) 2014年 祝风翔. All rights reserved.
//

#include <iostream>
#include <memory.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <queue>
#include <math.h>
#include <algorithm>
#include <set>
using namespace std;
typedef long long LL;
vector<int>E;
const int N = 100000 + 5;
int used[100000 + 5];
multiset<int>S;
int cnt[1000 + 5];
int main(){
    int t,cas = 0;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    while(t--) {
        int n,x;
        memset(cnt,0,sizeof(cnt));
        scanf("%d %d",&n,&x);
        int ans = 0;
        int tp;
        E.clear();
        for(int i=  0;i < n;i++)
            scanf("%d",&tp),E.push_back(tp);
        sort(E.begin(),E.end());
        reverse(E.begin(),E.end());
        int r = n-1;
        for(int i = 0;i < n;i++) {
            if(r == i) {
                ans++;
                break;
            }
            if(r < i) break;
            ans = ans + 1;
            if(E[r] +E[i] <= x)
            r--;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}