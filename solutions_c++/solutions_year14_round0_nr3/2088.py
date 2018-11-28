#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int a[5][5];
int cnt[5][5];
int flt[5][5];
int b[25];
int R,C,W;

int count(int r,int c){
    int ans=0;
    for(int i=-1;i<2;i++)
    for(int j=-1;j<2;j++){
       int tr=i+r;
       int tc=j+c;
       if(tr<0)continue;
       if(tr>=R)continue;
       if(tc<0)continue;
       if(tc>=C)continue;
       ans+=(a[tr][tc]==1?1:0);
    }
    return cnt[r][c]=ans;
}
int dfs(int r,int c){
    flt[r][c]=1;
    if(cnt[r][c]!=0)return 0;
    for(int i=-1;i<2;i++)
    for(int j=-1;j<2;j++){
       if(i==0&&j==0)continue;
       int tr=i+r;
       int tc=j+c;
       if(tr<0)continue;
       if(tr>=R)continue;
       if(tc<0)continue;
       if(tc>=C)continue;
       if(a[tr][tc]==0&& !flt[tr][tc])dfs(tr,tc);
    }
}
int check2(){
    for(int i=0;i<R;i++)
    for(int j=0;j<C;j++)if(a[i][j]==0&&flt[i][j]==0)return 0;
    return 1;

}
int check(int p,int b){
    if(p<C*R){
        a[p/C][p%C]=0;
        if(check(p+1,b))return 1;
        a[p/C][p%C]=1;
        if(check(p+1,b-1))return 1;
    }
    else{
        if(b!=0)return 0;
        for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)count(i,j);
        for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)if(a[i][j]==0){
            memset(flt,0,sizeof(flt));
            a[i][j]=2;
            dfs(i,j);
            if(check2()){
                for(int i=0;i<R;i++){
                    for(int j=0;j<C;j++)
                    switch(a[i][j]){
                    case 0:printf(".");break;
                    case 1:printf("*");break;
                    case 2:printf("c");break;
                    }
                    printf("\n");
                }
                return 1;
            }
            a[i][j]=0;
        }
        return 0;
    }
}
int main(){
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,flag;
    cin >> T;
    for(int t=1;t<=T;t++){

        cin >> R >> C >> W;
        printf("Case #%d:\n",t);
        if(!check(0,W)){
            printf("Impossible\n");
        }
    }
}
