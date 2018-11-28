// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 6;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

int dx[]={1,-1,0,0,1,1,-1,-1};
int dy[]={0,0,1,-1,1,-1,-1,1};
int r,c,m;

char grid[M][M];
char copy_grid[M][M];

void print_grid() {
    for(int i=0;i<r;++i) {
        copy_grid[i][c] = 0;
        puts(copy_grid[i]);
    }
}

void dfs(int x, int y) {
    if(copy_grid[x][y] != '.') return;

    int count = 0;
    for(int i=0;i<8;++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >=0 && nx <r && ny >=0 && ny < c && copy_grid[nx][ny] == '*') ++count;
    }

    copy_grid[x][y] = count + '0';

    if(count == 0) {
        for(int i=0;i<8;++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >=0 && nx <r && ny >=0 && ny < c) dfs(nx, ny);
        }
    }
}

bool is_one_click(int x, int y) {
    memcpy(copy_grid, grid, sizeof(char) * M * M);

    dfs(x,y);
    for(int i=0;i<r;++i) {
        for(int j=0;j<c;++j) {
            if(copy_grid[i][j] == '.') return false;
        }
    }

    memcpy(copy_grid, grid, sizeof(char) * M * M);
    copy_grid[x][y] = 'c';
    return true;
}

bool try_grid(int mask) {

    SET(grid, '.');
    int sq = r * c;
    for(int i=0;i<sq;++i) {
        if(mask & (1<<i)) {
            grid[i/c][i%c] = '*';
        }
    }

    for(int i=0;i<r;++i) {
        for(int j=0;j<c;++j) {
            if(grid[i][j] == '.' && is_one_click(i,j))  {
                print_grid();
                return true;
            }
        }
    }
    return false;
}

bool solve() {

    int sq = r * c;
    for(int i=0;i< (1<<sq); ++i) {
        if(__builtin_popcount(i) != m) continue;
        
        if(try_grid(i)) return true;
    }
    return false;
}

int main() {
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;++t) {
        scanf("%d %d %d",&r,&c,&m);
        printf("Case #%d:\n",t);
        bool is_solved = solve();
        if(!is_solved) {
            puts("Impossible");
        }
    }
    return 0;
}

