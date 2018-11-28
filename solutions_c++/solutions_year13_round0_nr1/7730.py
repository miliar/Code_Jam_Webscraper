#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int T, a[4][4], cnt;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d", &T);
    getchar();
    char c;
    while(T--){
        memset(a, 0, sizeof(a));
        printf("Case #%d: ", ++cnt);
        int f_f = 1, cX, cO, cT, f_w = 0;
        for(int i=0; i<4; i++){
            cX = cO = cT = 0;
            for(int j=0; j<4;j++){
                c = getchar();
                switch(c){
                    case 'X':
                        a[i][j] = 1;
                        cX ++;
                        break;
                    case 'T':
                        a[i][j] = -1;
                        cT ++;
                        break;
                    case 'O':
                        a[i][j] = 2;
                        cO ++;
                        break;
                    case '.':
                        a[i][j] = 0;
                        f_f = 0;
                        break;
                    default:
                        break;
                }
            }
            getchar();
        }
        if(f_w == 0){
            for(int i=0; i<4;i++){
                cX = cO = cT = 0;
                for(int j=0; j<4; j++){
                    switch(a[i][j]){
                        case -1:
                            cT++;
                            break;
                        case 1:
                            cX++;
                            break;
                        case 2:
                            cO++;
                            break;
                    }
                }
                if(f_w == 0){
                    if(cX == 4 || (cX == 3 && cT == 1)){
                        printf("X won\n");
                        f_w = 1;
                        break;
                    }
                    if(cO == 4 || (cO == 3 && cT == 1)){
                        printf("O won\n");
                        f_w = 1;
                        break;
                    }
                }
            }
        }
        if(f_w == 0){
            for(int i=0; i<4;i++){
                cX = cO = cT = 0;
                for(int j=0; j<4; j++){
                    switch(a[j][i]){
                        case -1:
                            cT++;
                            break;
                        case 1:
                            cX++;
                            break;
                        case 2:
                            cO++;
                            break;
                    }
                }
                if(f_w == 0){
                    if(cX == 4 || (cX == 3 && cT == 1)){
                        printf("X won\n");
                        f_w = 1;
                        break;
                    }
                    if(cO == 4 || (cO == 3 && cT == 1)){
                        printf("O won\n");
                        f_w = 1;
                        break;
                    }
                }
            }
        }
        if(f_w == 0){
            cX = cO = cT = 0;
            for(int j=0; j<4; j++){
                switch(a[j][j]){
                    case -1:
                        cT++;
                        break;
                    case 1:
                        cX++;
                        break;
                    case 2:
                        cO++;
                        break;
                }
            }
            if(f_w == 0){
                if(cX == 4 || (cX == 3 && cT == 1)){
                    printf("X won\n");
                    f_w = 1;
                    getchar();
                    continue;
                }
                if(cO == 4 || (cO == 3 && cT == 1)){
                    printf("O won\n");
                    f_w = 1;
                    getchar();
                    continue;
                }
            }
        }
        if(f_w == 0){
            cX = cO = cT = 0;
            for(int j=0; j<4; j++){
                switch(a[j][3-j]){
                    case -1:
                        cT++;
                        break;
                    case 1:
                        cX++;
                        break;
                    case 2:
                        cO++;
                        break;
                }
            }
            if(f_w == 0){
                if(cX == 4 || (cX == 3 && cT == 1)){
                    printf("X won\n");
                    f_w = 1;
                    getchar();
                    continue;
                }
                if(cO == 4 || (cO == 3 && cT == 1)){
                    printf("O won\n");
                    f_w = 1;
                    getchar();
                    continue;
                }
            }
        }
        if(f_w == 0){
            if(f_f ) printf("Draw\n");
            else printf("Game has not completed\n");
        }
        getchar();
    }
    return 0;
}
