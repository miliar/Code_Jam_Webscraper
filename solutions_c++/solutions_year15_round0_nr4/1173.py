#include<stdio.h>
int main(void){
    FILE *fin=fopen("codejam-4.in", "r");
    FILE *fout=fopen("codejam-4.out", "w");
    int T;
    fscanf(fin,"%i", &T);
    int i;
    int c;
    int X; int R; int C;
    for(i=0;i<T;i++){
        fscanf(fin,"%i %i %i", &X, &R, &C);
        if(R>C){
            c=R;
            R=C;
            C=c;
        }
        if(X==1) fprintf(fout,"CASE #%i: GABRIEL\n", i+1);
        if(X==2){
            if((R*C)%2==1) fprintf(fout,"CASE #%i: RICHARD\n", i+1);
            else fprintf(fout,"CASE #%i: GABRIEL\n", i+1);
        }
        if(X==3){
            if(R==1) fprintf(fout,"CASE #%i: RICHARD\n", i+1);
            else if(R==2&&C==3) fprintf(fout,"CASE #%i: GABRIEL\n", i+1);
            else if(R==2) fprintf(fout,"CASE #%i: RICHARD\n", i+1);
            else if(R==3) fprintf(fout,"CASE #%i: GABRIEL\n", i+1);
            else fprintf(fout,"CASE #%i: RICHARD\n", i+1);
        }
        if(X==4){
            if(R==1||R==2) fprintf(fout,"CASE #%i: RICHARD\n", i+1);
            else if(R==3&&C==3) fprintf(fout,"CASE #%i: RICHARD\n", i+1);
            else if(R==3) fprintf(fout, "CASE #%i: GABRIEL\n", i+1);
            else fprintf(fout, "CASE #%i: GABRIEL\n", i+1);
        }
    }
    return 0;
}
