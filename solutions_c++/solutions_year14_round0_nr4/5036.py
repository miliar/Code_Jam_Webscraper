#include <stdio.h>
#include <fstream>
#include <stdlib.h>


using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

    FILE* fio = fopen("input.txt", "r");
    FILE* fi = fopen("output.txt", "w");

int comp(const void *i, const void *j)
{
    if(*(double *)i > *(double *)j)
        return 1;
    return 0;
}

void NK_gen(int n, double N[], double K[], int NK[]){//N == 1, K == 2
    qsort(N, n, sizeof(double), comp);
    qsort(K, n, sizeof(double), comp);
    int j=0, k=0;
    while(k < n && j < n){
        if(j < n && N[j] < K[k]){
            NK[k+j] = 1;
            j++;
            //fprintf(fi, "N");
        }
        if(k < n && N[j] > K[k]){
            NK[k+j] = 2;
            k++;
            //fprintf(fi, "K");
        }
    }
    while(k < n){
        NK[k+j] = 2;
        k++;
        //fprintf(fi, "K");
    }
    while(j < n){
        NK[k+j] = 1;
        j++;
      //  fprintf(fi, "N");
    }
}

int true_game(int n, int NK[]){
    int np = 0, j;
    for(int i = 0; i < 2*n; i++){
        if(NK[i] == 0)
            NK[i] = 2;
    }
    for(int i = 0; i < 2*n; i++){
        if(NK[i] == 1){
            j = i+1;
            while(j < 2*n && NK[j]!=2)
                j++;
            if(j < 2*n)
                NK[j] = 0;
            else{
                j = 0;
                while(j < i && NK[j]!=2)
                    j++;
                NK[j] = 0;
                np++;
            }
        }
    }
    return np;

}

int cheat_game(int n, int NK[]){
    int np = 0, j;
    for(int i = 0; i < 2*n; i++){
        if(NK[i] == 0)
            NK[i] = 2;
    }
    for(int i = 0; i < 2*n; i++){
        if(NK[i] == 1){
            j = 0;
            while(j < i && NK[j]!=2){
                j++;
            }
            if(j < i){
                np++;
                NK[j] = 0;
            }
            else{
                j = 2*n-1;
                while(j > i && NK[j]!=2)
                    j--;
                NK[j] = 0;
            }
        }
    }
    return np;
}



int main(){
    int t;
    fscanf(fio, "%i", &t);
    int n[t];
    double N[t][10], K[t][10];
    int NK[t][20];
    for(int i = 0; i < t; i++){
        fscanf(fio, "%i", &n[i]);
        for(int j = 0; j < n[i]; j++)
            fscanf(fio, "%lf", &N[i][j]);
        for(int j = 0; j < n[i]; j++)
            fscanf(fio, "%lf", &K[i][j]);
    }
                //cout << "K";
    for(int i = 0; i < t; i++){
        NK_gen(n[i], N[i], K[i], NK[i]);//работает :)
        fprintf(fi, "Case #%i: %i %i\n", i+1, cheat_game(n[i], NK[i]), true_game(n[i], NK[i]));
    }
    return 0;
}

