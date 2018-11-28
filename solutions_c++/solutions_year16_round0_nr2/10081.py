//  code jam
//  RevengeofthePancakes.cpp
//  Algorithm
//
//  Created by chan on 2016. 4. 10..
//  Copyright © 2016년 chan. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char arr[110];
int len;
int result;

bool isSolve(){
    for(int i = 0 ; i <len; i++){
        if(arr[i] == '-') return false;
    }
    return true;
}

int selectIndex(){
    int i = 0;
    if(arr[i] == '-'){
        while(i < len && arr[i+1] != '+') i++;
    }else{
        while(i < len && arr[i+1] != '-') i++;
    }
    return i;
}

void solve(){
    result = 0;
    while(!isSolve()){
        int index = selectIndex();
        for(int i = 0 ; i <=index; i++){
            if(arr[i] == '+') arr[i] = '-';
            else              arr[i] = '+';
        }
        result++;
    }
}

int main () {
    int T;
    scanf("%d", &T);
    for(int tc = 1; tc <= T; tc++){
        scanf("%s", arr);
        len = (int) strlen(arr);
        solve();
        printf("Case #%d: %d\n", tc, result);
    }
}