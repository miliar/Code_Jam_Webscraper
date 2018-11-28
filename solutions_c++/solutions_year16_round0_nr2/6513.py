/*
 * Author: fatboy_cw
 * Created Time:  2016年04月09日 星期六 11时52分56秒
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

const int maxn = 100 + 5;

int T, N, ca;
char ch[maxn];

int main() {
    freopen("B.out", "w", stdout);
    scanf("%d", &T);
    while(T--) {
        scanf("%s", ch);
        N = strlen(ch);
        char p = '*';
        int cnt = 0;
        for(int i = 0; i < N; i++) {
            if(ch[i] != p) cnt ++;
            p = ch[i];
        }
        if(ch[N - 1] == '+') cnt--;
        printf("Case #%d: %d\n", ++ca, cnt);
    }
    return 0;
}

