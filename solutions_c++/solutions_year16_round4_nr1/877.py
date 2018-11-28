#include<cstdio>
int board[13][3];
int seq[13][5000];
char rsp[3]={'R','S','P'};

int cmp(int kk,int ii,int jj){
    for(int i=0;i<jj-ii;i++){
        if((1+seq[kk][i+ii])%3<(1+seq[kk][i+jj])%3) return 0;
        if((1+seq[kk][i+ii])%3>(1+seq[kk][i+jj])%3) return 1;
    }
}
int main(){
    int t,n,a[3],now,jj,tmp=0;
    bool fnd,can;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //0 : rock, 1: scissor, 2: paper
    seq[0][0]=0;
    board[0][0]=1;board[0][1]=0;board[0][2]=0;
    for(int i=1;i<=12;i++){
        board[i][0]=board[i-1][2]+board[i-1][0];
        board[i][1]=board[i-1][0]+board[i-1][1];
        board[i][2]=board[i-1][1]+board[i-1][2];
    }
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        fnd=false;
        can=false;
        scanf("%d %d %d %d",&n,&a[0],&a[2],&a[1]);
        printf("Case #%d: ",turn);
        for(int i=0;i<3;i++){
            can=true;
            for(int j=0;j<3;j++){
                if(a[(i+j)%3]!=board[n][j]){
                    can=false;
                    break;
                }
            }
            if(can){
                fnd=true;
                seq[0][0]=i;
                for(int ii=1;ii<=12;ii++){
                    for(int j=0;j<(1 << (ii));j++){
                        seq[ii][j]=(seq[ii-1][j/2]+(j%2))%3;
                        jj=j+1;now=1;
                        while(1){
                            if(jj%2) break;
                            if(cmp(ii,(jj-2)*now,(jj-1)*now)>0){
                                for(int kk=(jj-2)*now;kk<(jj-1)*now;kk++){
                                    tmp=seq[ii][kk];
                                    seq[ii][kk]=seq[ii][kk+now];
                                    seq[ii][kk+now]=tmp;
                                }
                            }
                            jj>>=1;now<<=1;
                        }
                    }
                }
                for(int j=0;j<(1 << n);j++){
                    printf("%c",rsp[seq[n][j]]);
                }
                printf("\n");
                break;
            }
        }
        if(!fnd){
            printf("IMPOSSIBLE\n");
        }
    }
}
