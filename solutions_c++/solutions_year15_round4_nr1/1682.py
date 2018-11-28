#include<cstdio>
#include<algorithm>
using namespace std;

int bae[101][101];
char bd[102][102];
int res[101][101]={0};
int bang[256];
int rr[4]={-1,0,1,0};
int cc[4]={0,1,0,-1};

int main(){
    int cnt,turn,t,r,c,i,j,ii,jj,recent[3],direc;
    bool err,can;
    //freopen("answer.txt","w",stdout);
    scanf("%d",&turn);
    bang['^']=0;
    bang['>']=1;
    bang['v']=2;
    bang['<']=3;
    for(t=1;t<=turn;t++){
        cnt=0;
        printf("Case #%d: ",t);
        scanf("%d %d",&r,&c);
        for(i=0;i<=100;i++){
            for(j=0;j<=100;j++){
                bae[i][j]=0;res[i][j]=0;
            }
        }
        for(i=0;i<r;i++){
            scanf("%s",bd[i]);
        }
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(bd[i][j]=='.') continue;
                else{
                    err=false;ii=i;jj=j;
                    while(bae[ii][jj]==0){

                        if(ii<0||ii==r){
                            err=true;
                            break;
                        }
                        if(jj<0||jj==c){
                            err=true;
                            break;
                        }
                        if(bd[ii][jj]!='.'){
                            if(bae[ii][jj]) break;
                            recent[0]=ii;recent[1]=jj;
                            direc=bang[bd[ii][jj]];
                            bae[ii][jj]=1;
                        }
                        ii+=rr[direc];jj+=cc[direc];
                    }
                    if(err){
                        res[recent[0]][recent[1]]=1;
                        cnt++;
                    }
                }
            }
        }
        err=false;
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(res[i][j]){
                    can=false;
                    for(int di=0;di<4;di++){
                        ii=i+rr[di];jj=j+cc[di];
                        while(1){
                            //printf("->%d %d %c\n",ii,jj,bd[ii][jj]);
                            if(ii<0||ii==r){
                                break;
                            }
                            if(jj<0||jj==c){
                                break;
                            }
                            if(bd[ii][jj]!='.'){
                                if(res[ii][jj]){
                                    res[i][j]=0;
                                }
                                can=true;
                                break;
                            }
                            ii+=rr[di];jj+=cc[di];
                        }
                        if(can) break;
                    }
                    if(!can){
                        err=true;
                        break;
                    }
                }
            }
            //if(err) break;
        }
        if(err){
            printf("IMPOSSIBLE\n");
        }else{
            printf("%d\n",cnt);
        }
    }
}
