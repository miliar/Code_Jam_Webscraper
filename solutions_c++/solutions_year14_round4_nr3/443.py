#include <cstdio>
#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

bool map[100][500];
bool visited[100][500];

int solve(){
    fill_n(&map[0][0], 100 * 500, true);
    fill_n(&visited[0][0], 100 * 500, false);
    int w, h, b;
    scanf("%d %d %d", &w, &h, &b);
    for(int i = 0; i < b; i++){
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        for(int j = x1; j <= x2; j++)
            fill(map[j] + y1, map[j] + y2 + 1, false);
    }
//puts("a");
    deque<pair<pair<int, int>, int>> dq;
    for(int i = 0; i < h; i++){
        if(map[0][i]) dq.push_back({{0, i}, 1}); else dq.push_front({{0, i}, 0});
        visited[0][i] = true;
    }

    while(!dq.empty()){
        auto p = dq.front(); dq.pop_front();
#define X first.first
#define Y first.second
#define T second

#define FF(X, Y)        if((X) >= 0 && (X) < w && (Y) >= 0 && (Y) < h && !visited[(X)][(Y)]) {\
            if(map[(X)][(Y)]) dq.push_back({{(X),(Y)}, p.T+1}); else dq.push_front({{(X), (Y)}, p.T});\
            visited[(X)][(Y)] = true;\
        }
        if(p.X == w - 1)
            return p.T;
        FF(p.X+1, p.Y);
        FF(p.X+1, p.Y+1);
        FF(p.X, p.Y+1);
        FF(p.X-1, p.Y);
        FF(p.X-1, p.Y-1);
        FF(p.X, p.Y-1);
        FF(p.X-1, p.Y+1);
        FF(p.X+1, p.Y-1);
    }
}

int main(){
    int t;
    scanf("%d", &t);
//    auto& out = cout;
    ofstream out("C.out");
    for(int i = 1; i <= t; i++){
        out << "Case #" << i << ": " << solve() << "\n";
    }
}
