#include <stdio.h>
int vet[10];
int main(){
    int t, n, num;
    int i, c = 1, j = 0, digito, digitos = 0, res, numres;
    scanf("%d", &t);

    for(i = 1; i <= t; ++i){
        scanf("%d", &n);
        if(n == 0){
            printf("CASE #%d: INSOMNIA\n", i);
        }else{
            c = 1;
            while(1){
                num = n*c;
                numres = num;

                while(1){
                    digito = num % 10;
                    num /= 10;
                    vet[digito]++;
                    if(vet[digito] == 1){
                        digitos++;
                    }
                    if(num == 0){
                        res = numres;
                        break;
                    }
                }
                if(digitos >= 10){
                    printf("CASE #%d: %d\n", i, res);
                    break;
                }
                c++;
            }
        }

        digitos = 0;
        for(j = 0; j <= 10; ++j){
            vet[j] = 0;
        }
    }

    return 0;
}
