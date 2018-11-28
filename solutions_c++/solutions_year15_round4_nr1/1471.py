#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

pair < int , int > charToWay[200];

char grid[105][105];
pair < int , int > way[105][105];
char buf[105];
int r, c;

int sumRow[105], sumCol[105];

bool visited[105][105];
bool f[105][105];
pair < int , int > nextCell[105][105];

void buildPairToWay () {
    charToWay['^'] = make_pair(-1, 0);
    charToWay['>'] = make_pair(0, 1);
    charToWay['v'] = make_pair(1, 0);
    charToWay['<'] = make_pair(0, -1);
}

bool inField (int x, int y) {
    return x > -1 && x < r && y > -1 && y < c;
}

bool checkBadCell () {
    for (int i = 0; i < r; i++) {
        sumRow[i] = 0;
        for (int j = 0; j < c; j++) {
            if (grid[i][j] != '.')
                sumRow[i]++;
        }
    }
    
    for (int j = 0; j < c; j++) {
        sumCol[j] = 0;
        for (int i = 0; i < r; i++) {
            if (grid[i][j] != '.')
                sumCol[j]++;
        }
    }

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            if (grid[i][j] != '.' && sumRow[i] == 1 && sumCol[j] == 1)
                return true;
    
    return false;
}

void getNextCell (int sx, int sy) {
    int x = sx, y = sy;
    int wx = way[x][y].first, wy = way[x][y].second;
    x += wx; y += wy;
    while (inField(x, y) && grid[x][y] == '.') {
        x += wx; y += wy;
    }
    
    if (!inField(x, y) ) {
        nextCell[sx][sy] = make_pair(-1, -1);
    } else {
        nextCell[sx][sy] = make_pair(x, y);
    }
}

void getArrows () {
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            visited[i][j] = false;
    
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            if (grid[i][j] != '.')
                way[i][j] = charToWay[grid[i][j]];
    
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            if (grid[i][j] != '.')
                getNextCell(i, j);
}

int checkField (int x, int y) {
    f[x][y] = true;
    while (true) {
        int nx = nextCell[x][y].first;
        int ny = nextCell[x][y].second;
        
        if (nx == -1)
            return 1;
        
        if (f[nx][ny] )
            return 0;
        
        x = nx; y = ny;
        f[x][y] = true;
    }
    
    throw 42;
}

void solve () {
    if (checkBadCell() ) {
        printf("IMPOSSIBLE\n");
        return ;
    }
    
    getArrows();
    
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            f[i][j] = false;
        }
    }
    
    int ans = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (!f[i][j] && grid[i][j] != '.')
                ans += checkField(i, j);
        }
    }
    printf("%d\n", ans);
}

int main () {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    
    buildPairToWay();
    
    int tests;
    scanf("%d\n", &tests);
    for (int t = 0; t < tests; t++) {
        scanf("%d%d\n", &r, &c);
        for (int i = 0; i < r; i++) {
            scanf("%s", buf);
            string s = string(buf);
            for (int j = 0; j < c; j++) {
                grid[i][j] = s[j];
            }
        }
        
        printf("Case #%d: ", t + 1);
        
        solve();
    }
    
    return 0;
}