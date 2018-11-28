#include<iostream>
#include<cstdio>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<queue>
using namespace std;

struct point{
    int x,y;
    point(){}
    point(int _x,int _y){
        x = _x;
        y = _y;
    }
};

int n,m;
int adj[109][109];

int gao(int x,int y){
    int cur = 0;
    for(int i=0;i<m;i++){
        if(adj[x][i]>adj[x][y]){
            cur ++;
            break;
        }
    }
    for(int i=0;i<n;i++){
        if(adj[i][y]>adj[x][y]){
            cur ++;
            break;
        }
    }
    if(cur==2) return 0;
    return 1;
}

int check(){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!gao(i,j)) return 0;
        }
    }
    return 1;
}

int main(){
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&adj[i][j]);
        printf("Case #%d: ",cas);
        if(check()) puts("YES");
        else puts("NO");
    }
    return 0;
}
