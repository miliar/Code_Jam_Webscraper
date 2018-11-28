#include <stdio.h>
#include <algorithm>
using namespace std;

const int INF = 100000000;

struct PT{
    int x,y;
};
PT c[20000][2];

int dis[2004][2004];
int ud[2004];
int u[2004];

inline int D(int a,int b){
    a-=b;
    return a>0?a:-a;
}

inline int btw(int a,int b,int c){
    return c>=a && c<=b;
}

inline int overlap(int a,int b,int c,int d){
    return btw(a,b,c) || btw(a,b,d) || btw(c,d,a) || btw(c,d,b);
}

inline int p2p(PT p1,PT p2){
    return max(D(p1.x,p2.x),D(p1.y,p2.y))-1;
}

inline int calc_dis(int a,int b){
    PT p1 = c[a][0];
    PT p2 = c[a][1];
    PT q1 = c[b][0];
    PT q2 = c[b][1];
    if(overlap(p1.x,p2.x,q1.x,q2.x)){
        return min(min(D(p1.y,q1.y),D(p1.y,q2.y)),min(D(p2.y,q1.y),D(p2.y,q2.y)))-1;
    }else if(overlap(p1.y,p2.y,q1.y,q2.y)){
        return min(min(D(p1.x,q1.x),D(p1.x,q2.x)),min(D(p2.x,q1.x),D(p2.x,q2.x)))-1;
    }else{
        int md = INF;
        for( int i=0; i<2; i++ ){
            for( int j=0; j<2; j++ ){
                p1.x = c[a][i].x;
                p1.y = c[a][j].y;
                for( int k=0; k<2; k++ ){
                    for( int h=0; h<2; h++ ){
                        p2.x = c[b][k].x;
                        p2.y = c[b][h].y;
                        md = min(md,p2p(p1,p2));
                    }
                }
            }
        }
        return md;
    }
}

int main(){
    int TT,W,H,n,N;
    scanf("%d",&TT);
    for( int tt=0; tt<TT; tt++ ){
        scanf("%d %d %d",&W,&H,&n);
        for( int i=0; i<n; i++ ){
            scanf("%d %d %d %d",&c[i][0].x,&c[i][0].y,&c[i][1].x,&c[i][1].y);
        }
        N = n+2;
        for( int i=0; i<n; i++ ){
            dis[i][n] = dis[n][i] = c[i][0].x;
            dis[i][n+1] = dis[n+1][i] = W-c[i][1].x-1;
        }
        dis[n][n] = dis[n+1][n+1] = 0;
        dis[n+1][n] = dis[n][n+1] = W;
        for( int i=0; i<n; i++ ){
            dis[i][i] = 0;
            for( int j=i+1; j<n; j++ ){
                dis[i][j] = dis[j][i] = calc_dis(i,j);
            }
        }
        for( int j=0; j<N; j++ ){
            ud[j] = INF;
            u[j] = 1;
        }
        ud[n] = 0;
        for( int i=0; i<N; i++ ){
            int md = INF+1;
            int mj;
            for( int j=0; j<N; j++ ){
                if(u[j] && ud[j]<md){
                    md = ud[j];
                    mj = j;
                }
            }
            u[mj] = 0;
            for( int j=0; j<N; j++ ){
                if(u[j] && ud[mj]+dis[mj][j]<ud[j]){
                    ud[j] = ud[mj]+dis[mj][j];
                }
            }
        }
        printf("Case #%d: %d\n",tt+1,ud[n+1]);
    }
    return 0;
}
