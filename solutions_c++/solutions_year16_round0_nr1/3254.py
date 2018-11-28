#include<stdio.h>

int main(){
    FILE *fp, *fpo;
    fp = fopen("a.in", "r");
    fpo = fopen("a.out", "w");
    
    int t, n;
    fscanf(fp, "%d", &t);
    for(int i = 1; i <= t; i++){
        fscanf(fp, "%d", &n);
        
        if(!n){
            fprintf(fpo, "Case #%d: INSOMNIA\n", i);
            continue;
        }
        
        bool c[10] = { false, };
        int cnt = 0;
        
        int j;
        for(j = 1; cnt != 10; j++){
            long long now = 1L * n * j;
            
            while(now != 0){
                if(!c[now % 10]){
                    c[now % 10] = true;
                    cnt++;
                }
                now /= 10;
            }
        }
        
        fprintf(fpo, "Case #%d: %lld\n", i, 1LL * (j - 1) * n);
    }
}