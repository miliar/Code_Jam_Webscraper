#include <stdio.h>

int main(){
    int t, n;

    scanf ("%d", &t);

    for (int k=1; k<=t; k++){
        printf ("Case #%d: ", k);

        scanf("%d", &n);

        if (n == 0){
            printf ("INSOMNIA\n");
            continue;
        }

        bool used[15];
        int used_c = 0, p = 1;
        for (int i=0; i<=9; i++)
            used[i] = false;

        while (used_c < 10){
            int m = p*n;

            while (m > 0){
                int alg = m%10;
                if (!used[alg]) used_c++;
                used[alg] = true;
                m /= 10;
            }

            p++;
        }

        printf ("%d\n", (p-1)*n);
    }

    return 0;
}
