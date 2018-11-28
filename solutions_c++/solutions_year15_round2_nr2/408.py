#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>
#include <iostream>

using namespace std;

#define INF 1000000007
#define MAXR 10000
#define MAXC 10000

int mat[MAXR][MAXC];
int r, c, n;
int dx[4]={-1, 1, 0, 0};
int dy[4]={0, 0, -1, 1};

int isValido(int x, int y) {
    return x>=0 && x<=r-1 && y>=0 && y<=c-1;
}

int prencher(int a, int b) {
    if (r==1 && c==1 && n==1) {
        return 0;
    }
    int i, j;
    for (i=0; i<r; i++) {
        for (j=0; j<c; j++) {
            mat[i][j]=0;
        }
    }
    int atual=0;
    int aux=n;
    while (n>0) {
        int x, y;
        int k;
        for (i=0; i<r; i++) {
            for (j=0; j<c; j++) {
                if (atual==0 && i==a && j==b) {

                }
                else {
                    if (mat[i][j]==0) {
                        int quant=0;
                        for (k=0; k<4; k++) {
                            x=i+dx[k];
                            y=j+dy[k];
                            if (isValido(x, y) && mat[x][y]==1) {
                                quant++;
                            }
                        }
                        if (quant==atual) {
                            n--;
                            mat[i][j]=1;
                        }
                    }
                    if (n==0) {
                        break;
                    }
                }
            }
            if (n==0) {
                break;
            }
        }
        atual++;
    }
    int x, y;
    int soma=0;
    for (x=0; x<r; x++) {
        for (y=0; y<c; y++) {
            if (mat[x][y]==1) {
                int novoX, novoY;
                int i;
                for (i=0; i<4; i++) {
                    novoX=x+dx[i];
                    novoY=y+dy[i];
                    if (isValido(novoX, novoY) && mat[novoX][novoY]==1) {
                        soma++;
                    }
                }
            }
        }
    }
    n=aux;
    return soma/2;
}

int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large_saida.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        scanf("%d %d %d", &r, &c, &n);
        //int =
        int res=min(prencher(0, 0), prencher(0, 1));
        printf("Case #%d: %d\n", teste, res);
    }
    return 0;
}
