#include <stdio.h>
#include <stdlib.h>
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#include <iostream>
using namespace std;

int main()
{
    int num_cases, a, b, k, num_matches, case_no = 0;
    scanf("%d", &num_cases);
    while(num_cases--)
    {
        scanf("%d %d %d", &a, &b, &k);
        num_matches = 0;
        FOR(i, 0, a)
            FOR(j, 0, b)
                num_matches += (i & j) < k ? 1 : 0;
        printf("Case #%d: %d\n", ++case_no, num_matches);
    }
    return 0;
}
