#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <functional>
#include <cmath>
#define CLR(a) memset(a,0,sizeof(a))
typedef long long ll;
using namespace std;
char ans[60][60];
int dx[]={-1,0,1,-1,1,-1,0,1};
int dy[]={1,1,1,0,0,-1,-1,-1};
//bool vis[60][60];
bool dfs(int x,int y,int r,int c,int m,int cnt){
    //vis[x][y] = true;
    if(r*c == cnt+m+1){
        return true;
    }
        
    vector<int> vx,vy;
    for(int i=0;i<8;i++){
        int nx = x+dx[i],ny=y+dy[i];
        //cout<<nx<<" "<<ny<<endl;
        if(0<=nx&&nx<r && 0<=ny&&ny<c && ans[nx][ny] == 0){
            vx.push_back(nx);
            vy.push_back(ny);
            ans[nx][ny] = '.';
            // 
            cnt++;
        }
    }
    for(int i=0;i<vx.size();i++){
        if(dfs(vx[i],vy[i],r,c,m,cnt)){
            return true;
        }
    }
    for(int i=0;i<vx.size();i++){
        ans[vx[i]][vy[i]] = 0;
    }
    return false;

}
void solve(){
    int r,c,m;
    cin>>r>>c>>m;
    memset(ans,0,sizeof(ans));
    bool ok = false;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            ans[i][j] = 'c';
            //memset(vis,0,sizeof(vis));
            ok = dfs(i,j,r,c,m,0);
            if(ok)
                break;
            ans[i][j]=0;
        }
        if(ok){
            break;
        }
    }
    if(!ok){
        cout<<"Impossible\n";
    }else{
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(ans[i][j]==0)
                    cout<<'*';
                else
                    cout<<ans[i][j];
            }
            cout<<endl;
        }
    }
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int t,cs = 1;
    cin>>t;
    while(cs<=t) {
        cout<<"Case #"<<cs<<":\n";
        solve();
        cs++;
    }
}