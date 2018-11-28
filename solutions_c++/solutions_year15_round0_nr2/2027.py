#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

void solve() {
    int d;
    scanf("%d", &d);
    
    vector<int> v;
    for (int i = 0; i < d; i++) {
        int val;
        scanf("%d", &val);
        v.push_back(val);
    }
    
    int best = 1000;
    
    for (int vmax = 1; vmax <= 1000; vmax++) {
        int cnt = vmax;
        for (int i = 0; i < d; i++) {
            int temp = (v[i] + vmax - 1) / vmax;
            cnt += temp - 1;
        }
        best = min(best, cnt);
    }
    
    printf("%d", best);
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("B-large.in.txt", "rt", stdin);
//    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    int t;
    scanf("%d", &t);
    
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    
}
