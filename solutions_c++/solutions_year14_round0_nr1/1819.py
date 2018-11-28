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

void DO(){
    bool vis[17];
    for(int i = 0; i < 17; i++){
        vis[i] = 0;
    }
    int a;
    scanf("%d", &a);
    for(int i = 0; i < 16; i++){
        int t;
        scanf("%d", &t);
        if(i / 4 == a - 1){
            vis[t] = true;
        }
    }
    scanf("%d", &a);
    for(int i = 0; i < 16; i++){
        int t;
        scanf("%d", &t);
        if(i / 4 != a - 1){
            vis[t] = false;
        }
    }
    int sum = 0;
    int bingo = 0;
    for(int i = 1; i < 17; i++){
        if(vis[i]){
            bingo = i;
            sum++;
        }
    }
    if(sum > 1){
        printf("Case #%d: Bad magician!\n", now);
    }else if(sum == 1){
        printf("Case #%d: %d\n", now, bingo);
    }else{
        printf("Case #%d: Volunteer cheated!\n", now);
    }
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