#include <cstdio>
#include<cstring>
char chess[5 * 5] = {'*'};//5 * Row + Col

void displayChess(int Row, int Col)
{
    for(int i = 0; i < Row; i++){
        for(int j = 0; j < Col; j++)
            printf("%c", chess[5 * i + j]);
        printf("\n");
    }
}

int countTheArea(int Row, int Col){
    int count = 0;
    for(int i = 0; i < Row; i++)
        for(int j = 0; j < Col; j++)
        {
            char temp = chess[5 * i + j];
            if(temp == 'c' || temp == '.')
                count++;
        }
    return count;
}

int setZeroPlace(int Row, int Col, int r, int c){
    chess[5*r + c] = 'c';
    for(int tempR = r - 1; tempR <= r + 1; tempR++){
        if(tempR >=0 && tempR < Row){
            for(int tempC = c - 1; tempC <= c + 1; tempC++){
                if(tempC >= 0 && tempC < Col){
                    if(chess[5 * tempR + tempC] == '*')
                        chess[5*tempR + tempC] = '.';
                }
            }
        }
    }
    return countTheArea(Row, Col);
}

bool recur(int Row, int Col, int areaWithoutMines){

    char* tempChess = new char[25];
    memcpy(tempChess, chess, sizeof(char)*25);
    for(int i = 0; i < Row; i ++){
        for(int j = 0; j < Col; j++){
            if(chess[5*i + j] == '.'){
                int temp = setZeroPlace(Row,Col, i, j);
                if(temp < areaWithoutMines){
                    if(recur(Row, Col, areaWithoutMines))
                        return true;
                }
                else if(temp == areaWithoutMines)
                    return true;
                memcpy(chess, tempChess, sizeof(char)*25);
            }
        }
    }
    return false;
}

int main(){

    int T;
    scanf("%d\n", &T);

    int count = 0;
    while(T--){

        memset(chess, '*', sizeof(char)*25);
        int Row, Col, Mine;
        scanf("%d %d %d\n", &Row, &Col, &Mine);

        int areaWithoutMines = Row * Col - Mine;
        if(Mine == 0){
            memset(chess, '.', sizeof(char)*25);
            chess[0] = 'c';
            printf("Case #%d:\n", ++count);
            displayChess(Row, Col);
        }
        else if(areaWithoutMines == 1)
        {
            chess[0] = 'c';
            printf("Case #%d:\n", ++count);
            displayChess(Row, Col);
        }
        else{
            //initial
            //with all areas fill with mines, find safe spaces
            bool flag = false;
            for(int i = 0; i < Row; i++){
                for(int j = 0; j < Col; j++){
                    int temp = setZeroPlace(Row, Col, i, j);
                    if( temp < areaWithoutMines){
                        if(recur(Row,Col,areaWithoutMines))
                            //continue;
                            goto data;
                    }
                    else if(temp == areaWithoutMines){
                        goto data;
                    }
                }
            }
            printf("Case #%d:\nImpossible\n", ++count);
            continue;
data:
            bool first = false;
            for(int i = 0; i < Row; i++)
                for(int j = 0; j < Col; j++){
                    if(chess[5 *i + j] == 'c'){
                        if(!first)
                        {
                            first = true;
                        }
                        else
                            chess[5 * i + j] = '.';
                    }
                }
            printf("Case #%d:\n", ++count);
            displayChess(Row, Col);
            //displayChess(Row, Col);
        }
    }
    return 0;
}
