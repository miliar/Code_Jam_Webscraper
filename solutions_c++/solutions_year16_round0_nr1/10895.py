/*********************************************************************************************
 **                                                                                         **
 ** @author         : Ilker MORAL                                                           **
 ** @version        : 1                                                                     **
 ** @email          : ilkermoral@gmail.com                                                  **
 ** @since          : Apr  9 14:41:07 2016                                                  **
 ** @compiled with  : GCC GCC4.2.1 (MacOS)                                                  **
 **                                                                                         **
 *********************************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int digits[10];

int testCase;

int checkDigit(int digit);

int main (void) {

    int numberOfCase = 1;
    
    for (int j = 0; j < 10; j++)
        digits[j] = 0;

    scanf("%d", &testCase);

        int nextNum = 0;
        
        while (scanf("%d", &nextNum) != EOF) {

            if (nextNum == 0) {
                    printf("Case #%d: INSOMNIA\n",numberOfCase++);
                    continue;
            }

            int num = nextNum;

            int k = 1;

            while (k > 0) {

                num = nextNum * k;
                
                while (num > 0) {

                    int digit = num % 10;
                    
                    if (checkDigit(digit) == 1) {

                        printf("Case #%d: %d\n", numberOfCase++, nextNum * k);

                        k = -10;

                        for (int j = 0; j < 10; j++)
                            digits[j] = 0;
                    }
        
                    if (k == -10)
                        break;
                    
                    if (num > 9)
                        num = num / 10;
                    else
                        num = 0;
                }
                if (k == -10)
                    break;
                k++;    
            }
    }
}


int checkDigit(int digit) {

    digits[digit] = 1;

    int i;

    for (i = 0; i < 10; i++) {
        
        if (digits[i] == 0)
            return 0;
    }

    return 1;
}
