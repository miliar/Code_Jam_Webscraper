#include <bits/stdc++.h>
using namespace std;
int main(void){
    FILE *f_i = fopen("C-small-attempt1.in", "r"), *f_o = fopen("C_output.txt", "w");
    int t, N, J, i, j, k, f, w[32];
    long long int A, B, P, temp, C, D[9], M;
    fscanf(f_i, "%d", &t);
    //printf("%d\n", t);
    for(j = 1; j <= t; j++){
        fprintf(f_o, "Case #%d:\n", j);
        fscanf(f_i, "%d %d", &N, &J);
        //printf("%d %d\n", N, J);
        for(A = B = (1ull << (N - 1)) + 1; B < (1ull << N) && J; B++){
            if(B & 1 && (B >> (N - 1) & 1)){
                /*P = B;
                while(P){
                    printf("%d", P & 1);
                    P >>= 1;
                }printf("\n");*/
                for(i = 0; i < 9; i++) D[i] = 0;
                for(i = 2, f = 9; i <= 10; i++){
                    P = B; C = 1; M = 0;
                    while(P && M < 1000){
                        if(P & 1) M += C;
                        P >>= 1; C *= i;
                    }//printf("M = %lld\n", M);
                    for(P = B, temp = 0, C = 1, k = 2; k < 1000 && k < M; k++, temp = 0, C = 1, P = B){
                        while(P){
                            if(P & 1) temp = (temp + C) % k;
                            P >>= 1; C *= i;
                        }
                        //printf("k = %d, temp = %lld\n", k, temp);
                        if(temp % k == 0) {
                            D[i - 2] = k;
                            break;
                        }
                    }
                    //printf("C = %lld, temp = %lld, D[%d] = %lld\n", C, temp, i - 2, D[i - 2]);
                    if(D[i - 2]) f--;
                    else break;
                }
                if(!f){
                    for(i = 0, P = B; i < N; i++){
                        w[i] = (P & 1);
                        P >>= 1;
                    }
                    for(i = N - 1; i >= 0; i--) fprintf(f_o, "%d", w[i]);
                    for(i = 0; i < 9; i++) fprintf(f_o, " %lld", D[i]);
                    if(J || (j != t))fprintf(f_o, "\n");
                    J--;
                }
            }
        }
    }
    fclose(f_i); fclose(f_o);
}
