#include<stdio.h>
#include<stdlib.h>
#define ll long long
#include<iostream>
#include<algorithm>
using namespace std;
ll v[1010];
int E,R,N;
int ans=0;
void dfs(int now,int scr,int nowe){
    if(now==N){
        ans=max(ans,scr);
        return;
    }
    for(int k=0;k<=nowe;k++){
        dfs(now+1,scr+v[now]*k,min(E,nowe-k+R));
    }
}
void solve(){

    cin >> E >> R >> N;
    for(int i=0;i<N;i++)cin >> v[i];
    ans=0;
    dfs(0,0,E);
    cout << ans << endl;
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
