#include <iostream>
#include <utility>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <numeric>
#include <list>
#include <stack>
#include <cmath>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>

#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef  long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VII;
typedef priority_queue<int> PQI;
const int Mod = 1e9 + 7;
inline LL FIX(LL a) {return (a % Mod + Mod) % Mod;}
#define MP(x,y) make_pair(x,y)
#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define take(x,y) (((x)>>(y)) & 1ll)
#define mv(n) (1<<(n))
#define what_is(x) cerr << #x << " is " << x << endl;
#define eb emplace_back
#define pb push_back
#define UNQ(x) (sort(begin(x),end(x)),x.erase(unique(begin(x),end(x)),end(x)))

int R,C;
string Maze[128];

int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
map<char,int>map_d;
int check(int x,int y) {
    int cur_d = map_d[Maze[x][y]];
    if(cur_d != -1) {
        int f = 0;
        for(int i = 0;i < 4;i++) {
            int xx = x + dir[i][0];
            int yy = y + dir[i][1];
            while(xx >= 0 && xx < R && yy >= 0 && yy < C) {
                if(map_d[Maze[xx][yy]] != -1) {
                    f = 1;
                    break;
                }
                int tmp_x = xx + dir[i][0];
                int tmp_y = yy + dir[i][1];
                xx = tmp_x;
                yy = tmp_y;
            }
            if(f == 1) break;
        }
        if(f == 0) return -1;
        int xx = x + dir[cur_d][0],yy = y + dir[cur_d][1];
        while(xx >= 0 && xx < R && yy >= 0 && yy < C) {
            if(map_d[Maze[xx][yy]] != -1) return 0;
            int tmp_x = xx + dir[cur_d][0];
            int tmp_y = yy + dir[cur_d][1];
            xx = tmp_x;
            yy = tmp_y;
        }
        return 1;
    }
    return 0;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    map_d['v'] = 0;
    map_d['^'] = 1;
    map_d['>'] = 2;
    map_d['<'] = 3;
    map_d['.'] = -1;
    int t,cas = 0;
    scanf("%d",&t);
    while(t--) {
        scanf("%d %d",&R,&C);
        for(int i = 0;i < R;i++)
            cin>>Maze[i];
        int Min = 0,imposs = 0;
        for(int i = 0;i < R;i++) {
            for(int j = 0;j < C;j++) {
                    int ret = check(i,j);
                    if(ret == -1) {
                        imposs = 1;
                        break;
                    }
                    Min += ret;
            }
            if(imposs == 1) break;
        }
        if(imposs)
            printf("Case #%d: IMPOSSIBLE\n",++cas);
        else
            printf("Case #%d: %d\n",++cas,Min);
    }
    return 0;
}