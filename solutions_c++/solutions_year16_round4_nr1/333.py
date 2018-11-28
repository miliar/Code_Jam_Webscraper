#include<bits/stdc++.h>
using namespace std;
int cnt[3];
string dp[13][3];
int get(char c){
    if(c=='P')return 0;
    if(c=='R')return 1;
    return 2;
}
void solve(){
    int n;
    scanf("%d%d%d%d",&n,cnt+1,cnt+0,cnt+2);
    string rep="";
    for(int i=0;i<3;i++){
        int tmp[3]={0,0,0};
        for(int j=0;j<dp[n][i].size();j++){
            tmp[get(dp[n][i][j])]++;
        }
        if(tmp[0]!=cnt[0]||tmp[1]!=cnt[1]||tmp[2]!=cnt[2])continue;
        if(!rep.size()||rep>dp[n][i]){
            rep=dp[n][i];
        }
    }
    if(!rep.size())cout<<"IMPOSSIBLE"<<endl;
    else
    cout<<rep<<endl;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    dp[0][0]="P",dp[0][1]="R",dp[0][2]="S";
    for(int i=1;i<13;i++){
        for(int j=0;j<3;j++){
            dp[i][j]=dp[i-1][j]<dp[i-1][(j+1)%3]?(dp[i-1][j]+dp[i-1][(j+1)%3]):
                                                 (dp[i-1][(j+1)%3]+dp[i-1][j]);
        }
    }
    int cas=1;
    int _;scanf("%d",&_);
    while(_--){
        printf("Case #%d: ",cas++);
        solve();
    }
}
