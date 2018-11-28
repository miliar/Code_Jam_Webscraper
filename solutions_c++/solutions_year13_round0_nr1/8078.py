#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(){
    int casen;
    bool empty=false;
    int i,j;
    int caser=1;
    char fc[4];
    char gr[4];
    bool c[4] = {false,false,false,false};
    bool r[4] = {false,false,false,false};
    bool tc[4] = {true,true,true,true};
    bool tr[4] = {true,true,true,true};
    char matrix[4][4];
    char c1[4];
    bool ff;
    scanf("%d\n",&casen);
    while(casen--){
        empty = false;
        for(i=0;i<4;++i){
            scanf("%s\n",c1);
            //printf("%s\n",c1);
            for(j=0;j<4;++j){
                matrix[i][j] = c1[j];
                if(c1[j] == '.'){
                    empty = true;
                }
                /*
                if(i==0){
                    if(c1 != 'T'){
                        fc[j] = c1;
                        c[j] = true;
                    }
                }
                if(j == 0){
                    if(c1 != 'T'){
                        gr[i] = c1;
                        r[i] = true;
                    }                    
                }
                else{
                    if(!r[i] && c1 != 'T'){
                        r[i] = true;
                        gr[i] = c1;
                    }
                    else if(r[i]){
                        if(c1 != gr[i])
                            tr[i] = false;
                    }
                    if(!c[i] && c1 != 'T'){
                        c[i] = true;
                        fc[i] = c1;
                    }
                    else if(c[i]){
                        if(c1 != fc[i])
                            tc[i] = false;
                    }
                }
                */
            }
        }
        ff = false;
        for(i=0;i<4&&!ff;++i){
            if(matrix[i][0] != '.' && matrix[i][1] != '.' && matrix[i][2] != '.' && matrix[i][3] != '.'){
                if(matrix[i][0] == matrix[i][2] && matrix[i][0] == matrix[i][3] && matrix[i][0] == matrix[i][1]){
                    printf("Case #%d: %c won\n",caser,matrix[i][0]);
                    ff = true;
                }
                if(matrix[i][0] == matrix[i][1] && matrix[i][0] == matrix[i][2] && matrix[i][3] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[i][0]);
                    ff = true;
                }
                else if(matrix[i][0] == matrix[i][2] && matrix[i][0] == matrix[i][3] && matrix[i][1] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[i][0]);
                    ff = true;
                }
                else if(matrix[i][1] == matrix[i][2] && matrix[i][1] == matrix[i][3] && matrix[i][0] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[i][1]);
                    ff = true;
                }
            }
        }
        if(!ff){
            for(i=0;i<4&&!ff;++i){
                if(matrix[0][i] != '.' && matrix[1][i] != '.' && matrix[2][i] != '.' && matrix[3][i] != '.'){
                    if(matrix[0][i] == matrix[2][i] && matrix[0][i] == matrix[3][i] && matrix[0][i] == matrix[1][i]){
                        printf("Case #%d: %c won\n",caser,matrix[0][i]);
                        ff = true;
                    }
                    if(matrix[0][i] == matrix[1][i] && matrix[0][i] == matrix[2][i] && matrix[3][i] == 'T'){
                        printf("Case #%d: %c won\n",caser,matrix[0][i]);
                        ff = true;
                    }
                    else if(matrix[0][i] == matrix[2][i] && matrix[0][i] == matrix[3][i] && matrix[1][i] == 'T'){
                        printf("Case #%d: %c won\n",caser,matrix[0][i]);
                        ff = true;
                    }
                    else if(matrix[1][i] == matrix[2][i] && matrix[1][i] == matrix[3][i] && matrix[0][i] == 'T'){
                        printf("Case #%d: %c won\n",caser,matrix[1][i]);
                        ff = true;
                    }
                }
            }
        }
        if(!ff){
            if(matrix[0][0] != '.' && matrix[1][1] != '.' && matrix[2][2] != '.' && matrix[3][3] != '.'){
                if(matrix[0][0] == matrix[2][2] && matrix[0][0] == matrix[3][3] && matrix[0][0] == matrix[1][1]){
                    printf("Case #%d: %c won\n",caser,matrix[0][0]);
                    ff = true;
                }
                if(matrix[0][0] == matrix[1][1] && matrix[0][0] == matrix[2][2] && matrix[3][3] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[0][0]);
                    ff = true;
                }
                else if(matrix[0][0] == matrix[2][2] && matrix[0][0] == matrix[3][3] && matrix[1][1] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[0][0]);
                    ff = true;
                }
                else if(matrix[1][1] == matrix[2][2] && matrix[1][1] == matrix[3][3] && matrix[0][0] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[1][1]);
                    ff = true;
                }
            }
        }
        if(!ff){
            if(matrix[0][3] != '.' && matrix[1][2] != '.' && matrix[2][1] != '.' && matrix[3][0] != '.'){
                if(matrix[0][3] == matrix[2][1] && matrix[0][3] == matrix[3][0] && matrix[0][3] == matrix[1][2]){
                    printf("Case #%d: %c won\n",caser,matrix[0][3]);
                    ff = true;
                }
                if(matrix[0][3] == matrix[1][2] && matrix[0][3] == matrix[2][1] && matrix[3][0] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[0][3]);
                    ff = true;
                }
                else if(matrix[0][3] == matrix[2][1] && matrix[0][3] == matrix[3][0] && matrix[1][2] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[0][3]);
                    ff = true;
                }
                else if(matrix[1][2] == matrix[2][1] && matrix[1][2] == matrix[3][0] && matrix[0][3] == 'T'){
                    printf("Case #%d: %c won\n",caser,matrix[1][2]);
                    ff = true;
                }
            }
        }
        if(!ff && empty){
            printf("Case #%d: Game has not completed\n",caser);
        }
        else if(!ff){
            printf("Case #%d: Draw\n",caser);
        }
        caser++;
    }
    return 0;
}

