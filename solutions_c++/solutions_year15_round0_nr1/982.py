//#include <bits/stdc++.h>

#include <iostream>
#include <cstdio>

using namespace std;

#define N 1005

char ss[N];

int main() {
    int test;
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &test);
    
    for (int cas = 1; cas <= test; cas++) {
        int n;
        scanf("%d%s", &n, ss);
        int sum = ss[0] - '0';
        int res = 0;
        for (int i = 1; i <= n; i++) {
                if (sum >= i) {
                
                }
                else {
                                res += i - sum;
                                sum = i;
                }
                sum += (ss[i] - '0');
        }
        printf("Case #%d: %d\n", cas, res);
    }
    
    //while (1);
    return 0;
}
