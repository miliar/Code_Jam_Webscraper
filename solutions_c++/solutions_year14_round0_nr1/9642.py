#include <iostream>
#include <cstdio>
#include <stack>
#include <queue>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>

#define PN(n) printf("%d\n", n)
#define DEBUG if(1)

#define LL long long int
#define ULL unsigned long long int

using namespace std;


int main(void) {
    int X[4][4];
    int Y[4][4];
    int a, b;

    int T;
    scanf("%d", &T);

    for(int TT = 1; TT <= T; TT++){

        scanf("%d", &a);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &X[i][j]);
            }
        }

        scanf("%d", &b);
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &Y[i][j]);
            }
        }

        a--; b--; //Zero index adjustment

        int ans = -1;
        int match = 0;
        for(int i = 0; i < 4; i++){
            int val = X[a][i];
            //printf("Val: %d\n", val);
            for(int j = 0; j < 4; j++){
                if(Y[b][j] == val){
                    ans = val;
                    match++;
                }
            }
        }
        //printf("%d %d\n", match, ans);
        if(match == 1){
            printf("Case #%d: %d\n", TT, ans);
        }
        else if(match > 1){
            printf("Case #%d: Bad magician!\n", TT);
        }
        else if(match == 0){
            printf("Case #%d: Volunteer cheated!\n", TT);
        }
    }
    return 0;
}

