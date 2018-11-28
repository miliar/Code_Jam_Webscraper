#include <cstdio>
#include <queue>
#include <limits.h>
#include <cstring>
#include <map>
#include <string>
#include <vector>
using namespace std;
#define MAXN 10000
#define INF INT_MAX //nao ha perigo de overflow

int main(){
    int t;
    int mat[4][4],mat2[4][4];
    int res,res2,aux;
    int count;
    scanf("%d", &t);
    for(int a = 0; a<t;a++){
        count = 0,aux = 0;
        scanf("%d", &res);
        for(int i = 0;i<4;i++){
            for(int j = 0;j<4;j++){
                scanf("%d",&mat[i][j]);
            }
        }
        scanf("%d",&res2);
        for(int i = 0;i<4;i++){
            for(int j = 0;j<4;j++){
                scanf("%d",&mat2[i][j]);
            }
        }
        for(int i = 0;i< 4;i++){
            for(int j = 0;j<4;j++){
                if(mat[res-1][i] == mat2[res2-1][j]){
                    count++;
                    aux = mat[res-1][i];
                    //printf("%d %d\n", mat[res-1][i], count);
                }
            }
        }
        printf("Case #%d: ", a+1);
        if(count == 0)
            printf("Volunteer cheated!\n");
        else if(count == 1)
            printf("%d\n", aux);
        else
            printf("Bad magician!\n");

    }
}