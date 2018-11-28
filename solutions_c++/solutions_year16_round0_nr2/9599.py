#include <stdio.h>


int main() {
    int i, j, k, l, t;
    FILE *in = fopen("data.in", "r");
    FILE *out = fopen("data.out", "w");
    int T;
    char pan[105];
    
    fscanf(in, "%d\n", &T);
    for(t=1;t<=T;t++) {
        fprintf(out, "Case #%d: ", t);
        
        l = 0;
        while(1) {
            fscanf(in, "%c", &pan[l]);
            if(pan[l] == '\n') break;
            l ++;
        }
        pan[l] = 0;
        
        if(pan[0] == '-') k = 1;
        else k = 0;
        
        for(i=1;i<l;i++) {
            if(pan[i] == pan[i-1]) continue;
            
            if(pan[i] == '-') k += 2;
        }
        
        fprintf(out, "%d\n", k);
    }
    
    return 0;
}