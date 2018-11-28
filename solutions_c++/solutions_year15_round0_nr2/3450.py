#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int T;
    int D;
    int P[1000];
    scanf("%d\n",&T);
    for (int t=1;t<=T;t++) {
        scanf("%d", &D);
        for (int i=0; i<D;i++) {
            scanf("%d", &P[i]);
        }
        int best=1000;
        for (int i=1;i<=1000;i++) {
            int current=i;
            for (int j=0;j<D;j++) {
                current += (P[j]-1)/i;

            }
            if (current<best) {
                best=current;
            }
        }
        printf("Case #%d: %d\n", t, best);
    }
    return 0;
}
