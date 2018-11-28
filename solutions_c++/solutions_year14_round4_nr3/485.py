#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
using namespace std;

struct rec {
    int x0, y0, x1, y1;
};

struct dir_node {
    int x, y, d;
    dir_node(int &x_, int &y_, int &d_) {
        x = x_;
        y = y_;
        d = d_;
    }
};

const int maxh = 2000 + 10;
const int maxw = 1000 + 10;
const int maxn = 1000 + 10;
int w, h, n, hh;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
bool mark[maxh][maxw];
bool dir_mark[maxh][maxw][4];
rec a[maxn];
vector<int> ly;
int ty[maxn * 3];
vector<dir_node> seq;
int ans;

inline bool is_rock(int &tx, int &ty) {
    return (tx < 0 || ty < 0 || tx >= w || ty >= h || mark[ty][tx]);
}

void solve() {   
    memset(mark, 0, sizeof(mark));
    for (int i = 0; i < n; i++) {        
        for (int y = a[i].y0; y <= a[i].y1; y++)
            for (int x = a[i].x0; x <= a[i].x1; x++)
                mark[y][x] = true;
    }
    
    ans = 0;
    
    for (int i = 0; i < w; i++) {
        if (mark[0][i]) continue;
        int cy = 0, cx = i;
        int cd = 0;
        seq.clear();
               
        while (true) {            
            seq.push_back(dir_node(cx, cy, cd));
            dir_mark[cy][cx][cd] = true;
            bool flag = false;
                                
            for (int j = 0; j < 4; j++) {
                int td = (cd + 3 + j) % 4;
                int tx = cx + dx[td];
                int ty = cy + dy[td];
                if (tx < 0 || ty < 0 || tx >= w || ty >= h || mark[ty][tx]) continue;
                flag = true;
                cx = tx; cy = ty;
                //mark[cy][cx] = true;
                cd = td;
                break;
            }
            if (!flag) break;
            if (dir_mark[cy][cx][cd]) break;
            if (cy == h - 1) {
                ans++;
                break;
            }
        }
        for (int j = 0; j < seq.size(); j++) {
            cx = seq[j].x;
            cy = seq[j].y;
            cd = seq[j].d;
            dir_mark[cy][cx][cd] = false;
            mark[cy][cx] = true;
        }
    }
    
}

int main() {    
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d %d", &w, &h, &n);        
        ly.clear();        
        ly.push_back(0);
        ly.push_back(h);
        for (int i = 0; i < n; i++) {
            scanf("%d %d %d %d", &a[i].x0, &a[i].y0, &a[i].x1, &a[i].y1);            
            ly.push_back(a[i].y0);
            ly.push_back(a[i].y1 + 1);
        }
        
        solve();
        printf("Case #%d: %d", t, ans);
        
        printf("\n");
    }
}

