#include <cstdio>
#include <cstring>
using namespace std;

int R, C;
char mz[50][50];
int love[100];

bool visited[50][50][4];

int idx(int r, int c, int pos) {
    if( r==0 && pos==0 )
        return c+1;
    if( c==C-1 && pos==1 )
        return C+r+1;
    if( r==R-1 && pos==2 )
        return C+R+(C-c);
    if( c==0 && pos==3 )
        return C+R+C+(R-r);
    return -1;
}

int dfs(int, int, int);
int A(int r, int c, int pos) {
    if( pos==0 ) {
        if( !visited[r][c][3] )
            return dfs(r, c, 3);
        if( r>0 && !visited[r-1][c][2] )
            return dfs(r-1, c, 2);
    }
    else if( pos==1 ) {
        if( !visited[r][c][2] )
            return dfs(r, c, 2);
        if( c<C-1 && !visited[r][c+1][3] )
            return dfs(r, c+1, 3);
    }
    else if( pos==2 ) {
        if( !visited[r][c][1] )
            return dfs(r, c, 1);
        if( r<R-1 && !visited[r+1][c][0] )
            return dfs(r+1, c, 0);
    }
    else {
        if( !visited[r][c][0] )
            return dfs(r, c, 0);
        if( c>0 && !visited[r][c-1][1] )
            return dfs(r, c-1, 1);
    }
    return idx(r, c, pos);
}
int B(int r, int c, int pos) {
    if( pos==0 ) {
        if( !visited[r][c][1] )
            return dfs(r, c, 1);
        if( r>0 && !visited[r-1][c][2] )
            return dfs(r-1, c, 2);
    }
    else if( pos==1 ) {
        if( !visited[r][c][0] )
            return dfs(r, c, 0);
        if( c<C-1 && !visited[r][c+1][3] )
            return dfs(r, c+1, 3);
    }
    else if( pos==2 ) {
        if( !visited[r][c][3] )
            return dfs(r, c, 3);
        if( r<R-1 && !visited[r+1][c][0] )
            return dfs(r+1, c, 0);
    }
    else {
        if( !visited[r][c][2] )
            return dfs(r, c, 2);
        if( c>0 && !visited[r][c-1][1] )
            return dfs(r, c-1, 1);
    }
    return idx(r, c, pos);
}
int dfs(int r, int c, int pos) {
    visited[r][c][pos] = true;
    if( mz[r][c]=='/' )
        return A(r, c, pos);
    else
        return B(r, c, pos);
}

bool ok() {
    memset(visited, 0, sizeof(visited));
    for(int i=0; i<C; ++i)
        if( !visited[0][i][0] &&
            dfs(0, i, 0) != love[idx(0, i, 0)] )
            return false;
    for(int i=0; i<R; ++i)
        if( !visited[i][C-1][1] &&
            dfs(i, C-1, 1) != love[idx(i, C-1, 1)] )
            return false;
    for(int i=0; i<C; ++i)
        if( !visited[R-1][i][2] &&
            dfs(R-1, i, 2) != love[idx(R-1, i, 2)] )
            return false;
    for(int i=0; i<R; ++i)
        if( !visited[i][0][3] &&
            dfs(i, 0, 3) != love[idx(i, 0, 3)] )
            return false;
    return true;
}

bool dfs(int r, int c) {
    if( r>=R ) return ok();
    if( c>=C ) return dfs(r+1, 0);
    mz[r][c] = '/';
    if( dfs(r, c+1) ) return true;
    mz[r][c] = '\\';
    return dfs(r, c+1);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int NOWCASE=1; NOWCASE<=T; ++NOWCASE) {
        scanf("%d%d", &R, &C);
        for(int i=R+C,a,b; i>0; --i) {
            scanf("%d%d", &a, &b);
            love[a] = b;
            love[b] = a;
        }
        printf("Case #%d:\n", NOWCASE);
        if( !dfs(0, 0) )
            puts("IMPOSSIBLE");
        else {
            for(int i=0; i<R; ++i) {
                for(int j=0; j<C; ++j)
                    printf("%c", mz[i][j]);
                puts("");
            }
        }
    }
    return 0;
}
