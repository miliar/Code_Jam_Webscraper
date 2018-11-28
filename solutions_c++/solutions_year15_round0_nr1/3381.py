//
//  main.cpp
//  standing ovation
//
//  Created by Estelle :) on 11/4/15.
//  Copyright (c) 2015 AWESOMENESS. All rights reserved.
//

#include <iostream>

int main() {
    int t;
    freopen("/Users/student/Downloads/A-large.in", "r", stdin);
    scanf("%d", &t);
    for (int i=0; i<t; i++) {
        int n;
        scanf("%d", &n);
        char arr[n+1];
        scanf("%s", &arr);
        int j=0;
        int p=0;
        int r=0;
        while (p>=j && j<n) {
            p+=(int)arr[j]-48;
            j++;
            if (p<j) {
                r+=j-p;
                p=j;
            }
        }
        printf("Case #%d: %d\n", i+1, r);
    }
}
