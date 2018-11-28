#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>

long digits[10];

bool digitCheck() {
    bool ret = true;
    for (int i = 0; i<10; i++) {
        if (digits[i] == 0) {
            ret = false;
        }
    }
    return ret;
}

int main(void) {

    int numCases;
    int d;
    
    scanf("%d", &numCases);
    //printf("%d\n", numCases);
    //fflush(stdout);
    int i;
    for (i = 0; i < numCases; i++) {
        //printf("A\n");
        //fflush(stdout);
        char asString[20];
        memset(digits, 0x00, 10*sizeof(long));
        long long startVal = 0;
        long long curVal;
        scanf("%d", &startVal);
        //printf("%d\n", startVal);
        //fflush(stdout);
        //printf("B\n");
        //fflush(stdout);
        curVal = 0;
        if (startVal == 0) {
            //printf("C\n");
            //fflush(stdout);
            printf("Case #%d: INSOMNIA\n", i+1);
        } else {
            //printf("D\n");
            //fflush(stdout);
            while( !digitCheck()) {
                curVal += startVal;
                sprintf(asString, "%Ld", curVal);
                int j = 0;
                while (asString[j] != '\0') {
                    digits[asString[j]-'0']++;
                    j++;
                }
            }
            printf("Case #%d: %Ld\n", i+1, curVal);
        }
            
        fflush(stdout);
    }

    return 0;
}