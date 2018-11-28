//
//  main.cpp
//  ACMtest
//
//  Created by sciencefans on 14-3-27.
//  Copyright (c) 2014年 sciencefans. All rights reserved.
//

#include <stdio.h>
#define MAXN 10001
int parent[MAXN], rank[MAXN];
int T, now;
double intertime[100001];

void DO(){
    double c, f, x;
    int i;
    double time;
    intertime[0] = 0;
    scanf("%lf%lf%lf", &c, &f, &x);
    time = x / 2.0;
    for(i = 1; i < x / c; i++){
        double ttime = 0;
        intertime[i] = c / (2 + f * (i - 1)) + intertime[i - 1];
        ttime += intertime[i];
        ttime += x / (2 + f * i);
        if(ttime < time)
            time = ttime;
    }
    printf("Case #%d: %.7lf\n", now, time);
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