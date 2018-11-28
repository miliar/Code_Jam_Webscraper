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

char s[10001];

pair<char, int> mul(char a, char b) {
    if (a == b) {
        if (a == '1') {
            return make_pair('1', 0);
        }
        return make_pair('1', 1);
    }
    if (a == 'i' && b == 'j') {
        return make_pair('k', 0);
    }
    if (a == 'j' && b == 'i') {
        return make_pair('k', 1);
    }
    if (a == 'j' && b == 'k') {
        return make_pair('i', 0);
    }
    if (a == 'k' && b == 'j') {
        return make_pair('i', 1);
    }
    if (a == 'k' && b == 'i') {
        return make_pair('j', 0);
    }
    if (a == 'i' && b == 'k') {
        return make_pair('j', 1);
    }
    if (a == '1') {
        return make_pair(b, 0);
    }
    return make_pair(a, 0);
}

void solve() {
    int l, x;
    scanf("%d%d", &l, &x);
    
    scanf("%s", s);
    
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < l; j++) {
            s[i * l + j] = s[j];
        }
    }
    
    char cur = '1';
    int sign = 0;
    int cnt = 0;
    for (int i = 0; i < x * l; i++) {
        pair<char, int> p = mul(cur, s[i]);
        cur = p.first;
        sign = (sign + p.second) % 2;
        if ((cnt == 0 && cur == 'i' && sign == 0) || (cnt == 1 && cur == 'j' && sign == 0)) {
            cnt++;
            cur = '1';
            sign = 0;
        }
    }
    if (cnt == 2 && cur == 'k' && sign == 0) {
        printf("YES");
    }
    else {
        printf("NO");
    }
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("C-small-attempt0.in.txt", "rt", stdin);
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
