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
#define INF 999999999
#define MAXN 1010
#define MAXM 1000000

using namespace std;

int vis[MAXM];
vector<int> naomi;
vector<int> ken;
vector<int> naomiNormal;
vector<int> kenNormal;
char aux[20];
int tam;

void jogadaKen(int escolhaNaomi, int &contador) {
    int i;
    int indiceKen=0;
    for (i=0; i<ken.size(); i++) {
        if (ken[i]>escolhaNaomi) {
            indiceKen=i;
            break;
        }
    }
    if (ken[indiceKen]<escolhaNaomi) {
        contador++;
    }
    vis[escolhaNaomi]=1;
    ken.erase(ken.begin()+indiceKen);
}

void jogadaKenNormal(int escolhaNaomi, int &contador) {
    int i;
    int indiceKen=0;
    for (i=0; i<kenNormal.size(); i++) {
        if (kenNormal[i]>escolhaNaomi) {
            indiceKen=i;
            break;
        }
    }
    if (kenNormal[indiceKen]<escolhaNaomi) {
        contador++;
    }
//    printf("*** %d %d\n", escolhaNaomi, )
    kenNormal.erase(kenNormal.begin()+indiceKen);
}

int main() {
//    freopen("D-large.in", "r", stdin);
//    freopen("deceitfull_war_saida.txt", "w", stdout);
    int t, teste;
    scanf("%d", &t);
    for (teste=1; teste<=t; teste++) {
        int n;
        scanf("%d", &n);
        int i, j;
//        naomi.clear();
//        ken.clear();
        memset(vis, 0, sizeof(vis));
        for (i=0; i<n; i++) {
            getchar();
            scanf("0.%s", aux);
            tam=strlen(aux);
            for (j=tam; j<5; j++) {
                aux[j]='0';
            }
            aux[j]='\0';
            naomi.push_back(atoi(aux));
            naomiNormal.push_back(naomi[i]);
            vis[naomi[i]]=1;
        }
        for (i=0; i<n; i++) {
            getchar();
            scanf("0.%s", aux);
            tam=strlen(aux);
            for (j=tam; j<5; j++) {
                aux[j]='0';
            }
            aux[j]='\0';
            ken.push_back(atoi(aux));
            kenNormal.push_back(ken[i]);
            vis[ken[i]]=1;
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        sort(naomiNormal.begin(), naomiNormal.end());
        sort(kenNormal.begin(), kenNormal.end());
        int rodadas = n;
        int contModificado=0;
        while (rodadas>0) {
            int escolhaNaomi;
            if (naomi[0]<ken[0]) {
                escolhaNaomi=ken[ken.size()-1]-1;
                while (escolhaNaomi>naomi[0] && vis[escolhaNaomi]!=0) {
                    escolhaNaomi--;
                }
                jogadaKen(escolhaNaomi, contModificado);
                naomi.erase(naomi.begin());
            }
            else {
                escolhaNaomi=ken[ken.size()-1]+1;
                while (escolhaNaomi<MAXM && vis[escolhaNaomi]!=0) {
                    escolhaNaomi++;
                }
                if (escolhaNaomi==MAXM) {
                    escolhaNaomi=naomi[0];
                }
                jogadaKen(escolhaNaomi, contModificado);
                naomi.erase(naomi.begin());
            }
            rodadas--;
        }
        int contNormal=0;
        rodadas=n;
        while (rodadas>0) {
            jogadaKenNormal(naomiNormal[0], contNormal);
            naomiNormal.erase(naomiNormal.begin());
            rodadas--;
        }
        printf("Case #%d: %d %d\n", teste, contModificado, contNormal);

    }
    return 0;
}































