#include <iostream>
#include <cstring>
#include <queue>
#include <cstdio>
using namespace std;

char a[6][6];
int N,K;
int P[5];
int ck[5];
int ans,countt = 0;;
int mat[5];
bool cc;
int xx = 0;
int fact[5]={1,1,2,6,24};
void check(int now){
    if(now==N) return;
    
    bool is = false;
    for(int i=0;i<N;i++){
        if(a[P[now]-1][i] == '1' && mat[i]==0){
            mat[i] = P[now];
            check(now+1);
            mat[i] = 0;
            is = true;
        }
    }
    if(!is){
        cc = false;
    }
}
void dfs2(int x){
    if(x==N){
        cc  = true;
        check(0);
        if(cc){
            xx ++;
        }
        return;
    }
    for(int i=1;i<=N;i++){
        if(ck[i]) continue;
        P[x] = i;
        ck[i] = 1;
        dfs2(x+1);
        ck[i] = 0;
    }
}

void dfs(int x,int y){
    int nx=x,ny=y+1;
    if(ny==N){
        nx++;
        ny = 0;
    }
    if(x == N){
        memset(ck,0,sizeof(ck));
        xx=0;
        dfs2(0);
        if( xx ==  fact[N]){
            ans = min(ans,countt);
        }
        return;
    }
    
    if(a[x][y] == '0'){
        a[x][y] = '1';
        countt ++;
        dfs(nx,ny);
        countt --;
        a[x][y] = '0';
        dfs(nx,ny);
    } else {
        dfs(nx,ny);
    }
}

int main(){
    
    freopen("/Users/clsrn1581/Desktop/xcode/practice/practice/input.txt","r",stdin);
    freopen("/Users/clsrn1581/Desktop/xcode/practice/practice/output.txt","w",stdout);

    int testcase;
    scanf("%d",&testcase);
    
    for(int t=1;t<=testcase;t++){
        
        scanf("%d",&N);
        ans = 11111;
        for(int i=0;i<N;i++){
            scanf("%s",a[i]);
        }
        dfs(0,0);
        
        printf("Case #%d: %d\n",t,ans);
        
    }
    
    return 0;
}