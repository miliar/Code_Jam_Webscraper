//
// Created by Alan Peixinho on 4/9/16.
//

#include <string.h>
#include <stdio.h>


int pancakeSort(int *pancakes, int n) {
    int nflips = 0;
    int flipSign = 1;

    for(;;) {
        n--;

        //find the blank
        while(n>=0 && (pancakes[n]*flipSign)>0)
            n--;

        if(n<0)
            return nflips;

        //if not in the end, we have to flip
        nflips++;
        flipSign*=-1;
    }
}


char s[105];
int pancakes[105];


int readPancakes() {
    scanf("%s", s);
    int n=strlen(s);
    for (int i = 0; i < n; ++i) {
        pancakes[i] = s[i]=='+'?1:-1;
    }
    return n;
}

int main() {
    int t;
    scanf("%d", &t);

    for(int c =0; c <t; ++c) {
        int n = readPancakes();
        int nflips = pancakeSort(pancakes, n);
        printf("case #%d: ", c +1);
        printf("%d\n", nflips);
    }
}

