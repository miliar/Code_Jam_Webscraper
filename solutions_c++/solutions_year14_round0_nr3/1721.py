#include <cstdio>
#include <cstring>
int r,c,m,cnt;
char f[5][5];
bool vst[5][5];
void check(int x,int y) {
    vst[x][y]=true;
    cnt++;
    for(int dx=-1;dx<=1;dx++) {
        for(int dy=-1;dy<=1;dy++) {
            int nx=x+dx,ny=y+dy;
            if(0>nx||nx>=c||0>ny||ny>=r) continue;
            if(f[nx][ny]=='*') return;
        }
    }
    for(int dx=-1;dx<=1;dx++) {
        for(int dy=-1;dy<=1;dy++) {
            int nx=x+dx,ny=y+dy;
            if(0>nx||nx>=c||0>ny||ny>=r) continue;
            if(!vst[nx][ny]) check(nx,ny);
        }
    }
}
bool make(int x,int y,int n) {
    if(y==r) {
        if(n<m) return false;
        for(int Y=0;Y<r;Y++) {
            for(int X=0;X<c;X++) {
                memset(vst,0,sizeof(vst));
                cnt=0;
                check(X,Y);
                if(cnt==(r*c-m)) {f[X][Y]='c'; return true;}
            }
        }
        return false;
    }
    int nx=x+1,ny=y;
    if(nx==c) {
        nx=0,ny++;
    }
    if(n==m) {
        f[x][y]='.';
        return make(nx,ny,n);
    }else {
        f[x][y]='.';
        if(make(nx,ny,n)) return true;
        f[x][y]='*';
        return make(nx,ny,n+1);
    }
}
void solve(int t) {
    printf("Case #%d:\n",t);
    scanf("%d %d %d",&r,&c,&m);
    if(make(0,0,0)) {
        for(int y=0;y<r;y++) {
            for(int x=0;x<c;x++) {
                putchar(f[x][y]);
            }
            putchar('\n');
        }
    }else {
        printf("Impossible\n");
    }
}
int main() {
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++) {
        solve(i);
    }
}
