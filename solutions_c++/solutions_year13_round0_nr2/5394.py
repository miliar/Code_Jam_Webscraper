#include<cstdio>
#include<cstring>

using namespace std;

int mat[101][101];
int maxRow[101];
int maxCol[101];

int main() {
    int t;
    int caseNum = 1;
    scanf("%d",&t);
    for(;caseNum <= t;caseNum++){
        memset(maxCol,0,sizeof(maxCol));
        memset(maxRow,0,sizeof(maxRow));
        int row = 0;
        int col = 0;
        scanf("%d%d",&row,&col);
        for(int i = 0;i<row;i++) {
            for(int j = 0;j<col;j++) {
                int tmp;
                scanf("%d",&tmp);
                mat[i][j] = tmp;
                if(tmp>maxCol[j]) {
                    maxCol[j] = tmp;
                }
                if(tmp>maxRow[i]) {
                    maxRow[i] = tmp;
                }
            }
        }
        for(int i = 0;i<row;i++) {
            for(int j = 0;j<col;j++) {
                if(mat[i][j]!=maxRow[i]&&mat[i][j]!=maxCol[j]){
                    printf("Case #%d: NO\n",caseNum);
                    goto BREAK;
                }
            }
        }
        printf("Case #%d: YES\n",caseNum);
        BREAK:;
    }
    return 0;
}

