//
//  main.cpp
//  ACMtest
//
//  Created by sciencefans on 14-3-27.
//  Copyright (c) 2014年 sciencefans. All rights reserved.
//

#include <stdio.h>
#include <algorithm>
#define MAXN 10001
int parent[MAXN], rank[MAXN];
int T, now;

using namespace std;
double a[1001], b[1001];

void DO(){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%lf", &a[i]);
    }
    for(int i = 0; i < n; i++){
        scanf("%lf", &b[i]);
    }
    sort(a, a+n);
    sort(b, b+n);
    int c, nc;
    c = nc = 0;
    for(int i = 0, j = 0; i < n; i++){
        while(j < n){
            if(a[j] > b[i]){
                c++;
                j++;
                break;
            }
            j++;
        }
    }
    for(int i = 0, j = 0; i < n; i++){
        while(j < n){
            if(b[j] > a[i]){
                nc++;
                j++;
                break;
            }
            j++;
        }
    }
    printf("Case #%d: %d %d\n", now, c, n - nc);
}

int main(){
    FILE* fin;
    fin = fopen("/Users/sciencefans/Documents/in.txt", "r");
    if(fin == NULL){
        printf("error read\n");
    }
    freopen("/Users/sciencefans/Documents/in.txt", "r", stdin);
    freopen("/Users/sciencefans/Documents/out.txt", "w", stdout);
    now = 0;
    scanf("%d", &T);
    while(T--){
        now++;
        DO();
    }
    return 0;
}