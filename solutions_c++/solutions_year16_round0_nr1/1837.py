#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int T;
int N[105];
int digits[15];
int len;
int tens[10];

void make_ten(){
    tens[0] = 1;
    int i;
    for(i = 1; i < 10; i++){
        tens[i] = tens[i-1] * 10;
    }
    return;
}

int make_len(int x){
    int j;
    for(j = 1; j < 10; j++){
        if(tens[j] > x) return j;
    }
}

int solve(int n){
    int j,k;
    int done = 10;
    for(j = 1; j < 1000; j++){
        if(j * n >= tens[len]) len++;
        for(k = 0; k < len; k++){
            if(!digits[(j*n%tens[k+1])/tens[k]]){
                digits[(j*n%tens[k+1])/tens[k]] = 1;
                done--;
            }
        }
        if(done == 0) return j;
    }
}

main(){
    FILE *inp = fopen("countingsheepL.in", "r"), *outp = fopen("countingsheep.out", "w");
    fscanf(inp, "%d", &T);
    int i,j;
    for(i = 0; i < T; i++){
        fscanf(inp, "%d", N+i);
    }
    make_ten();
    for(i = 0; i < T; i++){
        if(N[i] == 0){
            fprintf(outp, "Case #%d: INSOMNIA\n", i+1);
            continue;
        }
        for(j = 0; j < 10; j++){
            digits[j] = 0;
        }
        len = make_len(N[i]);
        fprintf(outp, "Case #%d: %d\n", i+1, solve(N[i]) * N[i]);
    }
    return 0;
}
