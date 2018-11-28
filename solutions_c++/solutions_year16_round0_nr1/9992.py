//
//  project1.cpp
//  
//
//  Created by Gabriel Gaudreau on 2016-04-09.
//
//


#include <stdio.h>
#include <stdint.h>

#define LIMIT 1000

unsigned short get_digits(uint32_t num){
    uint16_t digits = 0;
    do{
        digits |= 1 << (num % 10);
        num /= 10;
    }while(num > 0);
    return digits;
}

uint32_t highest_num(uint32_t num){
    uint32_t i = 0;
    uint16_t seen_digits = 0;
    for(i=1; i<LIMIT; i++){
        seen_digits |= get_digits(i * num);
        if(0x3ff == seen_digits){
            return i * num;
        }
    }
    return 0;
}

int main(int argc, char** argv){
    uint32_t n_cases = 0;
    uint32_t i = 0;
    scanf("%d", &n_cases);
    for(i=0; i<n_cases; i++){
        uint32_t num = 0;
        uint32_t result = 0;
        scanf("%d", &num);
        result = highest_num(num);
        if(0 == result){
            printf("Case #%d: INSOMNIA\n", i+1);
        }else{
            printf("Case #%d: %d\n", i+1, result);
        }
    }
}
