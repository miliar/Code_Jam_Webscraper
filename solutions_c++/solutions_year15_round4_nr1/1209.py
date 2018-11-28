#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

char S[110][110];
int R,C;
const int dx[4]={0,0,1,-1};
const int dy[4]={1,-1,0,0};
int Dir(char op){
    if(op=='^')return 3;
    else if(op=='v')return 2;
    else if(op=='<')return 1;
    else return 0;
}
bool inmap(int cx,int cy){
    return cx>=0 && cx<R && cy>=0 && cy<C;
}
int solve(){
    cin>>R>>C;
    for(int i=0;i<R;i++){
        scanf("%s",S[i]);
    }
    bool ok=true;
    int ans=0;
    for(int i=0;i<R;i++)for(int j=0;j<C;j++)if(S[i][j]!='.'){
        int dir = Dir(S[i][j]);
        int cur = 0;
        bool ch = true;
        for(int k=0;k<4;k++){
            int cx=i+dx[k],cy=j+dy[k];
            while(inmap(cx,cy)){
                if(S[cx][cy]!='.'){
                    cur++;
                    if(k==dir)ch=false;
                    break;
                }
                cx+=dx[k];
                cy+=dy[k];
            }
        }
        if(cur==0)ok=false;
        if(ch)ans++;
    }
    return ok?ans:-1;
}
int main(){
    freopen("/Users/DXY/Desktop/DXY/in","r",stdin);
    freopen("/Users/DXY/Desktop/DXY/out","w",stdout);
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        int ans=solve();
        printf("Case #%d: ",i);
        if(ans==-1)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}