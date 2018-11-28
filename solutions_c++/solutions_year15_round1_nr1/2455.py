//
//  main.cpp
//  A
//
//  Created by 박수찬 on 14. 11. 22..
//  Copyright (c) 2014년 박수찬. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <numeric>
#include <deque>
#include <utility>
#include <bitset>
#include <limits.h>
#include <list>
#include <iostream>

using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;

int TCC;

int M[1050];
int N;

void init() {
    
}

void solve() {
    scanf("%d", &N);
    for(int i = 1; i <= N; i++) scanf("%d", M+i);
    
    int max_diff = 0;
    for(int i = 1; i < N; i++) {
        max_diff = max(max_diff, M[i] - M[i + 1]);
    }
    
    int ans1 = 0;
    for(int i = 1; i < N; i++) {
        ans1 += max(M[i] - M[i + 1], 0);
    }
    
    int ans2 = 0;
    for(int i = 1; i < N; i++) {
        ans2 += min(max_diff, M[i]);
    }
    
    printf("Case #%d: %d %d\n", TCC, ans1, ans2);
    
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int TC; scanf("%d", &TC);
    while(++TCC <= TC) {
        init();
        solve();
    }
    
    return 0;
}

