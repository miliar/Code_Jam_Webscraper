//
// Created by 金宇超 on 16/4/16.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char buf[1500] = {0};
    char temp[3000] = {0};
    int T=0;
    FILE* f=fopen("R1-A-large.in", "r");
    FILE* o=fopen("R1-A-large.out", "w");
    fscanf(f, "%d\n", &T);
    for(int i=0; i<T; i++) {
        memset(buf, 0, sizeof(char)*1500);
        memset(temp, 0, sizeof(char)*3000);
        fscanf(f, "%s\n", buf);
        char maxC='\0';
        int len=(int)strlen(buf);
        int before=1500;
        int after=1501;
        for(int j=0; j<len; j++) {
            if(buf[j]>=maxC) {
                maxC=buf[j];
                temp[before]=buf[j];
                before--;
            } else {
                temp[after]=buf[j];
                after++;
            }
        }
        printf("CASE #%d: ", i+1);
        fprintf(o,"CASE #%d: ", i+1);
        for(int j=0; j<len; j++) {
            printf("%c", temp[before+1+j]);
            fprintf(o, "%c", temp[before+1+j]);
        }
        printf("\n");
        fprintf(o,"\n");
    }
    return 0;
}