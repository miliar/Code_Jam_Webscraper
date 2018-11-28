#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>

#include <thread>
#include <chrono>

#include <memory>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/stat.h>

#define EP 1e-10
using namespace std;


struct B {
    double r, c;
};

B b[110];

bool cmp(B& x, B& y) {
    return x.c > y.c;
}

int main() {
    freopen("/Users/lujcmss/Downloads/B-small-attempt1.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/b.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int kase = 0; kase < T; kase++) {
        int n;
        double v, x;
        double t1 = 0, t2 = 0;

        cin >> n >> v >> x;
        for (int i = 0; i < n; i++) {
            cin >> b[i].r >> b[i].c;
            t2 = max(t2, v / b[i].r);
        }
        
        sort(b, b+n, cmp);
        
        
        printf("Case #%d: ", kase+1);
        if ((n == 1 && b[0].c != x) || b[0].c + EP < x || b[n-1].c - EP > x) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        while (t2 - t1 > 1e-8) {
            double mid = (t1 + t2) / 2;
            
            double totV = 0, totT = 0;
            for (int i = 0; i < n; i++) {
                totT += b[i].r * mid * b[i].c;
                totV += b[i].r * mid;
            }
            
            double totC = totT / totV;
            while (totC > x + EP) {
                for (int i = 0; i < n; i++) {
                    double tt = b[i].r * mid * b[i].c;
                    double tv = b[i].r * mid;
                    if (totV - tv < EP) { totC = x; break; }
                    if ((totT - tt) / (totV - tv) > x + EP) {
                        totT -= tt;
                        totV -= tv;
                        totC = totT / totV;
                    } else {
                        totV -= (totT - totV * x) * b[i].r / (b[i].r * b[i].c - b[i].r * x);
                        totC = x;
                        break;
                    }
                }
            }
            while (totC < x - EP) {
                for (int i = n - 1; i >= 0; i--) {
                    double tt = b[i].r * mid * b[i].c;
                    double tv = b[i].r * mid;
                    if (totV - tv < EP) { totC = x; break; }
                    if ((totT - tt) / (totV - tv) < x - EP) {
                        totT -= tt;
                        totV -= tv;
                        totC = totT / totV;
                    } else {
                        totV -= (totT - totV * x) * b[i].r / (b[i].r * b[i].c - b[i].r * x);
                        totC = x;
                        break;
                    }
                }
            }

            if (totV < v) {
                t1 = mid;
            } else {
                t2 = mid;
            }
        }
        
        printf("%.10f\n", t2);
    }
    
    return 0;
}