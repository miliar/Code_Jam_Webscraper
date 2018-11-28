/* 
 * File:   main.cpp
 * Author: juro
 *
 * Created on April 10, 2016, 1:10 AM
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <math.h>

using namespace std;

/*
 * 
 */

long long quick_pow(long long a, long long b) {
    if (b == 0) return 1;
    return quick_pow(a * a, b/2) * (b%2 == 0 ? 1 : a);
}

int main(int argc, char** argv) {
    
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        long long k, c, s;
        
        cin >> k >> c >> s;
        
        long long step = quick_pow(k, c-1);
        printf("Case #%d: ", i+1);
        long long current = 0;
        for (int j = 0; j < s; j++) {
            printf("%lld ", current + 1);
            current += step;
        }
        printf("\n");
    
    }
    return 0;
}

