#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>



int main(void) {

    int numCases;
    int d;
    char panStr[101];

    scanf("%d", &numCases);
    int i;
    for (i = 0; i < numCases; i++) {
        int turns = 0;
        scanf("%s", panStr);
//        printf(panStr);
//        fflush(stdout);
        int j = 1;
        while (panStr[j] != '\0')
        {
            //printf("%d, %c, %c\n", j, panStr[j], panStr[j-1]);
            if (panStr[j] != panStr[j-1]) {
                char temp[101];
                strcpy(temp, panStr);
                for (int k=0; k<j; k++) {
                    panStr[k] = (temp[j-1-k] == '+') ? '-':'+';
                //    printf("%c\n",panStr[k]);
                //    fflush(stdout);
                }
                j=1;
                turns++;
            } else{
                j++;
            }
            
        }
        if (panStr[j-1] == '-') {
            turns++;
        }
        printf("Case #%d: %d\n", i+1, turns);
        fflush(stdout);
    }

    return 0;
}