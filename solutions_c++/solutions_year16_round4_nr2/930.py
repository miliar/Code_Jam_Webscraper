#include <iostream>
#include <cstring>
#include <queue>
#include <cstdio>
using namespace std;

char a[6][6];
int N,K;

int check[20];
int check2[20];
double input[20];
double ans = 0.0, ans2;
void dfs2(int x,int cnt){
    
    if(cnt > K/2) return;
    if(x == N && cnt == K/2){
        double A=1.0,B= 1.0;
        for(int i=0;i<N;i++){
            if(check[i] && check2[i]) {
                A*=input[i];
            }
            if(check[i] && !check2[i]) {
                B*=(1.0-input[i]);
            }
        }
        double temp = A*B;
        A=1.0,B=1.0;
        for(int i=0;i<N;i++){
            if(check[i] && check2[i]) {
                A*=(1.0-input[i]);
            }
            if(check[i] && !check2[i]) {
                B*=(input[i]);
            }
        }
        ans2 += temp + A*B;

        return;
    }
    if(x==N) return;
    
    if(check[x]){
        check2[x] = 1;
        dfs2(x+1,cnt+1);
    }
    check2[x] = 0;
    dfs2(x+1,cnt);
}

void dfs(int x,int cnt){
    
    if(cnt > K) return;
    if(x == N && cnt == K){
        ans2=0.0;
        dfs2(0,0);
        ans = max(ans,ans2);
        return;
    }
    if(x==N) return;
    
    check[x] = 1;
    dfs(x+1,cnt+1);
    check[x] = 0;
    dfs(x+1,cnt);
}

int main(){
    
    freopen("/Users/clsrn1581/Desktop/xcode/practice/practice/input.txt","r",stdin);
    freopen("/Users/clsrn1581/Desktop/xcode/practice/practice/output.txt","w",stdout);

    int testcase;
    scanf("%d",&testcase);
    
    for(int t=1;t<=testcase;t++){
        
        scanf("%d%d",&N,&K);
        
        for(int i=0;i<N;i++){
            cin >> input[i];
        }
        memset(check,0,sizeof(check));
        ans = 0.0;
        dfs(0,0);
        
        
        printf("Case #%d: %lf\n",t,ans/2);
        
    }
    
    return 0;
}