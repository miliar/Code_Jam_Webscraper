#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){
    int T;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    scanf("%d", &T);
    for(int t = 0; t < T; t++){
        int num1, num2;
        int mat1[4][4], mat2[4][4];
        scanf("%d", &num1);
        num1--;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &mat1[i][j]);
            }
        }
        scanf("%d", &num2);
        num2--;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                scanf("%d", &mat2[i][j]);
            }
        }
        int flag = 0, num;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(mat1[num1][i] == mat2[num2][j]){
                    flag++;
                    num = mat1[num1][i];
                    break;
                }
            }
        }
        if(flag == 1){
            printf("Case #%d: %d\n", t + 1, num);
        }
        else if(flag == 0){
            printf("Case #%d: Volunteer cheated!\n", t + 1);
        }
        else{
            printf("Case #%d: Bad magician!\n", t + 1);
        }
    }
    return 0;
}
