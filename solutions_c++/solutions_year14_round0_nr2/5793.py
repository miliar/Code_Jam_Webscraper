#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

int a[5][5], b[5][5];

int main() {
    freopen("/Users/L/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/L/Downloads/B-large.out.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int kase = 1; kase <= T; kase++) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        
        double re = 100000;
        double curtime = 0, currate = 2;
        while (curtime + x / currate < re) {
            re = curtime + x / currate;
            curtime += c / currate;
            currate += f;
        }
        
        printf("Case #%d: %.7f\n", kase, re);
    }
    return 0;
}
