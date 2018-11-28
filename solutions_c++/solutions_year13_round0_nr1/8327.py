#include <cstdio>
#include <cstdlib>
#define eq(x,y) opc == board[x][y] || board[x][y] == 'T'
using namespace std;

int board[4][4];

int validate(int i, int j, char opc){
    int count = 0;
    for(int jj = j; jj < 4 && eq(i, jj); jj++)
        count++;
    if(count == 4) return 1;
    else count = 0;
    for(int jj = j; jj >= 0 && eq(i, jj); jj--)
        count++;
    if(count == 4) return 1;
    else count = 0;
    for(int ii = i; ii < 4 && eq(ii, j); ii++)
        count++;
    if(count == 4) return 1;
    else count = 0;
    for(int ii = i; ii >= 0 && eq(ii, j); ii--)
        count++;
    if(count == 4) return 1;
    else count = 0;
    for(int ii = i, jj = j; ii >= 0 && jj < 4 && eq(ii, jj); ii--, jj++)
        count++;
    if(count == 4) return 1;
    else count = 0;
    for(int ii = i, jj = j; ii < 4 && jj < 4 && eq(ii, jj); ii++, jj++)
        count++;
    if(count == 4) return 1;
    else count = 0;
    for(int ii = i, jj = j; ii < 4 && jj >= 0 && eq(ii, jj); ii++, jj--)
        count++;
    if(count == 4) return 1;
    else count = 0;
    for(int ii = i, jj = j; ii >= 0 && jj >= 0 && eq(ii, jj); ii--, jj--)
        count++;
    if(count == 4) return 1;
    return 0;
}

int main(){
    FILE *f = fopen("out.txt", "w");
    int cases = 0, c = 0;
    scanf("%d", &cases);
    while(c++ < cases){
        int empty = 0;
        fprintf(f,"Case #%d: ", c);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4;){
                char tile;
                scanf("%c", &tile);
                if(tile == '.' || tile == 'X' || tile == 'O' || tile == 'T')
                    board[i][j++] = tile;
                if(tile == '.') empty = 1;
            }
        }
        
        for(int i =0;i<4;i++){
            for(int j=0;j<4;j++){
                printf("%c",board[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        printf("Case #%d: ", c);
        int xopc = 0, oopc = 0;
        for(int i = 0; i < 4 && xopc == 0 && oopc == 0; i++){
            for(int j = 0; j < 4 && xopc == 0 && oopc == 0; j++){
                if(board[i][j] == 'X'){
                    xopc = validate(i, j, board[i][j]);
                }else if(board[i][j] == 'O'){
                    oopc = validate(i, j, board[i][j]);
                }
            }
        }
        if(xopc == 1){
            printf("X won\n");
            fprintf(f, "X won\n");
        }else if(oopc == 1){
            printf("O won\n");
            fprintf(f, "O won\n");
        }else if(empty == 1){
            printf("Game has not completed\n");
            fprintf(f, "Game has not completed\n");
        }else{
            printf("Draw\n");
            fprintf(f,"Draw\n");
        }
    }
}