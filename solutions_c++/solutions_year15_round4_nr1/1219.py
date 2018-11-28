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
#define MAXR 110
#define MAXC 110

char mat[MAXR][MAXC];
int visCima[MAXR][MAXC];
int visBaixo[MAXR][MAXC];
int visEsq[MAXR][MAXC];
int visDir[MAXR][MAXC];
int r, c;

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large_saida.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        scanf("%d %d", &r, &c);
        int i, j, k;
        for (i=1; i<=r; i++) {
            scanf("%s", mat[i]+1);
        }
        memset(visCima, 0, sizeof(visCima));
        memset(visBaixo, 0, sizeof(visBaixo));
        memset(visEsq, 0, sizeof(visEsq));
        memset(visDir, 0, sizeof(visDir));
        for (i=1; i<=r; i++) {
            for (j=1; j<=c; j++) {
                if (mat[i][j]!='.') {
                    for (k=i+1; k<=r; k++) {
                        visCima[k][j]=1;
                    }
                    for (k=i-1; k>=1; k--) {
                        visBaixo[k][j]=1;
                    }
                    for(k=j-1; k>=1; k--) {
                        visDir[i][k]=1;
                    }
                    for (k=j+1; k<=c; k++) {
                        visEsq[i][k]=1;
                    }
                }
            }
        }
        int quant=0;
        for (i=1; i<=r; i++) {
            for (j=1; j<=c; j++) {
                if (mat[i][j]!='.') {
                    int achou=0;
                    if (mat[i][j]=='^') {
                        if (visCima[i][j]>0) {
                            achou=1;
                        }
                    }
                    else if (mat[i][j]=='v') {
                        if (visBaixo[i][j]>0) {
                            achou=1;
                        }
                    }
                    else if (mat[i][j]=='>') {
                        if (visDir[i][j]>0) {
                            achou=1;
                        }
                    }
                    else if (mat[i][j]=='<') {
                        if (visEsq[i][j]>0) {
                            achou=1;
                        }
                    }
                    if (achou==0 && visEsq[i][j]+visDir[i][j]+visBaixo[i][j]+visCima[i][j]>0) {
                        quant++;
                    }
                    if (achou==0 && visEsq[i][j]+visDir[i][j]+visBaixo[i][j]+visCima[i][j]==0) {
                        quant=-1;
                        break;
                    }
                }
            }
            if (quant==-1) {
                break;
            }
        }

        if (quant==-1) {
            printf("Case #%d: Impossible\n", teste);
        }
        else {
            printf("Case #%d: %d\n", teste, quant);
        }
    }
    return 0;
}
