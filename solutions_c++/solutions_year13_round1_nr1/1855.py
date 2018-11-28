#include <stdio.h>

 int main() {

    long long int q, r, t;
    long long int nove, rozdiel, pocet;

    scanf("%lld", &q);

    int priklad = 1;
    while(q--)
    {
        pocet = 0;

        scanf("%lld %lld", &r, &t);


        while(1)
        {
            r++;
            nove = r*r;
            rozdiel = nove-((r-1)*(r-1));

           // printf("nove = %d, rozdiel= %d \n", nove, rozdiel);
            if(rozdiel <= t)
                pocet++;
            else
                break;

            t = t - rozdiel;
            r++;
        }

        printf("Case #%d: %lld\n", priklad++, pocet);
    }

    return 0;
 }
