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

int DEBUG = 0;

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int n; scanf("%d", &n);
        long long raw[n], a[n], left[n], right[n];
        for (int i=0;i<n;i++) {
            scanf("%lld", &raw[i]);
            a[i] = raw[i];
        }


            if (DEBUG) {
                for (int i=0;i<n;i++) printf("%lld ", a[i]); puts("");
            }


            for (int i=0;i<n;i++) {
                int tmp = 0;
                for (int j=0;j<i;j++) {
                    if (a[j] > a[i]) tmp ++;
                }
                left[i] = tmp;

                tmp = 0;
                for (int j=i+1;j<n;j++) {
                    if (a[j] > a[i]) tmp ++;
                }
                right[i] = tmp;
            }

            if (DEBUG) {
                printf("- "); for (int i=0;i<n;i++)printf("%lld ", left[i]); puts("");
                printf("- "); for (int i=0;i<n;i++)printf("%lld ", right[i]); puts("");
            }
                
            long long init = 0;
            long long cnt = init;
            for (int j=0;j<n;j++) {
                cnt += min(left[j], right[j]);
            }
            /*
            for (int j=0;j<p;j++) {
                cnt += left[j];
            }
            for (int j=p+1;j<n;j++) {
                cnt += right[j];
            }
            */
            if (DEBUG) printf("- %lld (init %lld)\n", cnt, init);

       long long ans = cnt;


        printf("Case #%d: %lld\n",ti,ans);
    }
    return 0;
}
