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
        int n; 
        char s[2000];
        scanf("%d%s", &n, s);

        n++;

        int a[n]; 
        for (int i=0;i<n;i++) {
            a[i] = s[i] - '0';
        }

        int add = 0, standing = a[0];
        
        for (int i=1;i<n;i++) {
            if (a[i] > 0) {
                if (i > standing) {
                    int diff = i - standing;
                    add += diff;
                    standing += diff;
                }
                standing += a[i];
                //printf("%d(%d) %d(%d)\n", i, a[i], standing, add);
            }
        }

        int ans = add;


        printf("Case #%d: %d\n",ti,ans);
    }
    return 0;
}
