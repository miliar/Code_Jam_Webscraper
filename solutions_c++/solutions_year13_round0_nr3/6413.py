#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <queue>
#include <stack>

using namespace std;

int main(void)
{
    int cases;
    int i, j;
    int table[5] = { 1, 4, 9, 121, 484};
    int upper, lower;
    int a, b;


    freopen("C-small-attempt4.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &cases);

    for (i=1; i<=cases; i++){
        scanf("%d%d", &a, &b);
        int counter = 0;
        for (j=0; j<=4; j++){
            if (table[j]>=a && table[j]<=b){
                counter++;
            }
        }

        printf("Case #%d: %d\n", i, counter);
    }
    return 0;
}
