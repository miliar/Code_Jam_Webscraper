
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <list>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)

char board[50][50];
int dist[50][50];
int rows,cols;
int cross_delta[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};
int delta[8][2] = {{-1,0},{1,0},{0,1},{0,-1},{-1,-1},{1,1},{-1,1},{1,-1}};

void printBoard() {
    rep(i,rows) { 
        rep(j,cols) {
            cout << board[i][j];
        }
        cout << endl;
    }
}

bool onboard(int r, int c) {
    if (r<0 || r>=rows || c<0 || c>=cols) return false;
    return true;
}

bool isMine(int r, int c) {
    if (!onboard(r,c)) return false;
    return board[r][c] == '*';
}

int getDist(int r, int c) {
    if (!onboard(r,c)) return 100000;
    return dist[r][c];
}

bool isCool(int r, int c) {
    if (!onboard(r,c)) return false;
    rep(d,8) {
        int nr = r + delta[d][0];
        int nc = c + delta[d][1];
        if (isMine(nr,nc)) return false;
    }
    return true;
}

#define dbg false

bool isOk(int r, int c) {
    if (board[r][c] != '.') return false;
    char nboard[rows][cols];
    rep(i,rows) rep(j,cols) nboard[i][j]=board[i][j];
    list<pair<int,int>> queue;
    queue.push_back(make_pair(r,c));
    while (!queue.empty()) {
        pair<int,int> p = queue.front(); queue.pop_front();
        nboard[p.first][p.second]='d';
        if (isCool(p.first,p.second)) {
            rep(d,8) {
                int nr = p.first + delta[d][0];
                int nc = p.second + delta[d][1];
                if (onboard(nr,nc) && nboard[nr][nc]=='.') queue.push_back(make_pair(nr,nc));
            }
        }
    }
    if (dbg) {
        cout << endl;
        rep(i,rows) { 
            rep(j,cols) {
                cout << nboard[i][j];
            }
            cout << endl;
        }
    }
    rep(i,rows) rep(j,cols) if (nboard[i][j]=='.') return false;
    return true;
}

/*bool solve(int mines) {
    int wspaces = rows*cols-mines;
    rep(i,rows) rep(j,cols) board[i][j] = '*';
    int i=0,j=0;
    rep(w,wspaces) {
        board[i][j] = '.';
        pair<int,int> nextMove = make_pair(j,i);
        int cost=100000;
        rep(d,4) {
            int ni = i+cross_delta[d][0];
            int nj = j+cross_delta[d][1];
            int ndist = getDist(ni,nj);
            if (isMine(ni,nj) && ndist<cost) {
                nextMove = make_pair(ni,nj); cost=ndist;
            }
        }
        if (cost==100000) w--;
        i = nextMove.first; j = nextMove.second;
    }
    if (i==1 && j>1) {
        int nr=i,nc=j-1;
        swap(board[i][j],board[nr][nc]);
        while (onboard(nr+1,nc) && board[nr+1][nc]=='.') {
            swap(board[nr][nc],board[nr+1][nc]);
            nr++;
        }
    } else if (j==1 && i>1) {
        int nr = i-1, nc=j;
        swap(board[i][j],board[nr][nc]);
        while (onboard(nr,nc+1) && board[nr][nc+1]=='.') {
            swap(board[nr][nc],board[nr][nc+1]);
            nc++;
        }
    }
    if (dbg) printBoard();
    return isOk(0,0);
}*/

int bitcnt(int x) {
    int cnt=0;
    rep(i,31) {
        if ((1<<i) & x) cnt++;
    }
    return cnt;
}

bool solve(int mines, int &r, int &c) {
    int nsquares = rows*cols;
    for (int mask=0; mask<(1<<nsquares); mask++) {
        if (bitcnt(mask)==mines) {
            rep(i,rows) rep(j,cols) 
                board[i][j] = (mask & (1<<(i*cols+j))) ? '*' : '.';
            rep(i,rows) rep(j,cols)
                if (isOk(i,j)) {
                    r=i;c=j;
                    return true;
                }
        }
    }
    return false;
}

int main(int argc, char **argv) {
    int T,m,r,c;
    rep(j,50) dist[0][j]=j;
    rep(i,50) dist[i][0]=i;
    repf(i,1,49) repf(j,1,49) dist[i][j] = dist[i-1][j-1]+1;
    cin >> T;
    rep(i, T) {
        cin >> rows >> cols >> m;
        printf("Case #%d:\n",i+1);
        if (m==0) {
            rep(i,rows) rep(j,cols) board[i][j]='.';
            board[0][0]= 'c';
            printBoard();
        } else if (solve(m,r,c)) {
            board[r][c]='c';
            printBoard();
        } else {
            printf("Impossible\n");
        }
    }
}

