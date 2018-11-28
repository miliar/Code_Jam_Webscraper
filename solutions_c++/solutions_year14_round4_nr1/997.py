#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int n, x; scanf("%d%d", &n, &x);
        int a[n];
        for (int i=0;i<n;i++) {
            scanf("%d", &a[i]);
        }
        sort(a, a+n);

        int ans = 0;
        int p = 0, q = n-1;
        while (p <= q) {
            if (p == q) {
                ans ++;
                p ++;
                q --;
            } else {
                if (a[q] + a[p] <= x) {
                    ans ++;
                    p ++;
                    q --;
                } else {
                    ans ++;
                    q --;
                }
            }
        }

        printf("Case #%d: %d\n",ti,ans);
    }
    return 0;
}
