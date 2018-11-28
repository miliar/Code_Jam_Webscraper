//
//  main.cpp
//  google_Codjam_2016
//
//  Created by Sunghyo Chung on 4/9/16.
//  Copyright © 2016 Sunghyo Chung. All rights reserved.
//

#include <iostream>
#include <math.h>
#define ll long long
//__int128
using namespace std;

ll checkarr[9];

ll convert(ll num, int base) {
    
    ll convertval = 0;
    int iter = 0;
    
    while(num > 0) {
        
        ll digit = num % 10;
        convertval = convertval + digit*pow(base, iter);
        num = num / 10;
        iter++;
    }
    
    return convertval;
}

ll binarytodecimal(ll num) {
    
    ll convertval = 0;
    int iter = 0;

    while(num > 0) {
        
        ll digit = num % 2;
        convertval = convertval + digit*pow(10, iter);
        num = num / 2;
        iter++;
    }
    
    return convertval;
}

ll isPrime(ll num, int base) {
    
    if(num == 1)
        return 1;
    
    for(ll i=2; i<=sqrt(num); i++) {
        
//        ll div = convert(i, base);
        if (num % i == 0)
            return i;
    }
    
    //prime
    return -1;
}

void printarr() {
    for(int i = 0; i<9; i++)
        printf("%lld ", checkarr[i]);
    printf("\n");
}

void initarr() {
    for(int i = 0; i<9; i++)
        checkarr[i] = 0;
}

int main() {
    
    int T, N, J;
    
    freopen("sample.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    scanf("%d", &T);
    scanf("%d", &N);
    scanf("%d", &J);
    
    printf("Case #%d:\n", T);
    
    ll startval = pow(10, N-1)+1;
    int count = 0;
    
    while(1) {
        
        initarr();
        bool jam = true;
        
        for(int base=2; base<=10; base++) {
            ll cv = convert(startval, base);
            ll divisor = isPrime(cv, base);

            if(divisor == -1) {
                jam = false;
                break;
            }
            else {
                checkarr[base-2] = divisor;
            }
            
        }
        
        if(jam) {
            printf("%lld ", startval);
            printarr();
            
            count++;
            if(count >= J)
                break;
        }
        
        ll addb = convert(startval, 2);
        addb = addb+2;
        startval = binarytodecimal(addb);

    }
    
    
//    startval = 100011;
////    printf("%lld ", startval);
//    for(int base=2; base<=10; base++) {
//        ll cv = convert(startval, base);
//        
//        printf("%lld ", cv);
////        printf("\n");
//        
//        ll divisor = isPrime(cv, base);
//
//        checkarr[base-2] = divisor;
//        
//    }
//    printf("\n");
//
//    printarr();


    return 0;
}