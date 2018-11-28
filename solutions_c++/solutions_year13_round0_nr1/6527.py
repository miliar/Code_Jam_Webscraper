#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#include<time.h>
#define N 4
using namespace std;
int t,a[N][N],dap,t_cnt,w[4][2]={{0,1},{1,0},{1,1},{1,-1}},b;
FILE *in,*out;
void input();
void solve();
int f(int x,int y,int z);
void output();
int output_no();
int main(){
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    input();
}
void input(){
    int i,j;
    char s[N][N];
    fscanf(in,"%d",&t);
    for(t_cnt=1;t_cnt<=t;t_cnt++){
        for(i=0;i<N;i++){
            fscanf(in,"%s",s[i]);
        }
        for(i=0;i<N;i++){
            for(j=0;j<N;j++){
                if(s[i][j]=='X'){
                    a[i][j]=1;
                }else if(s[i][j]=='O'){
                    a[i][j]=2;
                }else if(s[i][j]=='T'){
                    a[i][j]=3;
                }else{
                    a[i][j]=0;
                }
            }
        }
        solve();
        output();
    }
}
void solve(){
    int i,j;
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            printf("%d",a[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\n");



    dap=0;
    for(i=0;i<N;i++){
        if(a[i][0]!=0 && f(i,0,0)==1){
            dap=a[i][0];
            if(a[i][0]==3){
                dap=b;
            }
            return;
        }
        if(a[0][i]!=0 && f(0,i,1)==1){
            dap=a[0][i];
            if(a[0][i]==3){
                dap=b;
            }
            return;
        }
    }
    if(a[0][0]!=0 && f(0,0,2)==1){
        dap=a[0][0];
        if(a[0][0]==3){
            dap=b;
        }
        return;
    }
    if(a[0][3]!=0 && f(0,3,3)==1){
        dap=a[0][3];
        if(a[0][3]==3){
            dap=b;
        }
        return;
    }


}
int f(int x,int y,int z){
    int xx,xxx,yy,yyy,i;
    xx=xxx=x;
    yy=yyy=y;
    if(a[x][y]==3){
        xxx+=w[z][0];
        yyy+=w[z][1];
        b=a[xxx][yyy];
        if(b==0){
            return 0;
        }
    }
    for(i=0;i<3;i++){
        xx+=w[z][0];
        yy+=w[z][1];
        if(a[xx][yy]!=3 && a[xxx][yyy]!=a[xx][yy]){
            return 0;
        }
    }
    return 1;
}
void output(){
    if(dap==0){
        dap=output_no();
    }
    if(dap==1){
        fprintf(out,"Case #%d: X won\n",t_cnt);
    }else if(dap==2){
        fprintf(out,"Case #%d: O won\n",t_cnt);
    }else if(dap==3){
        fprintf(out,"Case #%d: Draw\n",t_cnt);
    }else if(dap==4){
        fprintf(out,"Case #%d: Game has not completed\n",t_cnt);
    }
}
int output_no(){
    int i,j;
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            if(a[i][j]==0){
                return 4;
            }
        }
    }
    return 3;
}
