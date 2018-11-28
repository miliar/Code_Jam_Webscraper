#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;

int T, n, c1, c2;
double a1[1005], a2[1005];

int main(){
    int kk = 0;
    cin >> T;
    while (T--){
        kk++;
        cin >> n;
        for (int i = 0; i < n; ++i) cin>> a1[i];
        for (int i = 0; i < n; ++i) cin >> a2[i]; // read blocks

        sort(a1, a1 + n);
        sort(a2, a2 + n);
        int l1 = 0; 
        int l2 = 0;
       
        // compute war
        while (l2 <= n-1){
            while (l2 <= n-1 && a2[l2] < a1[l1]) // move right to win
                l2 ++;
            if (l2 <= n-1) {
                l1 ++; l2++;
            }
        }
        c1 = 0;
        c2 = n - l1;

        // compute deceive war
        l1 = l2 =0;
        int r1 = n-1, r2 = n-1;
        while (l1 <= r1){
            if (a1[l1] < a2[l2]){ //deceive
                l1 ++; r2 --;
            }
            else {
                c1 ++;
                l1 ++; l2++;
            }
        }

        printf("Case #%d: %d %d\n", kk, c1, c2);

    }
}
