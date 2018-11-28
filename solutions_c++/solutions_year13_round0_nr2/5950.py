#include<stdio.h>
#include<memory.h>
int pattern[15][15];
int n,m;
bool check(int row, int col){
    bool row_legal = true;
    for(int i = 0;i<m;i++){
        if(pattern[row][i] != 1){
            row_legal = false;
            break;
        }
    }

    bool col_legal = true;
    for(int i=0;i<n;i++){
        if(pattern[i][col] != 1){
            col_legal = false;
            break;
        }
    }

    return row_legal || col_legal;
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("p2.out","w",stdout);
    int css;
    scanf("%d",&css);
    for(int cs=0;cs<css;cs++){

        memset(pattern,0,sizeof(pattern));
        n=m=0;
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                pattern[i][j] = 0;
                scanf("%d",&pattern[i][j]);
            }
        }

        bool all_one_legal = true;
        bool finish = false;
        for(int i=0;i<n && !finish;i++)
            for(int j=0;j<m && !finish;j++){
                if(pattern[i][j] == 1){
                    //if(check_row || check_col)
                    if(check(i,j) == false){
                        all_one_legal = false;
                        finish = true;
                        break;
                    }
                }
            }

        printf("Case #%d: ",cs+1);
        if(all_one_legal){
            printf("YES\n");
        }
        else
            printf("NO\n");

    }

    return 0;
}
