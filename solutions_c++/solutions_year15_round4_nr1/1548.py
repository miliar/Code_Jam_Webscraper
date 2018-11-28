#include <vector>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;

int T, R, C;
string arrow = ">v<^";
int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
char grid[105][105];

int index_of(char c){
    for(int i=0; i<4; i++) if(arrow[i] == c) return i;
    return 1/0;
}

bool good(int x, int y){
    if(x < 0 || y < 0) return false;
    if(x >= R || y >= C) return false;
    return true;
}

bool points(int x, int y, int d){
    for(int dist = 1; ; dist++){
        int xx = x + dist * dir[d][0];
        int yy = y + dist * dir[d][1];
        if(!good(xx, yy)) break;
        if(grid[xx][yy] != '.') return true;
    }
    return false;
}

bool can_point(int x, int y){
    for(int d=0; d<4; d++)
        if(points(x, y, d))
            return true;
    return false;
}

int main(){
    cin >> T;
    for(int tt=1; tt<=T; tt++){
        cin >> R >> C;

        for(int r=0; r<R; r++)
            for(int c=0; c<C; c++)
                cin >> grid[r][c];

        bool can = true;
        int ans = 0;

        for(int r=0; r<R; r++)
            for(int c=0; c<C; c++){
                if(grid[r][c] == '.') continue;
                if(points(r, c, index_of(grid[r][c]))) continue;
                if(can_point(r, c)) ans++;
                else can = false;
            }

        cout << "Case #" << tt << ": ";
        if(can) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }

}
