/*
 * Author: fatboy_cw
 * Created Time:  2014/4/12 10:54:46
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

const int sz = 4;
int ca, t, n, m, a[sz][sz], b[sz][sz], ans;

int check(int v) {
    int cnt = 0;
    for(int i = 0; i < 4; i++) {
        if(a[n][i] == v) {
            cnt++;
        }
        if(b[m][i] == v) {
            cnt++;
        }
    }
    if(cnt == 2) return 1;
    return 0;
}
            

int main() {
    freopen("A1.in", "r", stdin);
    freopen("A1.out", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        n--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        scanf("%d", &m);
        m--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &b[i][j]);
            }
        }
        int cnt = 0;
        for(int i = 1; i <= 16; i++) {
            if(check(i)) {
                ans = i;
                cnt++;
            }
        }
        if(cnt == 1) {
            printf("Case #%d: %d\n", ++ca, ans);
        }
        else if(cnt == 0) {
            printf("Case #%d: Volunteer cheated!\n", ++ca);
        }
        else {
            printf("Case #%d: Bad magician!\n", ++ca);
        }
    }
    return 0;
}

