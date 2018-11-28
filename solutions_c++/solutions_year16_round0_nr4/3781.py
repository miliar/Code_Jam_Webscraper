//
// Created by Alan Peixinho on 4/9/16.
//

#include <stdio.h>
#include <math.h>

int t;
int k, c, s;

int main() {

    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        scanf("%d%d%d", &k, &c, &s);
        printf("case #%d:", i+1);
        if(s<k) {
            printf(" IMPOSSIBLE\n");
        }
        else {
            unsigned long int jump = pow(k, c-1);
            for (unsigned long int i = 0; i < k; ++i) {
                printf(" %lu", i*jump + 1ul);
            }
            printf("\n");
        }
    }

}