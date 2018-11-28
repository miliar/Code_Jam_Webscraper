#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    FILE *fp;
    FILE *wfp;
    
    fp = fopen("/Users/Shared/Documents/XCode/2016ACM/Pancake/B-large.txt", "r");
    wfp = fopen("/Users/Shared/Documents/XCode/2016ACM/Pancake/output.txt", "w");
    
    char tmp[110];
    
    int T = 1;
    
    int num;
    
    fscanf(fp, "%d\n", &num);
    
    while(!feof(fp)) {
        
        fprintf(wfp, "Case #%d: ", T);
        
        fscanf(fp, "%s\n", &tmp);
        
        int count = 0;
        
        for(int i=0; i<110; i++) {
            if(tmp[i] == '\0')
                break;
            else count ++;
        }
        
        if(count == 1) {
            if(tmp[0] == '-') {
                fprintf(wfp, "1\n");
            }
            else {
                fprintf(wfp, "0\n");
            }
        } else {
            int rescount = 0;
            while(1) {
                int check = -1;
                for(int i=0; i<count-1; i++) {
                    if(tmp[i] != tmp[i+1]) {
                        check = i;
                        break;
                    }
                }
                if(check == -1) {
                    if(tmp[0] == '-') {
                        rescount++;
                        fprintf(wfp, "%d\n", rescount);
                    }
                    else if(tmp[0] == '+') {
                        fprintf(wfp, "%d\n", rescount);
                    }
                    break;
                } else {
                    if(tmp[0] == '-') {
                        for(int i=0; i<= check; i++) {
                            tmp[i] = '+';
                        }
                        rescount ++;
                    } else if(tmp[0] == '+') {
                        for(int i=0; i<= check; i++) {
                            tmp[i] = '-';
                        }
                        rescount ++;
                    }

                }
            }
        }
        
        T++;
    }
    return 0;
}
