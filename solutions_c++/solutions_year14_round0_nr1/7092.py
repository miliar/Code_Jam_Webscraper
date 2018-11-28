#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
        int test;
        freopen ("input.txt", "r", stdin);
        freopen ("output.txt", "w", stdout);
        scanf( "%d\n", &test );
        int row, garbage;
        int arrangement_1[4], arrangement_2[4];
        for(int i = 1; i <= test; i++){
            scanf("%d\n", &row);
            for(int i = 1; i <= 4; i++){
                for(int j = 1; j <= 4; j++){
                    if(i == row){
                        scanf("%d", &arrangement_1[j]);
                    }
                    else{
                        scanf("%d", &garbage);
                    }
                }
            }
            scanf("%d\n", &row);
            for(int i = 1; i <= 4; i++){
                for(int j = 1; j <= 4; j++){
                    if(i == row){
                        scanf("%d", &arrangement_2[j]);
                    }
                    else{
                        scanf("%d", &garbage);
                    }
                }
            }
            int count = 0, ele = -1;
            for(int i = 1; i <= 4; i++){
                for(int j = 1; j <= 4; j++){
                    if(arrangement_1[i] == arrangement_2[j]){
                        count++;
                        ele = arrangement_1[i];
                    }
                }
            }
            switch(count){
                case 1:
                    printf("Case #%d: %d\n", i, ele);
                    break;
                case 0:
                    printf("Case #%d: Volunteer cheated!\n", i);
                    break;
                default:
                    printf("Case #%d: Bad magician!\n", i);
            }
        }
        return 0;
    }
