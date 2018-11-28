#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdlib>
#define LL long long

int T;
int n;
int a[37];
int ct;

int findMaxI(){
    int maxI = -1, maxV = 0;
    for (int i = 0; i < n; i++){
        if (a[i] > maxV){
            maxV = a[i];
            maxI = i;
        }
    }
    return maxI;
}

void solve(){
    scanf("%d", &n);
    ct = 0;
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n; i++) ct += a[i];
    while (1){
        int maxI = findMaxI();
        if (maxI == -1) break;
        a[maxI]--;
        ct--;
        int maxI2 = findMaxI();
        if (ct != 2 && maxI2 != -1){
            a[maxI2]--;
            ct--;
            printf(" %c%c", maxI + 'A', maxI2 + 'A');
        }else{
            printf(" %c", maxI + 'A');
        }
    }
    printf("\n");
}

int main(){
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        printf("Case #%d:", i);
        solve();
    }
    return 0;
}
