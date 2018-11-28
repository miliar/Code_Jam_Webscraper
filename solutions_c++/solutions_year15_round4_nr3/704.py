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
#define MAXN 21

char mat[MAXN][100000];
vector<string> vet[MAXN];
int n;

struct NoTrie {

    NoTrie *prox[27];
    int eng;
    int fran;
    int ambos;
    int tot;

    NoTrie(int _eng=0, int _fran=0, int _ambos=0, int _tot=0) {
        eng=_eng;
        fran=_fran;
        ambos=_ambos;
        tot=_tot;
        int i;
        for (i=0; i<27; i++) {
            prox[i]=NULL;
        }
    }

    ~NoTrie() {
        int i;
        for (i=0; i<27; i++) {
            delete(prox[i]);
        }
    }

    void inserir(string &s, int indice, char idioma) {
        if (indice==s.size()) {
            if (idioma=='E') {
                eng++;
            }
            if (idioma=='F') {
                fran++;
            }
            tot-=ambos;
            if (eng>0 && fran>0) {
                ambos=1;
            }
            tot+=ambos;
        }
        else {
            int pos=s[indice]-'a';
            if (prox[pos]==NULL) {
                prox[pos]=new NoTrie();
            }
            tot-=prox[pos]->tot;
            prox[pos]->inserir(s, indice+1, idioma);
            tot+=prox[pos]->tot;
        }
    }

    void remover(string &s, int indice, char idioma) {
        if (indice==s.size()) {
            if (idioma=='E') {
                eng--;
            }
            if (idioma=='F') {
                fran--;
            }
            tot-=ambos;
            if (eng>0 && fran>0) {
                ambos=1;
            }
            else {
                ambos=0;
            }
            tot+=ambos;
        }
        else {
            int pos=s[indice]-'a';
            if (prox[pos]!=NULL) {
                tot-=prox[pos]->tot;
                prox[pos]->remover(s, indice+1, idioma);
                tot+=prox[pos]->tot;
            }
        }
    }
};

NoTrie *raiz;
int menor=INF;

void backtrack(int a[MAXN], int k) {
    if (k==n) {
        int i, j;
        for (i=2; i<n; i++) {
            for (j=0; j<vet[i].size(); j++) {
                if (a[i]==0) {
                    raiz->inserir(vet[i][j], 0, 'E');
                }
                else {
                    raiz->inserir(vet[i][j], 0, 'F');
                }
            }
        }
//        printf("***\n");
//        for (i=2; i<n; i++) {
//            printf("%d", a[i]);
//        }
//        printf("\n%d\n", raiz->tot);
        menor=min(menor, raiz->tot);
        for (i=2; i<n; i++) {
            for (j=0; j<vet[i].size(); j++) {
                if (a[i]==0) {
                    raiz->remover(vet[i][j], 0, 'E');
                }
                else {
                    raiz->remover(vet[i][j], 0, 'F');
                }
            }
        }
    }
    else {
        a[k]=0;
        backtrack(a, k+1);
        a[k]=1;
        backtrack(a, k+1);
//        if (k==2) {
//            a[k]=0;
//            backtrack(a, k+1);
//        }
//        if (k==3) {
//            a[k]=1;
//            backtrack(a, k+1);
//        }
    }
}


int main() {
//    freopen("C-small-attempt4.in", "r", stdin);
//    freopen("C-small-attempt4_saida.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        scanf("%d", &n);
        getchar();
        int i, j;
        for (i=0; i<n; i++) {
            gets(mat[i]);
            vet[i].clear();
            char *aux=strtok(mat[i], " ");
            while (aux!=NULL) {
                vet[i].push_back(aux);
                aux=strtok(NULL, " ");
            }
        }
//        for (i=0; i<n; i++) {
//            for (j=0; j<vet[i].size(); j++) {
//                printf("%s ", vet[i][j].c_str());
//            }
//            printf("\n");
//        }
        raiz=new NoTrie();
        menor=INF;
        for (i=0; i<2; i++) {
            for (j=0; j<vet[i].size(); j++) {
                if (i==0) {
                    raiz->inserir(vet[i][j], 0, 'E');
                }
                else {
                    raiz->inserir(vet[i][j], 0, 'F');
                }
            }
        }
        int a[MAXN];
        backtrack(a, 2);
        printf("Case #%d: %d\n", teste, menor);
        //delete(raiz);
    }
    return 0;
}
