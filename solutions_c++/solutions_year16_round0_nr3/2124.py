//
//  main.cpp
//  CodeJam2016
//
//  Created by Young Seok Kim on 4/9/16.
//  Copyright © 2016 TonyKim. All rights reserved.
//

#include <iostream>
#include <string.h>
#include "bigint.cpp"

using namespace std;


int T;


bigint convertToBase(bigint n, int base) {
    bigint ans = 0;
    bigint multiplier = 1;
    while (n != 0){
        bigint digit = n%10;
        ans += digit * multiplier;
        n /= 10;
        multiplier *= base;
    }
    return ans;
}

bigint toBase10(bigint n) {
    bigint ans = 0;
    bigint multiplier = 1;
    while (n != 0){
        bigint digit = n % 2;
        ans += digit * multiplier;
        n /= 2;
        multiplier = multiplier * 10;
    }
    return ans;
}



bigint isPrime(bigint number) {
    bigint i;
    for (i=2; i*i<=number; i+=1) {
        if (number % i == 0) return i;
        // heuristic
        if (i > 1000) {
            return 0;
        }
    }
    return 0;
}





int N,J;


int main(int argc, const char * argv[]) {
    // insert code here...
    
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        
        scanf("%d %d", &N, &J);
        printf("Case #%d: \n", t);

    }
    
    bigint small = 2147483649; // 32bit
    int found = 0;
    
    while (found != 500) {
        bool shouldContinue = false;
        bigint keys[11];
        bigint basis = toBase10(small);
        
        
        for (int i=2; i<=10; i++) {
            
            bigint num = convertToBase(basis, i);
            bigint factor = isPrime(num);
            if (factor == 0) {
                // Prime case
                shouldContinue = true;
            } else {
                keys[i] = factor;
            }
                
            
            if (shouldContinue) {
                break;
            }
        }
        
        
        if (shouldContinue) {
            small += 2;
            continue;
        } else {
            // found!
//            cout << small << " ";
            cout << basis << " ";

            for (int i=2; i<=10; i++) {
                cout << keys[i] << " ";
            }
            printf("\n");
            found++;
            small += 2;
        }
    }
    return 0;
}
