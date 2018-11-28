#include <stdio.h>
#define MIN(t1, t2) (((t1)<(t2))?(t1):(t2))

FILE *fin, *fout;
bool process(void)
{
    int A[105][105]={0};
    int N, M, i, j;
    int R[105]={0}, C[105]={0};
    fscanf(fin, "%d %d", &N, &M);
    for (i=0;i<N;++i){
        for(j=0;j<M;++j){
            fscanf(fin, "%d", &A[i][j]);
            if (R[i] < A[i][j]) R[i] = A[i][j];
            if (C[j] < A[i][j]) C[j] = A[i][j];
        }
    }
    for (i=0;i<N;++i){
        for (j=0;j<M;++j){
            if (A[i][j] != MIN(R[i], C[j])) return false;
        }
    }
    return true;
}
int main(void)
{
    fin = fopen("input.txt", "r");
    fout = fopen("output.txt", "w");

    int T, t;
    fscanf(fin, "%d", &T);
    for (t=1;t<=T;++t){
        if (process()) fprintf(fout, "Case #%d: YES\n", t);
        else fprintf(fout, "Case #%d: NO\n", t);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
