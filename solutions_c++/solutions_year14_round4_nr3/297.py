//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int w,h,b;
int X1[1047], Y1[1047], X2[1047], Y2[1047];
int B[2047][2047];
int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

void fill(int x1, int y1, int x2, int y2){
    for(int i = x1; i<x2; i++)
        for(int j = y1; j<y2; j++)
            B[i][j] = 0;

}

bool dfs(int x, int y, int d){
    if (x<0 || y<0 || x>=w || y>=h) return 0;
    if (B[x][y]==0) return 0;
    B[x][y] = 0;
    if (y==h-1) return 1;
    
    For(i, 4){
        int s = (d+3+i)%4;
        if (dfs(x+dx[s],y+dy[s], s)) return 1;
    }
    return 0;
}

int extra(){
    scanf("%d%d%d",&w, &h, &b);
    For(i, w) For(j, h) B[i][j] = 1;
    For(i, b){
        scanf("%d%d%d%d", X1+i,Y1+i,X2+i,Y2+i);
        fill(X1[i],Y1[i],X2[i]+1,Y2[i]+1);
    }
    int flow = 0;
    For(x, w) if (dfs(x, 0, 0)) flow++;
    printf("%d\n", flow);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
