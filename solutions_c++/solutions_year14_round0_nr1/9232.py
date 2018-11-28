#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

char m[100][100];

int main(void){

    int T;
    scanf("%d",&T);

    for(int r = 0;r < T;++r){
        int data[5][10];
        int p = 0;
        for(int z = 0;z < 2;++z){
            scanf("%d",&p);
            for(int i = 0;i < 4;++i){
                if(i == p - 1){
                    scanf("%d %d %d %d",data[z]+0,data[z]+1,data[z]+2,data[z]+3);
                }else{
                    int d;
                    scanf("%d",&d);
                    scanf("%d",&d);
                    scanf("%d",&d);
                    scanf("%d",&d);
                }
            }
        }

        int m = 0;
        int lm = 0;
        for(int i = 0;i < 4;++i){
            for(int z = 0;z < 4;++z){
                if(data[0][i] == data[1][z]){
                    ++m;
                    lm = data[0][i];
                }
            }
        }

        int ans = 0;
        printf("Case #%d: ",r+1);
        if(m == 0){
            printf("Volunteer cheated!");
        }else if(m == 1){
            printf("%d",lm);
        }else{
            printf("Bad magician!");
        }
        printf("\n");
    }

}
