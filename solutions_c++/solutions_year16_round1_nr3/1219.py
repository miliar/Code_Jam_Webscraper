#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int N;
int Child[1005];
int Memo[1005];
int Ret;

bool isOk(int m) {
    for (int i=0;i<=m;++i){
        if (i==0){
            if (!(Child[Memo[i]]==Memo[m] || Child[Memo[i]]==Memo[1])) return 0;
        }
        else{
            if (!(Child[Memo[i]]==Memo[i-1] || Child[Memo[i]]==Memo[(i+1)%(m+1)])) return 0;
        }
    }
    return 1;
}
void DFS(int idx, int x) {
    Memo[idx]=x;
    if (isOk(idx)){
        Ret=max(Ret,idx+1);
    }
    
    for (int i=1;i<=N;++i){
        bool b=1;
        for (int j=0;j<=idx;++j) if (Memo[j]==i) b=0;
        if (b){
            DFS(idx+1,i);
        }
    }
    Memo[idx]=0;
}
void solve(){
    printf(" ");
    scanf("%d",&N);
    for (int i=1;i<=N;++i) {
        scanf("%d",&Child[i]);
    }
    
    Ret=-1;
    for (int i=1;i<=N;++i) DFS(0,i);
    printf("%d\n",Ret);
}

int main(){
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        printf("Case #%d:",test);
        solve();
    }
    return 0;
}
