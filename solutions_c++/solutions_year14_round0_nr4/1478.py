/*
 * Author: fatboy_cw
 * Created Time:  2014/4/12 12:31:21
 * File Name: D.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int ca, t, n;
vector<double> w1, w2;

int getAns() {
    set<double> st;
    for(int i = 0; i < w2.size(); i++) {
        st.insert(w2[i]);
    }
    int ans = n;
    for(int i = 0; i < w1.size(); i++) {
        set<double>::iterator it = st.lower_bound(w1[i]);
        if(it == st.end()) return ans;
        ans--;
        st.erase(it);
    }
    return ans;
}

bool check(int l1, int r1, int l2, int r2) {
    for(int i = l1; i <= r1; i++) {
        int j = i - l1 + l2;
        if(w1[i] < w2[j]) return false;
    }
    return true;
}

int main() {
    freopen("D2.in", "r", stdin);
    freopen("D2.out", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        w1.clear();
        w2.clear();
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            double w;
            scanf("%lf", &w);
            w1.push_back(w);
        }
        for(int i = 0; i < n; i++) {
            double w;
            scanf("%lf", &w);
            w2.push_back(w);
        }
        sort(w1.begin(), w1.end());
        sort(w2.begin(), w2.end());
        int l1 = 0, r1 = n - 1, l2 = 0, r2 = n - 1;
        while(l1 <= r1 && l2 <= r2 && check(l1, r1, l2, r2) == false) {
            l1++;
            r2--;
        }
        printf("Case #%d: %d %d\n", ++ca, r1 - l1 + 1, getAns());
    }
    return 0;
}

