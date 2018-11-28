#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int num_add(int num, int shyness[]){
    int vet[1050], i, de_pe = 0, adiciona = 0;

    for (i = 0 ; i <= num ; i++){
        if (de_pe >= i)
            de_pe += shyness[i];
        else if (shyness[i]!= 0){
           adiciona += (i - de_pe);
           de_pe += (i - de_pe) + shyness[i];
        }

    }

    return adiciona;
}

int main(){

    int cases, num, shyness[1050], i, j, a;

    scanf("%d ", &cases);

    for (i = 1 ; i <= cases ; i++){

        scanf("%d ", &num);
        for (j = 0 ; j <= num ; j++){
            a = getchar();
            shyness[j] = a - '0';
        }
        printf("Case #%d: %d\n", i, num_add(num, shyness));
    }
    return 0;
}
