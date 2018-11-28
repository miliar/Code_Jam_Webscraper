//
//  main.cpp
//  CodeJam2016
//
//  Created by Young Seok Kim on 4/9/16.
//  Copyright © 2016 TonyKim. All rights reserved.
//

#include <iostream>
#include <string.h>


int T;

char result[105];


void swap(int j) {
    char temp[105];
    for (int i=0; i<=j; i++) {
        temp[i] = result[j-i];
    }
    for (int i=0; i<=j; i++) {
        if (temp[i] == '+') {
            result[i] = '-';
        } else {
            result[i] = '+';
        }
    }
}

int findPlus() {
    int index = 0;
    while (result[index] == '+') {
        index++;
    }
    return index -1;
}


int function(char k[], int len) { //  0 ~ len-1
    if (len == 1) {
        if (k[0] == '+') {
            return 0;
        } else {
            return 1;
        }
    }
    
    
    if (k[len-1] == '+') {
        return function(k, len-1);
    } else { // when k[len-1] == '-'
        if (k[0] == '+') {
            swap(findPlus());
            return function(k, len) + 1;
        } else { // when k[0] == "-"
            swap(len-1);
            return function(k, len) + 1;
        }
    }
}


int main(int argc, const char * argv[]) {
    // insert code here...
    
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%s", result);
        
        
        printf("Case #%d: ", t);
        
        printf("%d\n", function(result, strlen(result)));
    }

    return 0;
}
