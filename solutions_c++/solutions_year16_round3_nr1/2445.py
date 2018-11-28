#include <stdio.h>

int main(int argc, const char * argv[]) {
    FILE *fp;
    FILE *wfp;
    
    fp = fopen("/Users/Shared/Documents/XCode/2016ACM/SenateEvacuation/A-large.txt", "r");
    wfp = fopen("/Users/Shared/Documents/XCode/2016ACM/SenateEvacuation/output1.txt", "w");
    
    long long tmp;
    
    int T = 1;
    
    if(fp) {
        fscanf(fp, "%lld\n", &tmp);
    }
    
    int num[1100];
    
    for(int i=0; i<1100; i++)
        num[i] = 0;
    
    while(!feof(fp)) {
        
        fprintf(wfp, "Case #%d: ", T);
        
        int P;
        
        fscanf(fp, "%d\n", &P);
        
        for(int i=1 ; i<=P ; i++) {
            if(i != P) {
                fscanf(fp, "%d ", &num[i]);
                printf("%d ", num[i]);
            }
            else {
                fscanf(fp, "%d\n", &num[i]);
                printf("%d\n", num[i]);
            }
        }
        
        int min = 10000;
        int lar = 0;
        int index = 0;
        
        for(int i=1; i<=P; i++) {
            if(num[i] <= min)
                min = num[i];
            if(num[i] >= lar) {
                lar = num[i];
                index = i;
            }
        }
        while (lar > min) {
            for(int i=1; i<=P; i++) {
                if(num[i] == lar) {
                    char tmp = i+64;
                    fprintf(wfp, "%c ", tmp);
                    printf("%c ", tmp);
                    num[i] --;
                }
            }
            lar = 0;
            for(int i=1; i<=P; i++) {
                if(num[i] >= lar) {
                    lar = num[i];
                    index = i;
                }
            }
            
        }
        
        if(P%2 == 0) {
            while (num[P] != 0) {
                for(int i=1; i<=P-1; i+=2) {
                    char tmp = i+64;
                    char tmp2 = i+65;
                    fprintf(wfp, "%c%c ", tmp, tmp2);
                    printf("%c%c ", tmp, tmp2);
                    num[i] --;
                    num[i+1] --;
                }
            }
        } else if(P%2 == 1) {
            while (num[P] != 0) {
                
                char fir = 'A';
                fprintf(wfp, "%c ", fir);
                printf("%c ", fir);
                num[1] --;
                
                for(int i=2; i<=P-1; i+=2) {
                    char tmp = i+64;
                    char tmp2 = i+65;
                    fprintf(wfp, "%c%c ", tmp, tmp2);
                    printf("%c%c ", tmp, tmp2);
                    num[i] --;
                    num[i+1] --;
                }
            }
        }
        
        fprintf(wfp, "\n");
        printf("\n");
        
        T++;
    }
    
    return 0;
}
