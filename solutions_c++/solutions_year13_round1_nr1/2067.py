#include <stdio.h>
#include <stdint.h>



int main()
{

    unsigned int Z;
    unsigned int C;
    int64_t T, R;
    int64_t tempsurface;
    int c, q;

    scanf("%i\n", &Z);
//    printf("Count: %I64u\n", Z);

    for (C = 1;C <= Z;C++)
    {

        scanf("%I64u %I64u \n", &R, &T);

        c = 1;
        tempsurface = 0;
        q = 0;

        tempsurface = (R+1)*(R+1) - (R*R);

//        printf(": %I64u %I64u\n", R, T);

//        printf("%i\n", tempsurface);
        while (tempsurface <= T)
        {
            R += 2;
            tempsurface += (R+1)*(R+1) - (R*R);
//            printf("%I64u\n", tempsurface);
            c++;
        }

        printf("Case #%i: %i\n", C, c-1);

    }


    return 0;
}
