#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int T, K, C, S;

main(){
    FILE *inp = fopen("fractilesS.in", "r"), *outp = fopen("fractiles.out", "w");
    fscanf(inp, "%d", &T);
    int i,j;
    long long int loc;
    for(i = 0; i < T; i++){
        loc = 1;
        fscanf(inp, "%d %d %d", &K, &C, &S);
        fprintf(outp, "Case #%d: ", i+1);
        for(j = 0; j < C-1; j++){
            loc = loc * K;
        }
        for(j = 0; j < K; j++){
            fprintf(outp, "%lld ", loc * j + 1);
        }
        fprintf(outp, "\n");
    }
    return 0;
}
