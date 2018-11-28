/*
Problem A. Counting Sheep
*/
#include <cstdio>
#include <cstring>
#include <climits>

int main(void){
    int T;
    long long int N;
    
    FILE *fin, *fout;
    // fin = stdin;
    // fout = stdout;
    fin = fopen("A-small-attempt2.in", "r");
    fout = fopen("A-small-attempt2.out", "w");
    
    fscanf(fin, "%d", &T);
    for(int t=1; t<=T; t++){
        fscanf(fin, "%lld", &N);
        
        if( N==0 ){
            fprintf(fout, "Case #%d: INSOMNIA\n", t);
            continue;
        }
        
        int arr[10];
        memset(arr, 0, sizeof(arr));
        
        long long int tmp;
        int cnt;
        for(int i=1; (tmp=N*i)<LLONG_MAX; i++){
            while( tmp>0 ){
                arr[tmp%10] = 1;
                tmp /= 10;
            }
            cnt = 0;
            for(int j=0; j<10; j++)
                cnt += arr[j];
            
            if( cnt==10 ){
                fprintf(fout, "Case #%d: %lld\n", t, N*i);
                break;
            }
        }
        
        if( cnt!=10 )
            fprintf(fout, "Case #%d: INSOMNIA\n", t);
    }
    
    fclose(fin);
    fclose(fout);
    
    return 0;
}