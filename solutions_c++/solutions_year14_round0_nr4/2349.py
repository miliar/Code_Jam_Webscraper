#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;
int main(void){
    int t, T;
    scanf("%d", &t);
    for(T = 1; T <= t; T++){
        int i, j, size;
        scanf("%d", &size);
        double a[1100], b[1100];
        for(i = 0; i < size; i++)
            scanf("%lf", &a[i]);
        for(i = 0; i < size; i++)
            scanf("%lf", &b[i]);
        sort(a, a+size);
        sort(b, b+size);
        int win = 0;
        i = size - 1; j = size - 1;
        for(; i >= 0; i--){
            if(a[i] > b[j])
                win++;
            else if(a[i] < b[j])
                j--;
        }
        int cnt = 0;
        j = size - 1; i = size - 1;
        while(i >= 0 && j >= 0){
            if(a[i] > b[j]){
                cnt++; i--; j--;
            }
            else if(a[i] < b[j]){
                j--;
            }
        }
        printf("Case #%d: %d %d\n", T, cnt, win);
    }

}