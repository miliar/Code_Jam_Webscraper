#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <list>

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)
#define S 150
#define LIM 100

using namespace std;

struct Node {
    int x,y;
    int px, py;
    int d;
    char move;

    void setParams(int cx, int cy, int cpx, int cpy, int cd) {
        x=cx; y=cy; px=cpx; py=cpy; d=cd;
    }
};

Node mat[300][300];
int delta[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
const char *moves = "WESN";

void bfs() {
    mat[S][S].setParams(0,0,0,0,0);
    list<Node*> q;
    q.push_back(&mat[S][S]);
    while (q.size() > 0) {
        Node *x = q.front(); q.pop_front();
        int d = x->d;
        int nd = d+1;
        rep(i,4) {
            int nx = x->x + delta[i][0]*nd;
            int ny = x->y + delta[i][1]*nd;
            if (nx>=-LIM && nx<=LIM && ny >=-LIM && ny <= LIM) {
                if (mat[nx+S][ny+S].d==-1) {
                    mat[nx+S][ny+S].setParams(nx,ny,x->x,x->y,nd);
                    mat[nx+S][ny+S].move = moves[i];
                    q.push_back(&mat[nx+S][ny+S]);
                }
            }
        }
    }
}

void getAns(int x, int y, char *buf) {
    if (x==0 && y==0) return;
    Node *nd = &mat[S+x][S+y];
    buf[nd->d - 1] = nd->move;
    getAns(nd->px,nd->py,buf);
}

int main() {
    rep(i,300) rep(j,300) mat[i][j].d=-1;
    bfs();
    int tc,x,y;
    char buf[600];
    cin >> tc;
    rep(i,tc) {
        cin >> x >> y;
        getAns(x,y,buf);
        buf[mat[S+x][S+y].d]='\0';
        printf("Case #%d: %s\n",i+1,buf);
    }
}
