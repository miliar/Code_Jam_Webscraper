#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int N = 1024;
int data[N];

int main(){
    int T;
    scanf("%d", &T);
    for(int _ = 1 ; _ <= T; ++_){
        int n, maxn = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; ++i){
            scanf("%d", &data[i]);
            if(data[i] > maxn)
                maxn = data[i];
        }
        for(int t1 = 1; t1 < maxn; ++t1){
            int t0 = 0;
            for(int i = 0; i < n; ++i){
                t0 += (data[i] - 1) / t1;
            }
            if(maxn > t0 + t1) maxn = t0 + t1;
        }
        printf("Case #%d: ", _);
        printf("%d\n", maxn);
    }
}
