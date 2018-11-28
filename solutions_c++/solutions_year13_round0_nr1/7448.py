#include <cstdio>
#include <cstdlib>

int c=1;
int total=0;
FILE* output = fopen("AOutput.txt", "w");
int checkHorizontal(char grid[4][4]){
    char curr='.', letter;
    int freq=0;
    for(int i=0; i<4; i++){
        freq=0;
        for(int j=0; j<4; j++){
            if(grid[i][j]!='.'){
                total++;
                //fprintf(output, "[%c] ", grid[i][j]);
                if(grid[i][j]=='T' || curr=='T'){
                    curr = grid[i][j];
                    freq++;
                }
                else if(curr!=grid[i][j]){
                    curr=grid[i][j];
                    freq=1;
                }
                else if(curr==grid[i][j]){
                    freq++;
                }
                if(grid[i][j]!='T')letter = grid[i][j];
                //fprintf(output, "%d \n", freq);
            }

        }
       // fprintf(output, "horizontal %d %c\n", freq, letter );
        if(freq==4){
            fprintf(output, "Case #%d: %c won\n", c, letter);
            //fprintf(output, "Horizontal\n");
            return 1;
        }
    }
    return 0;
}

int checkVertical(char grid[4][4]){
    char curr='.', letter;
    int freq=0;
    for(int i=0; i<4; i++){
        freq=0;
        for(int j=0; j<4; j++){
            if(grid[j][i]!='.'){
               // fprintf(output, "[%c] ", grid[j][i]);
                if(grid[j][i]=='T' || curr=='T'){
                    curr = grid[j][i];
                    freq++;
                }
                else if(curr!=grid[j][i]){
                    curr=grid[j][i];
                    freq=1;
                }
                else if(curr==grid[j][i]){
                    freq++;
                }
                if(grid[j][i]!='T')letter = grid[j][i];
                //fprintf(output, "%d \n", freq);
            }

        }
        //fprintf(output, "vertical %d %c\n", freq, letter );
        if(freq==4){
            fprintf(output, "Case #%d: %c won\n", c, letter);
            //fprintf(output, "vertical\n");
            return 1;
        }
    }
    return 0;
}

int checkDiagonal(char grid[4][4]){
    char curr='.', letter;
    int freq=0;
    for(int i=0; i<4; i++){
        if(grid[i][i]!='.'){
            //fprintf(output, "[%c] ", grid[i][i]);
            if(grid[i][i]=='T' || curr=='T'){
                curr = grid[i][i];
                freq++;
            }
            else if(curr!=grid[i][i]){
                curr=grid[i][i];
                freq=1;
            }
            else if(curr==grid[i][i]){
                freq++;
            }
            if(grid[i][i]!='T')letter = grid[i][i];
            //fprintf(output, "%d \n", freq);
        }
    }
    //fprintf(output, "diagonal1 %d %c\n", freq, letter );
    if(freq==4){
        fprintf(output, "Case #%d: %c won\n", c, letter);
        //fprintf(output, "diagonal\n");
        return 1;
    }
    return 0;
}

int checkDiagonal2(char grid[4][4]){
    char curr='.', letter;
    int freq=0;
    for(int i=0, j=3; i<4; i++, j--){
        if(grid[i][j]!='.'){
            //fprintf(output, "[%c] ", grid[i][j]);
            if(grid[i][j]=='T' || curr=='T'){
                curr = grid[i][j];
                freq++;
            }
            else if(curr!=grid[i][j]){
                curr=grid[i][j];
                freq=1;
            }
            else if(curr==grid[i][j]){
                freq++;
            }
            if(grid[i][j]!='T')letter = grid[i][j];
            //fprintf(output, "%d \n", freq);
        }
    }
    //printf("diagonal2 %d %c\n", freq, letter );
    if(freq==4){
        fprintf(output, "Case #%d: %c won\n", c, letter);
        //printf("diagonal2\n");
        return 1;
    }
    return 0;
}

int main (){
    int n;
    char blank[10];
    scanf("%d", &n);
    getchar();

    while(c<=n){
        total=0;
        char grid[4][4];
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                scanf("%c", &grid[i][j]);
            }
            getchar();
        }

        if(checkHorizontal(grid)==0){
            if(checkVertical(grid)==0){
                if(checkDiagonal(grid)==0){
                    if(checkDiagonal2(grid)==0){
                        //fprintf(output, "Total : %d\n", total);
                        if(total==16){
                            fprintf(output, "Case #%d: Draw\n", c);
                        }
                        else fprintf(output, "Case #%d: Game has not completed\n", c);
                    }
                }
            }
        }

        gets(blank);
        //fprintf(output, "Done\n");
        c++;
    }
    fclose(output);

    return 0;
}
