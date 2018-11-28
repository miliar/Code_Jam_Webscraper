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
#define MAXL 10010
#define MAXN 10010

int mat[4][4]={{0, 1, 2, 3},
               {1, 0, 3, 2},
               {2, 3, 0, 1},
               {3, 2, 1, 0}};

int sinal[4][4]={{0, 0, 0, 0},
                 {0, 1, 0, 1},
                 {0, 1, 1, 0},
                 {0, 0, 1, 1}};

char str[MAXL];
int vet[MAXN];
int pd[MAXN][4][3][2];
int n;

int busca(int indice, int subAtual, int valAtual, int sinAtual) {
    int &res=pd[indice][subAtual][valAtual][sinAtual];
    if (res!=-1) {
        return res;
    }
    if (indice==n) {
        if (subAtual<=2) {
            return res=0;
        }
        else {
            if (valAtual!=3) {
                return res=0;
            }
            else {
                if (sinAtual==1) {
                    return res=0;
                }
                else {
                    return res=1;
                }
            }
        }
    }
    res=0;
    if (valAtual==subAtual && sinAtual==0 && subAtual<=2) {
        res=max(res, busca(indice, subAtual+1, 0, 0));
    }
    int novoVal, novoSinal;
    novoVal=mat[valAtual][vet[indice]];
    novoSinal=(sinAtual+sinal[valAtual][vet[indice]])%2;
    res=max(res, busca(indice+1, subAtual, novoVal, novoSinal));
    return res;
}

int main() {
//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C-small-attempt0_saida.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        int L, X;
        scanf("%d %d", &L, &X);
        scanf("%s", str);
        int i, j;
        n=0;
        for (i=0; i<X; i++) {
            for (j=0; j<L; j++) {
                if (str[j]=='i') {
                    vet[n++]=1;
                }
                else if (str[j]=='j') {
                    vet[n++]=2;
                }
                else if (str[j]=='k') {
                    vet[n++]=3;
                }
            }
        }
        memset(pd, -1, sizeof(pd));
        if (busca(0, 1, 0, 0)==1) {
            printf("Case #%d: YES\n", teste);
        }
        else {
            printf("Case #%d: NO\n", teste);
        }
    }
    return 0;
}
