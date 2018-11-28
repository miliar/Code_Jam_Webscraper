#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;


int main(){
    int T;
    char start[50];
    int origin;
    int num[10];
    int collect = 0;
    int k;
    char last[50];

    FILE *fptr2;
    fptr2 = fopen("output.txt", "w");
    if(fptr2){
        scanf("%d", &T);
        for(int i=1;i<=T;i++){
            scanf("%s", start);
            if(strcmp(start, "0") == 0){
                fprintf(fptr2, "Case #%d: INSOMNIA\n", i);
                continue;
            }
            origin = atoi(start);
            for(int j=0;j<10;j++){
                num[j] = 0;
            }
            collect = 0;
            k = 2;
            while(collect != 10){
                for(int j=0;j<strlen(start);j++){
                    int index = start[j]-'0';
                    if(num[index] == 0 ){
                        num[index] = 1;
                        collect++;
                    }
                    last[j] = start[j];
                }
                if(collect < 10){
                    int next = origin * k;
                    k++;
                    sprintf(start, "%d", next);
                }
            }
            fprintf(fptr2, "Case #%d: ", i);
            for(int j=0;j<strlen(start);j++)
                fprintf(fptr2, "%c", last[j]);
            fprintf(fptr2, "\n");
        }
        fclose(fptr2);
    }
    else{
        printf("failed\n");
    }
    return 0;
}
