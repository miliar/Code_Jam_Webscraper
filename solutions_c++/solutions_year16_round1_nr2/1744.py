#include <stdio.h>

int main(){
    int t, n, x, v[10000];

    scanf ("%d", &t);

    for (int k=1; k<=t; k++){
        scanf ("%d", &n);

        for (int i=1; i<=2500; i++)
            v[i] = 0;

        for (int i=1; i<2*n; i++){
            for (int j=1; j<=n; j++){
                scanf ("%d", &x);
                v[x]++;
            }
        }

        printf ("Case #%d:", k);

        for (int i=1; i<=2500; i++)
            if (v[i]%2 == 1) printf (" %d", i);

        printf ("\n");
    }

    return 0;
}
