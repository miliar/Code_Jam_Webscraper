#include <iostream>
#include <stdio.h>
#include <stdlib.h>

#define MAXUS 1001
using namespace std;

int input[MAXUS];
int c, turns;

void compute(int x) {
    if (input[x] > 0) {
        if (x + c < turns) {
            turns = x + c;
        }
        if (x < 4) return;

        c += input[x];
        for (int i = x/2; i > 0; --i) {
            input[x - i] += input[x];
            input[i] += input[x];
            compute(x-1);
            input[x - i] -= input[x];
            input[i] -= input[x];
        }
        c -= input[x];
    } else {
        if (x == 0) {
           return;
        }
        compute(x-1);
    }
}


int main() {
    int z,n,in;
    scanf("%d",&z);
    for (int j = 0; j < z; j++) {
        scanf("%d", &n);
        int pmax = -1;
        c = 0;
        turns = MAXUS;
        memset(input, 0, sizeof(int)*MAXUS);
        for (int i = 0; i < n; i++) {
            scanf("%d",&in);
            input[in]++;
            if (pmax < in) pmax = in;
        }
        compute(pmax);
        printf("Case #%d: %d\n", j+1, turns);
    }

	return 0;
}
