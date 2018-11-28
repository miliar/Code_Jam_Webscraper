#include <stdio.h>
#include <string.h>


int main() {
    long i, j, k, l;
    FILE *in = fopen("data.in", "r");
    FILE *out = fopen("data.out", "w");
    long T, N, numbers[10];
    
    fscanf(in, "%ld", &T);
    for(l=0;l<T;l++) {
        fscanf(in, "%ld", &N);
        fprintf(out, "Case #%ld: ", l+1);
        
        if(N == 0) {
            fprintf(out, "INSOMNIA\n");
            continue;
        }
        
        for(i=0;i<10;i++) numbers[i] = 0;
        k = 0;
        i = 1;
        while(1) {
            j = N*i;
            while(j) {
                if(numbers[j%10] == 0) k += j%10;
                numbers[j%10] = 1;
                j /= 10;
            }
            
            if(k == 45 && numbers[0] == 1) break;
            i ++;
        }
        
        fprintf(out, "%ld\n", i*N);
    }
}