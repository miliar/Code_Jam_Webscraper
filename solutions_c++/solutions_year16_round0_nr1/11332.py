#include<stdio.h>

int main(void){

int v[110], numero=0, n, zero=0, um=0, dois=0, tres=0, quatro=0, cinco=0, seis=0, sete=0, oito=0, nove=0;

scanf("%d", &n);

for(int i=0; i < n; i++){
    scanf("%d", &v[i]);
    if(v[i] == 0){
        printf("Case #%d: INSOMNIA\n", i+1);
    }

    else{
        while(zero < 1 || um < 1 || dois < 1 || tres < 1 || quatro < 1 || cinco < 1 || seis < 1 || sete < 1 || oito < 1 || nove < 1){
            for(int j=1; 1 ; j++){
                int x = v[i]*j;
                while(x > 0){
                    int resto = x%10;
                    if(resto == 0){
                        zero++;
                    }
                    else if(resto == 1){
                        um++;
                    }
                    else if(resto == 2){
                        dois++;
                    }
                    else if(resto == 3){
                        tres++;
                    }
                    else if(resto == 4){
                        quatro++;
                    }
                    else if(resto == 5){
                        cinco++;
                    }
                    else if(resto == 6){
                        seis++;
                    }
                    else if(resto == 7){
                        sete++;
                    }
                    else if(resto == 8){
                        oito++;
                    }
                    else if(resto == 9){
                        nove++;
                    }
                    x = x/10;
                }

            if(zero > 0 && um > 0 && dois > 0 && tres > 0 && quatro > 0 && cinco > 0 && seis > 0 && sete > 0 && oito > 0 && nove > 0){
                numero = v[i]*j;
                printf("Case #%d: %d\n", i+1, numero);
                break;
            }

            }
        }
    zero = 0; um = 0; dois = 0; tres = 0; quatro = 0; cinco = 0; seis = 0; sete = 0; oito = 0; nove = 0;
    }
}
return 0;
}
