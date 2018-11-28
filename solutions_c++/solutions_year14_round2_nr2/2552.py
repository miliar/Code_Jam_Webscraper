#include <stdio.h>
#include <stdlib.h>
using namespace std;
FILE *answer;

int program(){
    int a, b, k, x = 0; scanf("%d%d%d", &a, &b, &k);
    for (int i=0; i<a; i++)
        for (int j=0; j<b; j++)
            if ((i&j) < k)
                x++;
    return x;
}

int main()
{
    answer = fopen("./answer.in", "w");
    int t; scanf("%d", &t);
    for (int i=1; i<=t; i++)
        fprintf(answer, "Case #%d: %d\n", i, program());

        fclose (answer);
    return 0;
}

