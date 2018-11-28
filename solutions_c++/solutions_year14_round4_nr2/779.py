/*
 * Author: fatboy_cw
 * Created Time:  2014/5/31 23:26:42
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int t, n, ans, ca;
vector<int> v;
bool use[1005];

int main() {
    freopen("b.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        v.clear();
        memset(use, false, sizeof(use));
        for(int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            v.push_back(x);
        }
        ans = 0;
        for(int i = 0; i < n; i++) {
            int val = maxint, ind = -1;
            for(int j = 0; j < n; j++) {
                if(use[j]) continue;
                if(get_min(val, v[j])) {
                    ind = j;
                }
            }
            int l = 0, r = 0;
            for(int j = 0; j < ind; j++) {
                if(!use[j]) l++;
            }
            for(int j = ind + 1; j < n; j++) {
                if(!use[j]) r++;
            }
            use[ind] = true;
            ans += min(l, r);
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }

    return 0;
}

