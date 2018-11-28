#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

int bord[4][4];

ifstream file ("A-large.in");

void getInputs(){
    for(int j=0; j<4; j++){
            string temp;
            file >> temp;
            for(int k=0; k<4; k++){
                if(temp[k] == '.'){
                    bord[j][k] = 0;
                }
                else if(temp[k] == 'O'){
                    bord[j][k] = 1;
                }
                else if(temp[k] == 'X'){
                    bord[j][k] = 2;
                }
                else if(temp[k] == 'T'){
                    bord[j][k] = 3;
                }
            }
    }
}

bool checkDraw(){
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if(bord[i][j] == 0){
                return false;
            }
        }
    }
    return true;
}

int checkRows(){
    for(int i=0; i<4; i++){
        bool ok = true;
        int comp = bord[i][0];
        if(comp == 3){
            comp = bord[i][1];
        }
        if(comp != 0){
            for(int j=0; j<4; j++){
                if(comp != bord[i][j] && bord[i][j] != 3){
                    ok = false;
                    break;
                }
            }
            if(ok){
                return comp;
            }
        }
    }
    return 0;
}

int checkCols(){
    for(int i=0; i<4; i++){
        bool ok = true;
        int comp = bord[0][i];
        if(comp == 3){
            comp = bord[1][i];
        }
        if(comp != 0){
            for(int j=0; j<4; j++){
                if(comp != bord[j][i] && bord[j][i] != 3){
                    ok = false;
                    break;
                }
            }
            if(ok){
                return comp;
            }
        }
    }
    return 0;
}

int checkDias(){
    int comp = bord[0][0];
    if(comp == 3){
        comp = bord[1][1];
    }
    bool ok = true;
    if(comp != 0){
        for(int i=0; i<4; i++){
            if(comp != bord[i][i] && bord[i][i] != 3){
                ok = false;
                break;
            }
        }
        if(ok){
            return comp;
        }
    }
    comp = bord[0][3];
    if(comp == 3){
        comp = bord[1][2];
    }
    if(comp != 0){
        ok = true;
        for(int i=0; i<4; i++){
            if(comp != bord[i][3-i] && bord[i][3-i] != 3){
                //printf("Found err at %d %d\n", i, 3-i);
                ok = false;
                break;
            }
        }
        if(ok){
            return comp;
        }
    }
    return 0;
}

int main()
{
    int T;
    int nip;
    file >> nip;
    FILE *f = fopen("A-large.in", "r");
    FILE *out = fopen("out.out", "w");
    fscanf(f, "%d", &T);
    for(int i=0; i<T; i++){
        getInputs();
        fprintf(out, "Case #%d: ", i+1);
        //fprintf(out, "Checkrows == %d\n", checkRows());
        if(checkRows() != 0){
            if(checkRows() == 1){
                fprintf(out, "O won\n");
            }
            else if(checkRows() == 2){
                fprintf(out, "X won\n");
            }
        }
        else if(checkCols() != 0){
            if(checkCols() == 1){
                fprintf(out, "O won\n");
            }
            else if(checkCols() == 2){
                fprintf(out, "X won\n");
            }
        }
        else if(checkDias() != 0){
            if(checkDias() == 1){
                fprintf(out, "O won\n");
            }
            else if(checkDias() == 2){
                fprintf(out, "X won\n");
            }
        }
        else if(checkDraw()){
            fprintf(out, "Draw\n");
        }
        else{
            fprintf(out, "Game has not completed\n");
        }
    }
    return 0;
}
