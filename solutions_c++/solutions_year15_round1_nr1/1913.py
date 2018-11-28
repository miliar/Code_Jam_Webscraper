
#include <stdio.h>

#include <stdlib.h>
#include <string.h>

#include <vector>

using namespace std;


int main(int argc, const char * argv[]) {
    
//        char inputname[1000] = "/Users/lbjcom/Downloads/A-small-attempt0.in.txt";
    char inputname[1000] = "/Users/lbjcom/Downloads/A-large.in.txt";
//        char inputname[1000] = "/Users/lbjcom/Downloads/in.txt";
    
    char outputname[1000] = "/Users/lbjcom/Downloads/_OUT.txt";
    
    FILE *fp = fopen(inputname, "r");
    
    FILE *fpout = fopen(outputname, "w");
    
    int number_of_tests = 0;
    
    int ns = 0;
    
    
    // 먼저 테스트 갯수를 읽는다.
    fscanf(fp, "%d", &number_of_tests);
    
    for(int i = 0; i < number_of_tests; i++) {
        int nn[20000];
        
        int n1 = 0;
        
        int n2 = 0;
        
        fscanf(fp, "%d", &ns);
        
        for(int j = 0; j < ns; j++) {
            fscanf(fp, "%d", &nn[j]);
        }
        
        
        // case1
        for(int j = 0; j < ns-1; j++) {
            if(nn[j] > nn[j+1]) {
                n1 += (nn[j] - nn[j+1]);
            }
        }
        
        // case2
        
        int rate = 0;
        
        for(int j = 0; j < ns-1; j++) {
            if(rate < (nn[j] - nn[j+1])) {
                rate = (nn[j] - nn[j+1]);
            }
        }
        
        for(int j = 0; j < ns-1; j++) {
            if(nn[j] < rate) {
                n2 += nn[j];
            } else {
                n2 += rate;
            }
        }
        
        
        fprintf(fpout, "Case #%d: %d %d \n", i+1, n1, n2);
        
        
    } //for(int i = 0; i < number_of_tests; i++) {
    
    fclose(fpout);
    fclose(fp);
    
}






