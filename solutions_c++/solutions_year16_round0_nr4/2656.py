#include<stdio.h>

FILE *fp, *fpo;

int main(){
    fp = fopen("d.in", "r");
    fpo = fopen("d.out", "w");
    
    int t;
    fscanf(fp, "%d", &t);
    for(int T = 1; T <= t; T++){
        int K, C, S;
        fscanf(fp, "%d%d%d", &K, &C, &S);
        
        fprintf(fpo, "Case #%d: ", T);
        for(int i = 1; i <= K; i++)
            fprintf(fpo, "%d ", i);
        fprintf(fpo, "\n");
    }
    
    return 0;
}