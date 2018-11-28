//
//  main.cpp
//  google_Codjam_2016
//
//  Created by Sunghyo Chung on 4/9/16.
//  Copyright © 2016 Sunghyo Chung. All rights reserved.
//

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool checkarr[10];

void initarr() {
    for(int i = 0; i<10; i++)
        checkarr[i] = false;
}

void printarr() {
    for(int i = 0; i<10; i++)
        printf("%d ", checkarr[i]);
    printf("\n");

}

void markarr(int num) {
    
    while(num > 0) {
        
        int digit = num % 10;
        checkarr[digit] = true;
        num = num / 10;
    }
}

bool donechecking() {
    for(int i = 0; i<10; i++)
        if(checkarr[i] == false)
            return false;
    
    return true;
}

int main() {
    
    int T;
    int test_case;
    
    freopen("A-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    setbuf(stdout, NULL);
    scanf("%d", &T);
    
    for(test_case = 1; test_case <= T; ++test_case) {
        
        initarr();
        
        int N;
        scanf("%d", &N);
        
        if(N==0) {
            printf("Case #%d: INSOMNIA\n", test_case);
            continue;
        }
        
        int i=1;
        
        while(1) {
            markarr(N*i);
            if(donechecking())
                break;
            else
                i++;
        }
        
        printf("Case #%d: %d\n", test_case, i*N);

    }
    
    return 0;
}