#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
using namespace std;

bool cmp(double a, double b){
    return a > b;
}

int getMax(double a[], int n){
    int i = n - 1;
    while(i >= 0 && a[i] == 0.0) i--;
    return i;
}

int getMin(double a[], int n){
    int i = 0;
    while(i < n && a[i] == 0.0) i++;
    return i;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int __tt, T;
    double naomi[1005], ken[1005], tKen[1005];
    int n, score, bestScore;
    int i, j;

    while(EOF != scanf("%d", &T)){
        for(__tt = 1; __tt <= T; __tt++){
            scanf("%d", &n);
            bestScore = 0;
            score = n;
            for(i = 0; i < n; i++)
                scanf("%lf", &naomi[i]);
            for(i = 0; i < n; i++)
                scanf("%lf", &ken[i]);
            sort(naomi, naomi + n);
            sort(ken, ken + n);
            memcpy(tKen, ken, sizeof(double) * n);
            for(i = 0; i < n; i++){
                int min = getMin(tKen, n);
                if(naomi[i] > tKen[min]){
                    bestScore ++;
                    tKen[min] = 0.0;
                } else{
                    tKen[getMax(tKen, n)] = 0.0;
                }
            }
            for(i = 0; i < n; i++){
                int min = getMin(naomi, n);
                if(ken[i] > naomi[min]){
                    score--;
                    naomi[min] = 0.0;
                } else{
                    naomi[getMax(ken, n)] = 0.0;
                }
            }
            printf("Case #%d: %d %d\n", __tt, bestScore, score);
        }
    }
    return 0;
}
