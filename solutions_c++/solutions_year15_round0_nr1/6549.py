//
//  main.cpp
//  CodeJam
//
//  Created by Young Seok Kim on 4/12/15.
//  Copyright (c) 2015 TonyKim. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>


int testcases;
int audience[1010];


int main(int argc, const char * argv[]) {
    
    freopen("A-large.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int t;
    
    
    
    scanf("%d", &testcases);
    for (t=1; t<=testcases; t++) {
        int n,k;
        scanf("%d ", &n);
        
        for (k=0; k<=n; k++) {
            char temp;
            scanf("%c", &temp);
            audience[k] = temp-'0';
        }
        
        
        int total = 0;
        int need = 0;
        for (k=0; k<=n; k++) {
            if (audience[k] == 0) {
                continue;
            }
            
            if (total>=k) {
                total+=audience[k];
            } else {
                need += k-total;
                total += k-total;
                total += audience[k];
            }
        }
        printf("Case #%d: %d\n", t, need);
    }
    
    
    
    
    
    return 0;
}
