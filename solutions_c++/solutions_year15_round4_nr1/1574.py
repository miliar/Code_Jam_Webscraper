#include<bits/stdc++.h>
using namespace std;
char mp[128][128];
int cc[128][128] = {};
bool tag[128][128];
int r,c;

int dfs(int x,int y,int wx,int wy){
    if(x<0 || x>=r || y<0 || y>=c)
        return -2;
    if(tag[x][y])
        return -1;
    if(cc[x][y]>0 && cc[x][y]!=x*1000+y)
        return cc[x][y];
    if(mp[x][y]=='.'){
        cc[x][y]=-1;
        return dfs(x+wx,y+wy,wx,wy);
    }
    if(mp[x][y]=='^')
        wx=-1,wy=0;
    if(mp[x][y]=='v')
        wx=1,wy=0;
    if(mp[x][y]=='>')
        wx=0,wy=1;
    if(mp[x][y]=='<')
        wx=0,wy=-1;
    tag[x][y]=true;
    int r = dfs(x+wx,y+wy,wx,wy);
    tag[x][y]=false;
    if(r==-2)
        return cc[x][y];
    return cc[x][y]=r;
}   
        
bool ck(int x,int y){
    for(int i=0;i<r;i++){
        if(i!=x && mp[i][y]!='.')
            return true;
    }
    for(int j=0;j<c;j++){
        if(j!=y && mp[x][j]!='.')
            return true;
    }
    return false;
}

int main(){
    int t,tk=0;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",mp[i]);
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cc[i][j]=1000*i+j;
            }
        }
        memset(tag,0,sizeof(tag));
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(mp[i][j]=='.')
                    cc[i][j]=-1;
                else
                    dfs(i,j,0,0);
            }
        }
        int ans=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(cc[i][j]==i*1000+j){
                    if(ck(i,j))
                        ans++;
                    else
                        ans=-99999999;
                }
            }
        }
        if(ans<0)
            printf("Case #%d: IMPOSSIBLE\n",++tk);
        else
            printf("Case #%d: %d\n",++tk,ans);
    }
}
