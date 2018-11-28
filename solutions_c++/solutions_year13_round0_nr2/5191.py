#include <cstdio>
#define REP(i,n) for(int i=0; i<n; i++)
using namespace std;

int main(){
    int _test;
    scanf("%d",&_test);
    for(int tc=1; tc<=_test; tc++){
        bool correct=1;
        int grid[110][110];
        int cmp[110][110];
        int row,col;
        
        scanf("%d %d",&row,&col);
        REP(i,row){
            REP(j,col){
                scanf("%d",&grid[i][j]);
                cmp[i][j]=100;
            }
        }
        
        for(int h=99; h>=1; h--){
            for(int r=0; r<row; r++){
                bool ok=1;
                for(int c=0;c<col;c++)
                    ok &= h >= grid[r][c];
                
                if(ok){
                    for(int c=0; c<col;c++){
                        cmp[r][c] = h;
                    }
                }
            }
            
            for(int c=0; c<col; c++){
                bool ok=1;
                for(int r=0;r<row; r++)
                    ok &= h >= grid[r][c];
                    
                if(ok){
                    for(int r=0;r<row;r++){
                        cmp[r][c]=h;
                    }
                }
            }
        }
        
        for(int r=0;r<row;r++)
            for(int c=0;c<col;c++)
                if(grid[r][c] != cmp[r][c])
                    correct=0;
        printf("Case #%d: %s\n",tc,correct?"YES":"NO");
    }
    return 0;
}
