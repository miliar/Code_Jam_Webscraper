#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <cstdio>
#include <cstring>
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}

char G[100][100];
bool vis[100][100];
using namespace std;
int dx[] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[] = {1, -1, 0, 0, 1, -1, 1, -1};
int r,c;
bool mamada(int x, int y){
    //cout<<"mierda";
    for(int i=0;i<8;i++){
        int cx=x+dx[i];
        int cy=y+dy[i];
        if(cx>=0&&cy>=0&&cx<r&&cy<c&&G[cx][cy]=='*'){
            return false;
            }
    }
    return true;
}
void dfs(int x,int y){
    if(vis[x][y]||x<0||y<0||x>=r||y>=c)return;
    vis[x][y]=true;
    if(!mamada(x,y))return;
    for(int i=0;i<8;i++){
        int cx=x+dx[i];
        int cy=y+dy[i];
        dfs(cx,cy);
    }
}
void solve(){
    int minas;
    cin>>r>>c>>minas;
    string troll="";
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(minas)troll+="*",minas--;
            else troll+=".";
        }
    }
    sort(troll.begin(),troll.end());
    do{
        int cholo=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                G[i][j]=troll[cholo++];
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(G[i][j]=='.'){
                    memset(vis,0,sizeof vis);
                    dfs(i,j);
                    bool lecholo=true;
                    for(int q=0;q<r;q++){
                        for(int w=0;w<c;w++){
                            if(!vis[q][w]){
                                if(G[q][w]!='*'){
                                lecholo=false;goto xd;}
                            }
                        }
                    }
                    xd:
                    if(lecholo){
                        G[i][j]='c';
                        for(int q=0;q<r;q++){
                            for(int w=0;w<c;w++){
                                cout<<G[q][w];
                            }
                            cout<<endl;
                        }
                        return;
                    }
                }
            }
        }
    }while (next_permutation(troll.begin(),troll.end()));
    cout<<"Impossible\n";
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases=in();
    for(int tc=1;tc<=cases&&printf("Case #%d:\n",tc++);)solve();
    return 0;
}
