#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>

using namespace std;

#define TAM 512
#define INF 124

int n,m;
int tab[TAM][TAM];
bool lin[TAM];
bool col[TAM];

bool possivel(){
    int menor,maior;
    for(int i = 0 ; i < TAM ;i++) lin[i] = col[i] = true;
    menor = INF;

    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++)
            menor = min(menor,tab[i][j]);
    do{
        maior = 0;
        for(int i = 0 ; i < n ; i++)
            for(int j = 0 ; j < m ; j++)
                maior = max(maior,tab[i][j]);

        for(int i = 0 ; i < n ; i++)
            for(int j = 0 ; j < m ; j++)
                if(tab[i][j] == maior){
                    if(!lin[i] && !col[j]) return false;
                }

         for(int i = 0 ; i < n ; i++)
            for(int j = 0 ; j < m ; j++)
                if(tab[i][j] == maior){
                    lin[i] = col[j] = false;
                    tab[i][j] = 0;
                }
    //printf(" %d %d\n",maior,menor);
    }while(maior > menor);

    return true;
}

int main(){
	int nt;
	FILE *in = fopen("B.in","r");
	FILE *out = fopen("B.out","w");

	fscanf(in," %d",&nt);
	for(int t = 1 ; t <= nt ; t++){
		fscanf(in," %d %d",&n,&m);
        for(int i = 0 ; i < n ; i++)
            for(int j = 0 ; j < m ; j++)
                fscanf(in," %d",&tab[i][j]);

		fprintf(out,"Case #%d: ",t);
		if(possivel()) fprintf(out,"YES\n");
		else fprintf(out,"NO\n");

	}

	return 0;


}
