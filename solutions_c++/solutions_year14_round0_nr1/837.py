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

using namespace std;

int mat[6][6];
int vis[20];

int main() {
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("magic_trick_saida.txt", "w", stdout);
    int t, cont;
    scanf("%d", &t);
    for (cont=1; cont<=t; cont++) {
        int linha;
        int i, j;
        memset(vis, 0, sizeof(vis));
        scanf("%d", &linha);
        for (i=1; i<=4; i++) {
            for (j=1; j<=4; j++) {
                scanf("%d", &mat[i][j]);
            }
        }
        for (j=1; j<=4; j++) {
            vis[mat[linha][j]]++;
        }
        scanf("%d", &linha);
        for (i=1; i<=4; i++) {
            for (j=1; j<=4; j++) {
                scanf("%d", &mat[i][j]);
            }
        }
        for (j=1; j<=4; j++) {
            vis[mat[linha][j]]++;
        }
        int quant=0, indice;
        for (i=1; i<=16; i++) {
            if (vis[i]==2) {
                quant++;
                indice=i;
            }
        }
        printf("Case #%d: ", cont);
        if (quant==1) {
            printf("%d\n", indice);
        }
        else if (quant>1) {
            printf("Bad magician!\n");
        }
        else if (quant==0) {
            printf("Volunteer cheated!\n");
        }

    }
    return 0;
}































