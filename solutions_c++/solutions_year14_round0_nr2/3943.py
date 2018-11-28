#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main()
{
    int loop=0;
    int i=0;

    bool flag=true;

    double C = 0.00000;
    double F = 0.00000;
    double X = 0.00000;
    double taxa = 2.000000;
    double tempo = 0.0000000000;
    double tempo_fabrica = 0.0000000000;
    double tempo_anterior = 0.0000000000;

    cin >> loop;

    for(i=0;i<loop;i++){

        scanf("%lf %lf %lf", &C, &F, &X);

        taxa = 2.000000;
        tempo = 0.0000000000;
        tempo_fabrica = 0.0000000000;
        tempo_anterior = 0.0000000000;
        flag=true;

        while(flag){

            tempo_anterior = (X/taxa) + tempo_fabrica;
            tempo_fabrica = tempo_fabrica + (C/taxa);
            taxa = taxa + F;
            tempo = (X/taxa) + tempo_fabrica;

            /*printf("tempo_anterior: %.7lf\n", tempo_anterior);
            printf("tempo_fabrica: %.7lf\n", tempo_fabrica);
            printf("taxa: %.5lf\n", taxa);
            printf("tempo: %.7lf\n", tempo);
            printf("\n"); */

            if(tempo>tempo_anterior) flag=false;

        }

        printf("Case #%d: %.7lf\n", i+1, tempo_anterior);
    }

    return 0;
}
