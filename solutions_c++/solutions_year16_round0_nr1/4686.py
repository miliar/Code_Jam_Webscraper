#include <stdio.h>

int num[10];

void solve (long long tmp, int num[]) {
    
    while(tmp) {
        int digit = tmp%10;
        tmp /= 10;
        num[digit] = 1;
    }
}

int main(int argc, const char * argv[]) {
    
    FILE *fp;
    FILE *wfp;

    fp = fopen("/Users/Shared/Documents/XCode/2016ACM/SheepCount/A-large.txt", "r");
    wfp = fopen("/Users/Shared/Documents/XCode/2016ACM/SheepCount/output.txt", "w");
    
    long long tmp;
    
    int T = 1;
    
    if(fp) {
        fscanf(fp, "%lld\n", &tmp);
    }
    
    while(!feof(fp)) {
        
        fprintf(wfp, "Case #%d: ", T);
        fscanf(fp, "%lld\n", &tmp);
        
        for(int i=0; i<10; i++) num[i] = 0;
        
        if(tmp == 0)
            fprintf(wfp, "INSOMNIA\n");
        else {
            int multi = 1;
            while (1) {
                long long res = tmp*multi;
                
                solve(res, num);
                int check = 1;
                for(int i=0; i<10; i++) {
                    if(num[i] == 0) {
                        check = 0;
                        break;
                    }
                }
                if(check == 1) {
                    fprintf(wfp, "%lld\n", res);
                    break;
                }
                multi++;
            }
        }
        
        T++;
    }
    
    return 0;
}
