/*
 * Author: fatboy_cw
 * Created Time:  2014/5/31 22:05:54
 * File Name: A.cpp
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

int t, n, x, ans, ca;
vector<int> vec;

int main() {
    freopen("A.out", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d", &n, &x);
        vec.clear();
        for(int i = 0; i < n; i++) {
            int v;
            scanf("%d", &v);
            vec.push_back(v);
        }
        sort(vec.begin(), vec.end());
        int l = 0, r = (int)vec.size() - 1;
        ans = 0;
        while(1) {
            if(l > r) break;
            if(l == r) {
                ans += 1;
                break;
            }
            if(vec[l] + vec[r] <= x) {
                ans += 1;
                l++;
                r--;
            }
            else {
                r--;
                ans += 1;
            }
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}

