#include <stdio.h>

int digitos[10];

int viu_todos(){
    int i;
    for(i=0; i<10; i++){
        if(digitos[i] == 0){
            return 0;
        }
    }
    return 1;
}

void limpar_digitos(){
    int i;
    for(i=0; i<10; i++){
        digitos[i] = 0;
    }
}

void preencher_array(int num){

    while(num){

        digitos[num%10] = 1;
        num /= 10;

    }

}

int main(){

    int n;
    int i, j, caso = 1;
    int k;

    scanf("%d", &n);

    for(i=0; i<n; i++){

        scanf("%d", &k);
        limpar_digitos();

        if(k){

            for(j=1; !viu_todos(); j++){
                preencher_array(j*k);
            }
            j--;
            printf("Case #%d: %d\n", caso, j*k);

        } else {
            printf("Case #%d: INSOMNIA\n", caso);
        }
        caso++;
    }


    return 0;
}
