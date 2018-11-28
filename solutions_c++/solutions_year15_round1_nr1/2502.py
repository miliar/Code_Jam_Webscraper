#include <iostream>
#include <stdio.h>

using namespace std;

int any(int vet[], int len){
    int i, soma = 0;

    for (i = 0 ; i < len - 1 ; i++)
        if (vet[i + 1] < vet [i])
            soma += vet[i] - vet [i + 1];

    return soma;
}

int constant(int vet[], int len){
    int i, soma = 0, rate = 0;

    for (i = 0 ; i < len - 1 ; i++)
        if (vet[i] - vet[i + 1] > rate)
            rate = vet[i] - vet[i + 1] ;

    if (rate < 10 && rate != 0)
        rate = 10;

    for (i = 0 ; i < len - 1 ;  i++){
        if (vet[i] >= rate)
            soma += rate;
        else
            soma += vet[i];
    }

    return soma;
}

int main(){
    int i, j, cases,  N,  v[20000];

    scanf("%d ", &cases);

    for (i = 0 ; i < cases ; i++){
        scanf("%d ", &N);
        for (j = 0 ; j < N ; j++)
            scanf("%d ", &v[j]);
        cout << "Case #" << i + 1 << ": " << any(v, N) << " " << constant(v, N) << endl;

    }
}

