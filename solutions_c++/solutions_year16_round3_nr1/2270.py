//
//  main.cpp
//  google_Codjam_2016
//
//  Created by Sunghyo Chung on 4/9/16.
//  Copyright © 2016 Sunghyo Chung. All rights reserved.
//

#include <iostream>
#include <math.h>

using namespace std;

int nmax = 26;
int people[26];


void initarr() {
    for(int i = 0; i<nmax; i++)
        people[i] = 0;
}

int findmaxindex() {
   
    int max = people[0];
    int index = 0;
    
    for(int i = 1; i<nmax; i++)
        if (people[i] > max) {
            max = people[i];
            index = i;
        }
    
    return index;
}

int findmaxval() {
    
    int max = people[0];
    int index = 0;
    
    for(int i = 1; i<nmax; i++)
        if (people[i] > max) {
            max = people[i];
            index = i;
        }
    
    return max;
}

int totalval() {
    
    int total = 0;
    
    for(int i = 0; i<nmax; i++)
        total = total + people[i];
    
    return total;
    
}

int main() {
    
    int T;
    int test_case;
    
    freopen("sample.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    setbuf(stdout, NULL);
    scanf("%d", &T);
    
    for(test_case = 1; test_case <= T; ++test_case) {
        
        initarr();
        
        int N; //n parties
        scanf("%d", &N);
        
        nmax = N;
        
        for(int i=0; i<N; i++) {
            scanf("%d", &people[i]);
        }
        
        //do something here!
        int total = totalval();
        
        printf("Case #%d:", test_case);
        
        bool two = false;
        
        while(1) {
            
            if(!two) {//false
                printf(" ");
                two = true;
            }
            
            int evacu = findmaxindex();
            
            people[evacu]--;
            total--;
            
            printf("%c", evacu+65);
            
            if(total == 0)
                break;
            
            int max = findmaxval();
            
            if(max > float(0.5 * total))
                two = true;
            else
                two = false;
            
        }
        
        printf("\n");
    }
    
    return 0;
}




