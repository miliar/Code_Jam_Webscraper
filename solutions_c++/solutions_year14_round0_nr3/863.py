#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <iostream>
#define MAXR 53
#define MAXC 53

using namespace std;

char mat[MAXR][MAXC];
int r, c, m;
int qR, qC;
int pR, pC;
int lim;

int main() {
//    freopen("C-large.in", "r", stdin);
//    freopen("minesweeper_master_saida.txt", "w", stdout);
    int t, teste;
    scanf("%d", &t);
    for (teste=1; teste<=t; teste++) {
        scanf("%d %d %d", &r, &c, &m);
        int i, j;
        for (i=1; i<=r; i++) {
            for (j=1; j<=c; j++) {
                if (m==r*c-1) {
                    mat[i][j]='*';
                }
                else {
                    mat[i][j]='.';
                }
            }
        }
        if (m==r*c-1) {
            m=0;
        }
        else {
            qR=r;
            qC=c;
            pR=1;
            pC=1;
            while (m>0) {
                if (qR<=qC) {
                    if (qC>=3) {
                        if (m>=qR) {
                            for (i=0; i<qR; i++) {
                                mat[pR+i][pC]='*';
                            }
                            m-=qR;
                        }
                        else {
                            lim=min(m, qR-2);
                            for (i=0; i<lim; i++) {
                                mat[pR+i][pC]='*';
                            }
                            m-=lim;
                        }
                        qC--;
                        pC++;
                    }
                    else {
                        break;
                    }
                }
                else {
                    if (qR>=3) {
                        if (m>=qC) {
                            for (i=0; i<qC; i++) {
                                mat[pR][pC+i]='*';
                            }
                            m-=qC;
                        }
                        else {
                            lim=min(m, qC-2);
                            for (i=0; i<lim; i++) {
                                mat[pR][pC+i]='*';
                            }
                            m-=lim;
                        }
                        qR--;
                        pR++;
                    }
                    else {
                        break;
                    }
                }
            }
        }
        printf("Case #%d:\n", teste);
        if (m==0) {
            mat[r][c]='c';
            for (i=1; i<=r; i++) {
                for (j=1; j<=c; j++) {
                    printf("%c", mat[i][j]);
                }
                printf("\n");
            }
        }
        else {
            printf("Impossible\n");
        }
    }
    return 0;
}































