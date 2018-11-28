#include<cstdio>

using namespace std;
int A[10][10], B[10][10];

int main(){
    int t,a,b,i,j,k,res=-1;
    scanf("%d", &t);
    for (i = 0; i < t; i++){
        scanf("%d", &a);
        for (j = 0; j < 4; j++){
            for (k = 0; k < 4; k++){
                scanf("%d", &A[j][k]);
            }
        }
        scanf("%d", &b);
        for (j = 0; j < 4; j++){
            for (k = 0; k < 4; k++){
                scanf("%d", &B[j][k]);
            }
        }
        for (j = 0; j < 4; j++){
            for (k = 0; k < 4; k++){
                if (A[a-1][j] == B[b-1][k]){
                    if (res != -1)
                        break;
                    res = A[a-1][j];
                }
            }
            if (k < 4)
                break;
        }
        if (j < 4)
            printf("Case #%d: Bad magician!\n", i+1);
        else if (res == -1)
            printf("Case #%d: Volunteer cheated!\n", i+1);
        else
            printf("Case #%d: %d\n", i+1, res);
        res = -1;
    }
}
