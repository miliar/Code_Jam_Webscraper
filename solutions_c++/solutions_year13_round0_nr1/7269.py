#include <cstdio>

int main() {
    int t, i, j, caso;
    int count_O, count_X, count_T, count_dot;
    int ganhou; /* 0 = empate, 1 = X ganha, 2 = O ganha, -1 = jogo não acabou */ 
    char game[4][4];
    scanf("%d",&t);
    caso = 1;
    while (t--) {
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                scanf(" %c",&game[i][j]);
            }
        }
        /* conta quantos X, O e T tem nas linhas */
        ganhou = -1;
        count_dot = 0;
        for (i = 0; i < 4; i++) {
            if (ganhou != -1)
                break;
            count_O = 0;
            count_T = 0;
            count_X = 0;
            for (j = 0; j < 4; j++) {
                if (game[i][j] == 'X')
                    count_X++;
                if (game[i][j] == 'T')
                    count_T++;
                if (game[i][j] == 'O')
                    count_O++;
                if (game[i][j] == '.')
                    count_dot++;
            }
            if ((count_X == 3 && count_T == 1) || (count_X == 4))
                ganhou = 1;
            if ((count_O == 3 && count_T == 1) || (count_O == 4))
                ganhou = 2;
        }

        /* conta quantos X, O e T tem nas colunas */
        if (ganhou == -1) {
            for (i = 0; i < 4; i++) {
                if (ganhou != -1)
                    break;
                count_X = 0;
                count_T = 0;
                count_O = 0;
                for (j = 0; j < 4; j++) {
                    if (game[j][i] == 'X')
                        count_X++;
                    if (game[j][i] == 'T')
                        count_T++;
                    if (game[j][i] == 'O')
                        count_O++;
                    if (game[i][j] == '.')
                        count_dot++;
                }
                if ((count_X == 3 && count_T == 1) || (count_X == 4))
                    ganhou = 1;
                if ((count_O == 3 && count_T == 1) || (count_O == 4))
                    ganhou = 2;
            }
        }

        /* Conta quantos x, o e t tem na diagonal principal */
        if (ganhou == -1) {
            count_X = 0;
            count_T = 0;
            count_O = 0;
            for (i = 0; i < 4; i++) {
                if (game[i][i] == 'X')
                    count_X++;
                if (game[i][i] == 'T')
                    count_T++;
                if (game[i][i] == 'O')
                    count_O++;
            }
            if ((count_X == 3 && count_T == 1) || (count_X == 4))
                ganhou = 1;
            if ((count_O == 3 && count_T == 1) || (count_O == 4))
                ganhou = 2;
        }

        /* conta as paradas na diagonal secundaria */
        if (ganhou == -1) {
            count_X = 0;
            count_T = 0;
            count_O = 0;
            for (i = 0; i < 4; i++) {
                if (game[i][3-i] == 'X')
                    count_X++;
                if (game[i][3-i] == 'T')
                    count_T++;
                if (game[i][3-i] == 'O')
                    count_O++;
            }
            if ((count_X == 3 && count_T == 1) || (count_X == 4))
                ganhou = 1;
            if ((count_O == 3 && count_T == 1) || (count_O == 4))
                ganhou = 2;
        }

        /* verifica se o jogo não acabou */
        if (ganhou == -1 && count_dot == 0)
            ganhou = 0;
        /* impressao dos casos*/ 
        printf("Case #%d: ", caso);
        if (ganhou == 1)
            printf("X won\n");
        else if (ganhou == 2)
            printf("O won\n");
        else if (ganhou == 0)
            printf("Draw\n");
        else 
            printf("Game has not completed\n");
        caso++;
    }
    return 0;
}
