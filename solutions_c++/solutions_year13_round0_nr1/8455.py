#include <iostream>
#include <stdio.h>

using namespace std;

char matrix[4][4];


int judge(){
    bool hasEmptyGrid = false;
    for(int i = 0; i < 4; i++){
        char own = matrix[i][0];
        bool isOk = true;
        for(int j = 1; j < 4; j++){
            if (own == 'T'){
                own = matrix[i][j];
            }
            if(matrix[i][j] != 'T'){
                if(own == '.' || matrix[i][j] != own){
                    if (matrix[i][j] == '.')
                        hasEmptyGrid = true;
                    isOk = false;
                    break;
                }
            }
        }
        if (isOk){
            if (own == 'X')
                return 1;
            else
                return 2;
        }
        own = matrix[0][i];
        isOk = true;
        for(int j = 1; j < 4; j++){
            if (own == 'T'){
                own = matrix[j][i];
            }
            if(matrix[j][i] != 'T'){
                if(own == '.' || matrix[j][i] != own){
                    if (matrix[j][i] == '.')
                        hasEmptyGrid = true;
                    isOk = false;
                    break;
                }
            }
        }
        if (isOk){
            if (own == 'X')
                return 1;
            else
                return 2;
        }
    }
    char own = matrix[3][0];
    bool isOk = true;
    for(int i = 2, j = 1; i >= 0; i--,j++){
        if (own == 'T')
            own = matrix[i][j];
        if(matrix[i][j] != 'T'){
            if(own == '.' || matrix[i][j] != own){
                isOk = false;
                break;
            }
        }
    }
    if (isOk){
        if (own == 'X')
            return 1;
        else
            return 2;
    }

    own = matrix[0][0];
    isOk = true;
    for(int i = 1, j = 1; i <= 3; i++,j++){
        if (own == 'T')
            own = matrix[i][j];
        if(matrix[i][j] != 'T'){
            if(own == '.' || matrix[i][j] != own){
                isOk = false;
                break;
            }
        }
    }
    if (isOk){
        if (own == 'X')
            return 1;
        else
            return 2;
    }
    if( hasEmptyGrid )return 3;
    return 4;
}
int main(){
    int t;
    scanf("%d", &t);
    for(int c = 1; c <=t; c++){

        for(int i = 0; i < 4; i++)
            scanf("%s", matrix[i]);

        printf("Case #%d: ", c);
        int x = judge();
        if (x == 1)
            printf("X won\n");
        else if(x == 2)
            printf("O won\n");
        else if(x == 3)
            printf("Game has not completed\n");
        else if(x == 4)
            printf("Draw\n");
    }
}
