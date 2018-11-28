#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

int t,T=0;
bool ck[10];
char buf[20];

int main(){
    
    FILE * ifp = fopen("/Users/KHJ/Desktop/codejam/A/A-large.in", "r");
    FILE * ofp = fopen("/Users/KHJ/Desktop/codejam/A/A-large.out", "w");
    
    fscanf(ifp,"%d",&t);
    int n;
    long long int next=0;
    bool flag = true;
    
    while (t--) {
        
        fscanf(ifp,"%d",&n);
        fprintf(ofp,"Case #%d: ", ++T);
        
        if (n==0) {
            fprintf(ofp,"INSOMNIA\n");
            continue;
        }
        
        next = n;
        while (1) {
            
            sprintf(buf,"%lld",next);
            flag = true;
            
            unsigned int len = (unsigned)strlen(buf);
            
            for (int i=0; i < len; i++) {
                if (!ck[buf[i]-'0']) {
                    ck[buf[i]-'0'] = true;
                }
            }
            for (int i=0; i<10; i++) {
                if (!ck[i]) {
                    flag = false;
                }
            }
            
            if (flag) {
                fprintf(ofp,"%lld\n",next);
                break;
            }
            //printf("%lld\n",next);
            next += n;
        }
        
        for (int i=0; i<10; i++) {
            ck[i] =false;
        }
        
    }
    return 0;
}