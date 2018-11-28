#include<cstdio>

char tbl[110][110];
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

int main(){
    int T;
    scanf("%d",&T);
    for(int cc = 1 ; cc <= T ; cc++){
        int R,C;
        scanf("%d %d",&R,&C);
        for(int c = 1 ; c <= R ; c++)
            scanf(" %s",tbl[c]+1);
        bool fail = false;
        int sol = 0;
        for(int c = 1 ; c <= R ; c++){
            for(int d = 1 ; d <= C ; d++){
                if(tbl[c][d] == '<'){
                    for(int e = d-1 ; e > 0 ; e--)
                        if(tbl[c][e] != '.')
                            goto xxx;
                    sol++;
                    for(int e = 0 ; e < 4 ; e++){
                        int nc = c+dir[e][0], nd = d+dir[e][1];
                        while(nc and nc <= R and nd and nd <= C){
                            if(tbl[nc][nd] != '.')
                                goto xxx;
                            nc += dir[e][0], nd += dir[e][1];
                        }
                    }
                    fail = true;
                    goto yyy;
                }
                if(tbl[c][d] == '>'){
                    for(int e = d+1 ; e <= C ; e++)
                        if(tbl[c][e] != '.')
                            goto xxx;
                    sol++;
                    for(int e = 0 ; e < 4 ; e++){
                        int nc = c+dir[e][0], nd = d+dir[e][1];
                        while(nc and nc <= R and nd and nd <= C){
                            if(tbl[nc][nd] != '.')
                                goto xxx;
                            nc += dir[e][0], nd += dir[e][1];
                        }
                    }
                    fail = true;
                    goto yyy;
                }
                if(tbl[c][d] == '^'){
                    for(int e = c-1 ; e > 0 ; e--)
                        if(tbl[e][d] != '.')
                            goto xxx;
                    sol++;
                    for(int e = 0 ; e < 4 ; e++){
                        int nc = c+dir[e][0], nd = d+dir[e][1];
                        while(nc and nc <= R and nd and nd <= C){
                            if(tbl[nc][nd] != '.')
                                goto xxx;
                            nc += dir[e][0], nd += dir[e][1];
                        }
                    }
                    fail = true;
                    goto yyy;
                }
                if(tbl[c][d] == 'v'){
                    for(int e = c+1 ; e <= R ; e++)
                        if(tbl[e][d] != '.')
                            goto xxx;
                    sol++;
                    for(int e = 0 ; e < 4 ; e++){
                        int nc = c+dir[e][0], nd = d+dir[e][1];
                        while(nc and nc <= R and nd and nd <= C){
                            if(tbl[nc][nd] != '.')
                                goto xxx;
                            nc += dir[e][0], nd += dir[e][1];
                        }
                    }
                    fail = true;
                    goto yyy;
                }
                xxx:;
            }
        }
        yyy:;
        printf("Case #%d: ",cc);
        if(fail)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",sol);
    }
}
