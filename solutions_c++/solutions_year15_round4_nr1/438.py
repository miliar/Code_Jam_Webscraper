#include<bits/stdc++.h>
#pragma GCC optimize ("O3")
#define f first
#define s second
using namespace std;
char mp[105][105];
int r,c;
bool chk(int x,int y,int vx,int vy){
    x+=vx;
    y+=vy;
    while(1){
        if(x<0||y<0||x>=r||y>=c)return 0;
        if(mp[x][y]!='.')return 1;
        x+=vx;
        y+=vy;
        }
    return 0;
    }
int main(){
    int T,t=0;
    scanf("%d",&T);
    while(T--){t++;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",mp[i]);
        printf("Case #%d: ",t);
        int ans=0,inp=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                char x=mp[i][j];
                if(x!='.'){
                    bool stat;
                    if(x=='^')stat=chk(i,j,-1,0);
                    if(x=='v')stat=chk(i,j,1,0);
                    if(x=='>')stat=chk(i,j,0,1);
                    if(x=='<')stat=chk(i,j,0,-1);
                    if(!stat){
                        stat=chk(i,j,-1,0)||chk(i,j,0,-1)||chk(i,j,0,1)||chk(i,j,1,0);
                        if(stat)ans++;
                        else inp=1;
                        }
                    }
                }
            }
        if(inp)puts("IMPOSSIBLE");
        else printf("%d\n",ans);
        }
    return 0;
    }
