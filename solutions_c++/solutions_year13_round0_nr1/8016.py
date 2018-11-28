#include<stdio.h>
#include<stdlib.h>

int compare_A(const void*p, const void*q);
int compare_B(const void*p, const void*q);

int main(){
    FILE *input, *output;
    int N, i, j, k;
    int O_win, X_win, flag;
    char c;
    char board[4][4];

    input = fopen("A-small-attempt2.in", "r");
    output = fopen("outa.txt", "w");
    fscanf(input,"%d%c", &N, &c);
    for(i=1;i<=N;i++){
        O_win = 0;
        X_win = 0;
        flag = 0;
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                fscanf(input, "%c", &board[j][k]);
                if(board[j][k]=='.')
                    flag = 1;
            }
            fscanf(input, "%c", &c);
        }
        if(board[0][0]=='O'){
            if(O_win==1)
                O_win = 1;
            else{
                O_win = 1;
                for(j=1,k=1;j<4;j++,k++)
                    if(board[j][k]!='O'&&board[j][k]!='T')
                            O_win = 0;
            }
        }else if(board[0][0]=='X'){
            if(X_win==1)
                X_win = 1;
            else{
                X_win = 1;
               for(j=1,k=1;j<4;j++,k++)
                    if(board[j][k]!='X'&&board[j][k]!='T')
                        X_win = 0;
            }
        }
        if(board[0][3]=='O'){
            if(O_win==1)
                O_win = 1;
            else{
                O_win = 1;
                for(j=1,k=2;j<4;j++,k--)
                    if(board[j][k]!='O'&&board[j][k]!='T')
                        O_win = 0;
            }
        }else if(board[0][3]=='X'){
            if(X_win==1)
                X_win = 1;
            else{
                X_win = 1;
                for(j=1,k=2;j<4;j++,k--)
                    if(board[j][k]!='X'&&board[j][k]!='T')
                        X_win = 0;
            }
        }
        if(O_win==0&&X_win==0){
            for(j=0;j<4;j++){
                if(board[j][0]=='O'){
                    O_win = 1;
                    for(k=1;k<4;k++)
                        if(board[j][k]!='O'&&board[j][k]!='T')
                            O_win = 0;
                }
                if(O_win==1)
                    break;
                if(board[j][0]=='X'){
                    X_win = 1;
                    for(k=1;k<4;k++)
                        if(board[j][k]!='X'&&board[j][k]!='T')
                            X_win = 0;
                }
                if(X_win==1)
                    break;
            }
        }
        if(O_win==0&&X_win==0){
            for(j=0;j<4;j++){
                if(board[0][j]=='O'){
                    O_win = 1;
                    for(k=1;k<4;k++)
                        if(board[k][j]!='O'&&board[k][j]!='T')
                            O_win = 0;
                }
                if(O_win==1)
                    break;
                if(board[0][j]=='X'){
                    X_win = 1;
                    for(k=1;k<4;k++)
                        if(board[k][j]!='X'&&board[k][j]!='T')
                            X_win = 0;
                }
                if(X_win==1)
                    break;
            }
        }
        fscanf(input, "%c", &c);
        if(O_win==1)
            fprintf(output, "Case #%d: O won", i);
        else if(X_win==1)
            fprintf(output, "Case #%d: X won", i);
        else if(flag==1)
            fprintf(output, "Case #%d: Game has not completed", i);
        else
            fprintf(output, "Case #%d: Draw", i);
        if(i!=N)
            fprintf(output, "\n");
    }

    fclose(input);
    fclose(output);
    return 0;
}
