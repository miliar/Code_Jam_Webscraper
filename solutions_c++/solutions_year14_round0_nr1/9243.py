#include <cstdio>
#include <cstdlib>

int main(){
    int cn;
    int row1[4];
    int row2[4];
    int ans[4];
    int ansNum;
    int r1, r2;
    int tmp;
    scanf("%d", &cn);
    for(int i = 0; i < cn; i++){
        scanf("%d", &r1);
        r1 -= 1;
        for(int r = 0; r < 4; r++){
            for(int c = 0; c < 4; c++){
                if(r == r1) scanf("%d", row1+c);
                else scanf("%d", &tmp);
            }
        }
        scanf("%d", &r2);
        r2 -= 1;
        for(int r = 0; r < 4; r++){
            for(int c = 0; c < 4; c++){
                if(r == r2) scanf("%d", row2+c);
                else scanf("%d", &tmp);
            }
        }
        ansNum = 0;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                if(row1[j] == row2[k]) {
                    //printf("ans: %d\n", row1[j]);
                    ans[ansNum] = row1[j];
                    ansNum++;
                }
            }
        }
        if(ansNum == 0){
            printf("Case #%d: Volunteer cheated!\n", i+1);
        }
        else if(ansNum == 1){
            printf("Case #%d: %d\n", i+1, ans[0]);
        }
        else{
            printf("Case #%d: Bad magician!\n", i+1);
        }
    }
}
