#include <stdio.h>
#include <string.h>

int letras[100];
int num[10];

int main(){
    int t = 0, i, cont, tam, j = 0;
    char texto[2001];
    char res[2001];

    scanf("%d ", &t);

    for(cont = 0; cont < t; cont++){
        scanf("%s", texto);
        tam = strlen(texto);
        for(i = 0; i < tam; i++){
            letras[texto[i]]++;
        }

        while(letras['Z'] != 0){
            num[0]++;
            letras['Z']--;
            letras['E']--;
            letras['R']--;
            letras['O']--;
        }

        while(letras['W'] != 0){
            num[2]++;
            letras['T']--;
            letras['W']--;
            letras['O']--;
        }

        while(letras['X'] != 0){
            num[6]++;
            letras['S']--;
            letras['I']--;
            letras['X']--;
        }

        while(letras['G'] != 0){
            num[8]++;
            letras['E']--;
            letras['I']--;
            letras['G']--;
            letras['H']--;
            letras['T']--;
        }

        while(letras['H'] != 0){
            num[3]++;
            letras['T']--;
            letras['H']--;
            letras['R']--;
            letras['E']--;
            letras['E']--;
        }

        while(letras['R'] != 0){
            num[4]++;
            letras['F']--;
            letras['O']--;
            letras['U']--;
            letras['R']--;
        }

        while(letras['F'] != 0){
            num[5]++;
            letras['F']--;
            letras['I']--;
            letras['V']--;
            letras['E']--;
        }

        while(letras['V'] != 0){
            num[7]++;
            letras['S']--;
            letras['E']--;
            letras['V']--;
            letras['E']--;
            letras['N']--;
        }

        while(letras['O'] != 0){
            num[1]++;
            letras['O']--;
            letras['N']--;
            letras['E']--;
        }

        while(letras['N'] != 0){
            num[9]++;
            letras['N']--;
            letras['I']--;
            letras['N']--;
            letras['E']--;
        }

        printf("Case #%d: ", cont+1);

        for(i = 0; i < 10; i++){
            while(num[i] != 0){
                printf("%d", i);
                num[i]--;
            }
        }
        printf("\n");

    }

    return 0;
}
