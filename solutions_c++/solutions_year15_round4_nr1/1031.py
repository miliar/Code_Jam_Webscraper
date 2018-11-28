#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int n,m;
char mp[111][111];

int dx[]={0,-1,0,1}, dy[]={1,0,-1,0};
char dirch[]=">^<v";
int dire(char ch){
    for(int i=0; i<4; i++)
        if(ch==dirch[i])return i;
    return -10000;
}
bool inside(int x, int y){
    return 0<=x && x<n && 0<=y && y<m;
}

void input(){
    scanf("%d%d",&n,&m);
    for(int i=0; i<n; i++)scanf("%s",mp[i]);
}

void solve(){
    static int cas=1;
    printf("Case #%d: ",cas++);
    int res=0;
    bool ok[11];
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(mp[i][j]!='.'){
                //printf("%d, %d\n",i,j);
                int di=dire(mp[i][j]), found=0;
                memset(ok,0,sizeof(ok));
                for(int d=0; d<4; d++){
                    for(int x=i,y=j;;){
                        x+=dx[d], y+=dy[d];
                        if(!inside(x,y))break;
                        if(mp[x][y]!='.'){
                            ok[d]=found=1;
                            break;
                        }
                    }
                }
                if(!found){
                    printf("IMPOSSIBLE\n");
                    return;
                }else if(!ok[di])res++;
                //printf("found\n");
            }
        }
    }
    printf("%d\n",res);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int zz;
    scanf("%d",&zz);
    while(zz--){
        input();
        solve();
    }
    return 0;
}
