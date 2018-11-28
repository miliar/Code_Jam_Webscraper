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

        int n; scanf("%d", &n);
        int a[n], mx = 0; 
        for (int i=0;i<n;i++) {
            scanf("%d", &a[i]);
            if (a[i] > mx) mx = a[i];
        }

        int ans = 1000;
        for (int bound=1; bound<=mx; bound++) {
            // bound : max P value in this round
            // time = #split + max P
            int time = bound;
            for (int j=0;j<n;j++) {
                time += (a[j] - 1) / bound;
            }
            //printf("bound:%d time:%d\n", bound, time);
            
            if (ans > time) {
                ans = time;
            }

        }
        


        printf("Case #%d: %d\n",ti,ans);
    }
    return 0;
}
