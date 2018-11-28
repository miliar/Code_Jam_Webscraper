#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
#include<set>
#include<map>
using namespace std;


int board[100][100];
bool gone[100][100];
pair<int,int> q[10000];
int _front,_rear;
int r,c,m;
int _try(int x,int y){
    int ret=0;
    if(x<0||x>=r||y<0||y>=c)return ret;
    if(!gone[x][y]){gone[x][y]=1;ret++;}
    else return ret;
    if(board[x][y]==0){
    for(int dx=-1;dx<=1;++dx)
        for(int dy=-1;dy<=1;++dy){
            ret+=_try(x+dx,y+dy);
        }
    }
        return ret;
}
void push(int x,int y){
    if(x<0||x>=r||y<0||y>=c)return;
    if(gone[x][y])return;
    q[_rear++]=make_pair(x,y);
    gone[x][y]=true;
}

void solve_hard(){

    for(int i = 0 ; i < r ; ++ i ) for(int j = 0 ; j < c ; ++ j ) board[i][j]=100;

    int need =r*c-m;
    if(need>=8){
        need-=8;
        for( int i = 0 ; i < 3 ; ++ i ) for(int j = 0 ; j < 3 ; ++ j ){
            board[i][j]=9;
        }
        board[2][2]=100;
    }
    for(int i = 0 ; i < r && need>0 ; ++ i ){
        for(int j = 0 ; j < c && need>0 ; ++ j ){
            //printf("need=%d\n",need);

            if(j==0&&need>2){
                if(board[i+1][j]>0){
                    int del =0 ;
                    if(board[i+1][j]==100)del++;
                    for(int dx=0;dx<=1;++dx)
                        for(int dy=0;dy<=1;++dy){
                            if(i+1+dx>=r||j+dy>=c)continue;
                            if ( board[i+1+dx][j+dy]== 100 ) del++;
                        }
                    if(need-del>=0){
                        if(board[i+1][j]==100)need--;
                        board[i+1][j]=0;
                        for(int dx=0;dx<=1;++dx)
                            for(int dy=0;dy<=1;++dy){
                                if(i+1+dx>=r||j+dy>=c)continue;
                                if ( board[i+1+dx][j+dy]== 100 ) board[i+1+dx][j+dy]=9,--need;
                            }
                    }
                }
            }
            if(board[i][j]>0){
                int del =0 ;
                if(board[i][j]==100)del++;
                for(int dx=0;dx<=1;++dx)
                    for(int dy=0;dy<=1;++dy){
                        if(i+dx>=r||j+dy>=c)continue;
                        if ( board[i+dx][j+dy]== 100 ) del++;
                    }
                if(need-del>=0){
                    if(board[i][j]==100)need--;
                    board[i][j]=0;
                    for(int dx=0;dx<=1;++dx)
                        for(int dy=0;dy<=1;++dy){
                            if(i+dx>=r||j+dy>=c)continue;
                            if ( board[i+dx][j+dy]== 100 ) board[i+dx][j+dy]=9,--need;
                        }
                }
            }
        }

    }
    if(need==0){
        for(int i =0 ; i  < r ; ++ i ){
            for(int j = 0 ; j < c ; ++ j ){
                if(i==0&&j==0)printf("c");
                else printf("%c",board[i][j]==100?'*':'.');
            }
            printf("\n");
        }
        return;
    }
    need =r*c-m;
    if(need>=8){
        need-=8;
        for( int i = 0 ; i < 3 ; ++ i ) for(int j = 0 ; j < 3 ; ++ j ){
            board[i][j]=9;
        }
        board[2][2]=100;
    }
    for(int i = 0 ; i < r ; ++ i ) for(int j = 0 ; j < c ; ++ j ) board[i][j]=100;
    for(int j = 0 ; j < c && need>0 ; ++ j ){
        for(int i = 0 ; i < r && need>0 ; ++ i ){
            //printf("need2=%d\n",need);
             if(i==0&&need>2){
                if(board[i][j+1]>0){
                    int del =0 ;
                    if(board[i][j+1]==100)del++;
                    for(int dx=0;dx<=1;++dx)
                        for(int dy=0;dy<=1;++dy){
                            if(i+dx>=r||j+1+dy>=c)continue;
                            if ( board[i+dx][j+1+dy]== 100 ) del++;
                        }
                    if(need-del>=0){
                        if(board[i][j+1]==100)need--;
                        board[i][j+1]=0;
                        for(int dx=0;dx<=1;++dx)
                            for(int dy=0;dy<=1;++dy){
                                if(i+dx>=r||j+1+dy>=c)continue;
                                if ( board[i+dx][j+1+dy]== 100 ) board[i+dx][j+1+dy]=9,--need;
                            }
                    }
                }
            }
            if(board[i][j]>0){
                int del =0 ;
                if(board[i][j]==100)del++;
                for(int dx=0;dx<=1;++dx)
                    for(int dy=0;dy<=1;++dy){
                        if(i+dx>=r||j+dy>=c)continue;
                        if ( board[i+dx][j+dy]== 100 ) del++;
                    }
                if(need-del>=0){
                    if(board[i][j]==100)need--;
                    board[i][j]=0;
                    for(int dx=0;dx<=1;++dx)
                        for(int dy=0;dy<=1;++dy){
                            if(i+dx>=r||j+dy>=c)continue;
                            if ( board[i+dx][j+dy]== 100 ) board[i+dx][j+dy]=9,--need;
                        }
                }
            }
        }

    }
    if(need==0){
        for(int i =0 ; i  < r ; ++ i ){
            for(int j = 0 ; j < c ; ++ j ){
                if(i==0&&j==0)printf("c");
                else printf("%c",board[i][j]==100?'*':'.');
            }
            printf("\n");
        }
        return;
    }
    printf("Impossible\n");
}

