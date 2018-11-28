#include<stdio.h>
#include<string.h>
#include<memory.h>
FILE *fo = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Round2/1/input.txt","r");
FILE *fp = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Round2/1/output.txt","w");
char Depth[13][3][4500];
int cnt[13][3][3];
int main(){
    int t,T;
    fscanf(fo,"%d",&T);
    // 0 -> P, 1 -> R, 2 -> S;
    Depth[0][0][0]='P';
    Depth[0][1][0]='R';
    Depth[0][2][0]='S';
    cnt[0][0][0] = 1;
    cnt[0][1][1] = 1;
    cnt[0][2][2] = 1;
    int mult = 1;
    for(int n=1;n<=12;n++){
        // P -> P, R
        // R -> R, S
        // S -> S, P
        for(int j=0;j<3;j++) {
            int now = j, next = (j+1)%3;
            bool go_now = true;
            int i;
            for(i=0;i<3;i++){
                cnt[n][now][i] = cnt[n-1][now][i] + cnt[n-1][next][i];
            }
            for (i = 0; i < mult; i++) {
                if (Depth[n - 1][now][i] < Depth[n - 1][next][i]) {
                    break;
                }
                else if(Depth[n-1][now][i] > Depth[n-1][next][i]){
                    go_now = false;
                    break;
                }
            }
            if(go_now){
                for(i=0;i<mult;i++){
                    Depth[n][now][i] = Depth[n-1][now][i];
                    Depth[n][now][i+mult] = Depth[n-1][next][i];
                }
            }else{
                for(i=0;i<mult;i++){
                    Depth[n][now][i] = Depth[n-1][next][i];
                    Depth[n][now][i+mult] = Depth[n-1][now][i];
                }
            }
        }
        mult *= 2;
    }
    for(t=1;t<=T;t++){
        int P,R,S,N;
        fscanf(fo,"%d %d %d %d",&N,&R,&P,&S);
        fprintf(fp,"Case #%d: ",t);
        int i,j;
        char ans[4500]={0,};
        bool check = false;
        for(i=0;i<3;i++){
            if(cnt[N][i][0] == P && cnt[N][i][1] == R && cnt[N][i][2] == S){
                bool change = false;
                if(check){
                    for(j=0;j<(1<<N);j++){
                        if(ans[j] > Depth[N][i][j]){
                            change = true;
                            break;
                        }
                        else if(ans[j] < Depth[N][i][j]){
                            break;
                        }
                    }
                }else {
                    change = true;
                }
                if(change){
                    for(j=0;j<(1<<N);j++){
                        ans[j] = Depth[N][i][j];
                    }
                }
                check = true;
            }
        }
        if(check){
            fprintf(fp,"%s\n",ans);
        }
        else{
            fprintf(fp,"IMPOSSIBLE\n");
        }
    }
    return 0;
}