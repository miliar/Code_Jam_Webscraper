#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <iostream>


using namespace std;


typedef unsigned long long int ull;


int main()
{
    int T, cases = 1;
    ull N,P;

    cin >> T;
    while(T--) {
        scanf("%llu%llu",&N,&P);
        ull all = (1ull << N);
        ull NoP = all - P;
        ull p = 1;
        ull nop = 1;
        ull half = all;
        if (all == P)
        {
            printf("Case #%d: %llu %llu\n",cases++, all-1, all-1);
            continue;
        }
        while(half >>= 1)
        {
            if (P > half) {
                p = (p+1)*2-1;
                P -= half;
            } else {
                break;
            }
        }
        half = all;
        while(half >>= 1)
        {
            if (NoP > half) {
                nop = (nop+1) *2 -1;
                NoP -= half;
            } else {
                break;
            }
        }
        p = p-1;
        nop = all - nop - 1;

        printf("Case #%d: %llu %llu\n",cases++, p, nop);

    }
	return 0;
}