void solve(){

    scanf("%d %d %d",&r,&c,&m);
    if(r>2&&c>2&&(r*c-m>1))return solve_hard();
    _front=_rear=0;
    memset(gone,0,sizeof(gone));
    memset(board,0,sizeof(board));

    push(0,0);
    for(int i = 0 ; i < m ; ++ i ){
        pair<int,int> cur = q[_front++];
        board[cur.first][cur.second]=100;
        for(int dx=-1;dx<=1;++dx)
            for(int dy=-1;dy<=1;++dy)
                push(cur.first+dx,cur.second+dy);
    }


    memset(gone,0,sizeof(gone));
    for(int i = 0 ; i < r ; ++ i )
        for(int j  = 0 ; j < c ; ++ j ){
            if(board[i][j]==0){

                for(int dx=-1;dx<=1;++dx)
                    for(int dy=-1;dy<=1;++dy)
                        if(i+dx>=0&&i+dx<r&&j+dy>=0&&j+dy<c && board[i+dx][j+dy]==100)board[i][j]++;
            }
        }

    for(int i = 0 ; i <r ; ++ i ){
        for(int j = 0 ; j< c ; ++ j ){
            if( board[i][j]!=100){
                memset(gone,0,sizeof(gone));
                int z = _try(i,j);
                if(z== r*c-m){
                    for(int x = 0 ; x < r ; ++ x){
                        for(int y = 0 ;  y< c ; ++ y ){

                            (x==i&&y==j)?printf("c"):printf("%c",board[x][y]==100?'*':'.');
                        }
                        printf("\n");
                    }

                    return;
                }
            }
        }
    }

    memset(gone,0,sizeof(gone));
    memset(board,0,sizeof(board));
    _front=_rear=0;
    push(0,0);
    for(int i = 0 ; i < m ; ++ i ){
        pair<int,int> cur = q[_front++];
        board[cur.first][cur.second]=100;
        for(int dy=-1;dy<=1;++dy)
            for(int dx=-1;dx<=1;++dx)

                push(cur.first+dx,cur.second+dy);
    }


    memset(gone,0,sizeof(gone));
    for(int i = 0 ; i < r ; ++ i )
        for(int j  = 0 ; j < c ; ++ j ){
            if(board[i][j]==0){

                for(int dx=-1;dx<=1;++dx)
                    for(int dy=-1;dy<=1;++dy)
                        if(i+dx>=0&&i+dx<r&&j+dy>=0&&j+dy<c && board[i+dx][j+dy]==100)board[i][j]++;
            }
        }

    for(int i = 0 ; i <r ; ++ i ){
        for(int j = 0 ; j< c ; ++ j ){
            if( board[i][j]!=100){
                memset(gone,0,sizeof(gone));
                int z = _try(i,j);
                if(z== r*c-m){
                    for(int x = 0 ; x < r ; ++ x){
                        for(int y = 0 ;  y< c ; ++ y ){

                            (x==i&&y==j)?printf("c"):printf("%c",board[x][y]==100?'*':'.');
                        }
                        printf("\n");
                    }

                    return;
                }
            }
        }
    }

    printf("Impossible\n");
}

int main(){
    freopen("C-small-attempt3.in","r",stdin);
    freopen("C.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d:\n",i);
        solve();
    }
}
