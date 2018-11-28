#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
using namespace std;

int main(void) {

    int numCases;
    char s[2001];
    
    scanf("%d", &numCases);
    int i;
    int answer;
    for (i = 0; i < numCases; i++) {
        int charCount[127];
        char outStr[800];
        int digits = 0;
        int numDigit[10];
        int n;
        cin >> s;
        int slen = strlen(s);
        memset (&charCount[0], 0, 127*sizeof(int));
        for (int j = 0; j < slen; j++) {
            charCount[s[j]]++; 
        }
        charCount['E'] -= charCount['Z'];
        charCount['R'] -= charCount['Z'];
        charCount['O'] -= charCount['Z'];
        numDigit[0] = charCount['Z'];
        charCount['Z'] = 0;

        charCount['T'] -= charCount['W'];
        charCount['O'] -= charCount['W'];
        numDigit[2] = charCount['W'];
        charCount['W'] = 0;

        charCount['E'] -= charCount['G'];
        charCount['I'] -= charCount['G'];
        charCount['H'] -= charCount['G'];
        charCount['T'] -= charCount['G'];
        numDigit[8] = charCount['G'];
        charCount['G'] = 0;

        charCount['S'] -= charCount['X'];
        charCount['I'] -= charCount['X'];
        numDigit[6] = charCount['X'];
        charCount['X'] = 0;

        charCount['E'] -= charCount['S'];
        charCount['E'] -= charCount['S'];
        charCount['V'] -= charCount['S'];
        charCount['N'] -= charCount['S'];
        numDigit[7] = charCount['S'];
        charCount['S'] = 0;

        charCount['F'] -= charCount['V'];
        charCount['I'] -= charCount['V'];
        charCount['E'] -= charCount['V'];
        numDigit[5] = charCount['V'];
        charCount['V'] = 0;

        charCount['O'] -= charCount['F'];
        charCount['U'] -= charCount['F'];
        charCount['R'] -= charCount['F'];
        numDigit[4] = charCount['F'];
        charCount['F'] = 0;

        charCount['N'] -= charCount['O'];
        charCount['E'] -= charCount['O'];
        numDigit[1] = charCount['O'];
        charCount['O'] = 0;

        charCount['H'] -= charCount['T'];
        charCount['E'] -= charCount['T'];
        charCount['E'] -= charCount['T'];
        charCount['R'] -= charCount['T'];
        numDigit[3] = charCount['T'];
        charCount['T'] = 0;

        charCount['N'] -= charCount['I'];
        charCount['N'] -= charCount['I'];
        charCount['E'] -= charCount['I'];
        numDigit[9] = charCount['I'];
        charCount['I'] = 0;
        
        printf("Case #%d: ", i+1);
        for (int k = 0; k < 10; k++) {
            for (int l = 0; l < numDigit[k]; l++) {
                printf("%d", k);
            }
        }
        printf("\n");
        fflush(stdout);
    }

    return 0;
}