#include<stdio.h>
int main(void){
    FILE *fin=fopen("codejam-1.in", "r");
    FILE *fout=fopen("codejam-1.out", "w");
    char Pole[1004];
    int T;
    fscanf(fin,"%i", &T);
    int S;
    int i; int j;
    int res; int zrovna;
    for(i=0;i<T;i++){
        fscanf(fin,"%i", &S);
        fscanf(fin,"%c", &Pole[0]);
        for(j=0;j<=S;j++){
            fscanf(fin,"%c", &Pole[j]);
            Pole[j]-='0';
        }
        zrovna=0; res=0;
        for(j=0;j<S;j++){
            zrovna+=Pole[j];
            if(zrovna<=j) {res++; zrovna++;}
        }
        fprintf(fout,"Case #%i: %i\n", i+1, res);
    }
    return 0;
}
