

#include <stdio.h>
#include <string.h>

using namespace std;


int T;

int R,C;


int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

int Dir(char c){
    if (c=='>') return 0;
    if (c=='<') return 1;
    if (c=='v') return 2;
    if (c=='^') return 3;
    return -1;
    
    
    
}

bool inside(int x,int y){
    
    if (x<0||y<0||x>=R||y>=C) return false;
    return true;
    
}

int main() {
    
    scanf("%d",&T);
    
    for (int case_number=1;case_number<=T;case_number++){
        
        char grid[105][105];
        
        int safe[105][105];
        
        scanf("%d %d",&R,&C);
        
        for (int i=0;i<R;i++) scanf("%s",grid[i]);
        
        int count=0;
        
        //count all the cells where I fall off.
        
        bool solvable=true;
        
        for (int i=0;i<R;i++)
            for (int j=0;j<C;j++){
                if (grid[i][j]=='.') continue;
                
                bool found_overall=false;
                
                for (int dir=0;dir<4;dir++){
                    bool found=false;
                    int x=i+dx[dir];
                    int y=j+dy[dir];
                    
                    while (inside(x,y)){
                        if (grid[x][y]!='.') { found=true; break;}
                        x=x+dx[dir];
                        y=y+dy[dir];
                    }
                    
                    if (found) found_overall=true;
                    if ((!found)&&dir==Dir(grid[i][j])) count++;
            
                    
                }
                
                if (!found_overall) {solvable=false; break;}
                
            }
        
        if (solvable) printf("Case #%d: %d\n",case_number,count); else printf("Case #%d: IMPOSSIBLE\n",case_number);
        
        
    }
    

    return 0;
}
