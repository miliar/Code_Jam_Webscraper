#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#define MAXN 1001
#define ll long long

using namespace std;

int t, L1, L2, grid1[5][5], grid2[5][5];
int main(void){
    freopen("in.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &t);
    for(int test = 1; test <= t; test++){
        scanf("%d", &L1);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &grid1[i][j]);
            }
        }
        scanf("%d", &L2);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &grid2[i][j]);
            }
        }
        int find = 0, cheat = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(grid1[L1-1][i] == grid2[L2-1][j]){
                    if(find == 0){
                        find = grid1[L1-1][i];
                    }else if(find != 0){
                        cheat = 1;
                    }
                }
            }
        }
        printf("Case #%d: ", test);
        if(find > 0){
            if(!cheat){
                printf("%d\n", find);
            }else{
                printf("Bad magician!\n", find);
            }
        }else{
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
