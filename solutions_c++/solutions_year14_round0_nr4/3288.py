//
//  main.cpp
//  DeceitfulWar
//
//  Created by 向仁楷 on 14-4-13.
//  Copyright (c) 2014年 Giraffe-Tech. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>

double num1[1009],num2[1009];
int n;


int mycmp(const void *a,const void *b){
    
    double n1,n2;
    n1 = *((double *)a);
    n2 = *((double *)b);
    if (n1 - n2 > 0) {
        return -1;
    }
    return 1;
}


int main(int argc, const char * argv[])
{
    int tc,i,j,k,ans1,ans2;
    
    freopen("./D-large.in", "r", stdin);
    freopen("./D-large.out", "w", stdout);
    
    scanf("%d",&tc);
    
    for (k = 1; k <= tc; k ++) {
        //scanf("%d",&tc);
        scanf("%d",&n);
        ans1 = 0;
        ans2 = 0;
        
        for (i = 0; i < n; i ++) {
            scanf("%lf",&num1[i]);
        }
        for (i = 0; i < n; i ++) {
            scanf("%lf",&num2[i]);
        }
        
        qsort(num1,n, sizeof(double), mycmp);
        qsort(num2,n, sizeof(double), mycmp);
        
        j = n - 1;
        for (i = n-1; i >= 0; i --){
            if (num1[i] > num2[j]) {
                j --;
                ans1 ++;
            }
        }
        
        j = 0;
        for (i = 0; i < n ; i ++){
            if (num2[j] > num1[i]) {
                j ++;
                ans2 ++;
            }
        }
        
        
        printf("Case #%d: %d %d\n",k,ans1,n - ans2);
    }
    
    
    return 0;
}

