#include <stdio.h>

int numeroTestes;
char tabuleiro[4][4];

bool testarLinhas(char jogador){
    for(int i = 0; i < 4; i++){
        if((tabuleiro[i][0] == jogador || tabuleiro[i][0] == 'T') &&
           (tabuleiro[i][1] == jogador || tabuleiro[i][1] == 'T') &&
           (tabuleiro[i][2] == jogador || tabuleiro[i][2] == 'T') &&
           (tabuleiro[i][3] == jogador || tabuleiro[i][3] == 'T'))
           return true;
        if((tabuleiro[0][i] == jogador || tabuleiro[0][i] == 'T') &&
           (tabuleiro[1][i] == jogador || tabuleiro[1][i] == 'T') &&
           (tabuleiro[2][i] == jogador || tabuleiro[2][i] == 'T') &&
           (tabuleiro[3][i] == jogador || tabuleiro[3][i] == 'T'))
           return true;
    }
    if((tabuleiro[0][0] == jogador || tabuleiro[0][0] == 'T') &&
           (tabuleiro[1][1] == jogador || tabuleiro[1][1] == 'T') &&
           (tabuleiro[2][2] == jogador || tabuleiro[2][2] == 'T') &&
           (tabuleiro[3][3] == jogador || tabuleiro[3][3] == 'T'))
           return true;
    if((tabuleiro[0][3] == jogador || tabuleiro[0][3] == 'T') &&
           (tabuleiro[1][2] == jogador || tabuleiro[1][2] == 'T') &&
           (tabuleiro[2][1] == jogador || tabuleiro[2][1] == 'T') &&
           (tabuleiro[3][0] == jogador || tabuleiro[3][0] == 'T'))
           return true;
    return false;
}

bool testarTerminou(){
    for(int j = 0; j < 4; j++){
        for(int k = 0; k < 4; k++){
            if(tabuleiro[j][k] == '.'){
                return false;
            }
        }
    }
    return true;
}

int main()
{
    scanf("%d", &numeroTestes);
    for(int i = 1; i <= numeroTestes; i++){
        for(int j = 0; j < 4; j++){
            scanf("%s", tabuleiro[j]);
        }

        if(testarLinhas('X'))
            printf("Case #%d: X won\n", i);
        else if(testarLinhas('O'))
            printf("Case #%d: O won\n", i);
        else if(testarTerminou())
            printf("Case #%d: Draw\n", i);
        else
            printf("Case #%d: Game has not completed\n", i);

    }
    return 0;
}
