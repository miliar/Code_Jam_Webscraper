//
//  main.cpp
//  Osmos
//
//  Created by Ignas Kancleris on 2013-05-04.
//  Copyright (c) 2013 Ignas Kancleris. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[])
{

    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    
    int t;
    scanf("%i", &t);
    for (int i = 0; i < t; i++) {
        long long a, n;
        scanf("%lli %lli", &a, &n);
        //printf("%lli %lli \n", a, n);
        long long sizes[n];
        for (int c = 0; c < n; c++) {
            scanf("%lli", &sizes[c]);
            //printf("%lli ", sizes[c]);
        }
        //printf("\n\n");
        
        sort(sizes, sizes+n);
        
        long long best = n;
        int current = 0;
        if (a != 1) {
            for (int b = 0; b < n; b++) {
                if (a > sizes[b]) {
                    a += sizes[b];
                }else{
                    while (a <= sizes[b]) {
                        a += a-1;
                        current++;
                    }
                    //printf("%lli \n", best);
                    a += sizes[b];
                }
                best = min(best, current + n-b-1);
            }
        }else{
            best = n;
        }
        
        printf("Case #%i: %lli \n", i+1, best);
        
    }
    return 0;
}

