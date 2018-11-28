//
//  main.cpp
//  Project2
//
//  Created by Gabriel Gaudreau on 2016-04-09.
//  Copyright © 2016 Gabriel Gaudreau. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdint.h>

uint32_t find_turns(char* str){
    uint32_t len = strlen(str);
    uint32_t i;
    uint32_t turns = 0;
    for(i=0; i<(len-1); i++){
        turns += str[i] != str[i+1];
    }
    if(str[len-1] == '-'){
        turns++;
    }
    return turns;
}

int main(int argc, char** argv){
    uint32_t n_cases = 0;
    uint32_t i = 0;
    scanf("%d", &n_cases);
    for(i=0; i<n_cases; i++){
        char str[101];
        scanf("%s", &str);
        printf("Case #%d: %d\n", i+1, find_turns(str));
    }
    return 0;
}