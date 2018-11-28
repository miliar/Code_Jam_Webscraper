//
//  CountingSheep.cpp
//  Algorithm
//
//  Created by chan on 2016. 4. 9..
//  Copyright © 2016년 chan. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int N;
int arr[101];
bool check[10];
int dab;

int main () {
    int T;
    scanf("%d", &T);
    for(int tc = 1; tc <= T; tc++){
        memset(check, false, sizeof(check));
        scanf("%d", &N);
        
        for(int i = 1; i <= 100; i++){
            arr[i] = N * i;
            int temp = arr[i];
            while(temp > 0){
                check[temp % 10] = true;
                temp /= 10;
            }
            bool flag = true;
            for(int i = 0; i < 10; i++){
                if(!check[i]) { flag = false; break; }
            }
            if(flag){
                dab = i;
                break;
            }
        }
        
        bool flag = true;
        for(int i = 0; i < 10; i++){
            if(!check[i]) { flag = false; break; }
        }
        
        if(flag){
            printf("Case #%d: %d\n", tc, arr[dab]);
        }else{
            printf("Case #%d: INSOMNIA\n", tc);
        }
        
        
    }
}