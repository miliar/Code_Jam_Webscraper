#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int T, R, C;

int color[1000];
vector<int> e[1000];

int getidx(int x) {
    if (x <= C) return x - 1;
    if (x <= R+C) return (R+1)*C + (C+1) * (x-C) - 1;
    if (x <= R + C*2) return (R + 1) * C - (x - R - C);
    return (R+1)*C + ((R+C)*2 - x)*(C+1);
}

void link(int x, int y) {
    e[x].push_back(y);
    e[y].push_back(x);
}

void buildgraph(int w) {
    for (int i = 0; i < (R+1)*C + R*(C+1); ++ i)
        e[i].clear();
    for (int i = 0; i < R*C; ++ i) {
        int x = i / C;
        int y = i % C;
        if ((1 << i) & w) {
            link(x * C + y, (R+1) * C + x * (C+1) + y);
            link((x + 1) * C + y, (R+1)*C + x * (C+1) + y + 1);
        }
        else {
            link(x * C + y, (R+1)*C + x * (C+1) + y + 1);
            link((x + 1) * C + y, (R+1) * C + x * (C+1) + y);
        }
    }
}

vector<int> sc;
bool vis[1000];

bool find(int sc) {
    memset(vis, 0, sizeof(vis));
    queue<int> que;
    que.push(sc);
    vis[sc] = true;
    bool flag1=false, flag2=false;
    while (!que.empty()) {
        int x = que.front();
        que.pop();
        for (int i = 0; i < e[x].size(); i ++ )
            if (!vis[e[x][i]]) {
                vis[e[x][i]] = true;
                if (color[e[x][i]] == color[sc]) flag1 = true;
                if (color[e[x][i]] != 0 &&
                    color[e[x][i]] != color[sc]) flag2 = true;
                que.push(e[x][i]);
            }
    }
//    cout<<flag1<<" "<<flag2<<endl;
    return !flag2 && flag1;
}

bool getans() {
   for (int i = 0; i < sc.size(); ++ i) {
        if (!find(sc[i])) return false;
   } 
   return true;
}

void out(int w) {
    for (int i = 0; i < R*C; ++ i) {
        if ((1 << i) & w) cout<<'/';
        else cout<<'\\';
        if ((i + 1) % C == 0) cout<<endl;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>T;
    for (int ca = 1; ca <= T; ++ ca) {
        cin>>R>>C;
        sc.clear();
        memset(color, 0, sizeof(color));
        for (int i = 0; i < (R + C); ++ i) {
            int a, b;
            cin>>a>>b;
            a = getidx(a);
            b = getidx(b);
            sc.push_back(a);
            color[a] = i + 1;
            color[b] = i + 1;
        }
        cout<<"Case #"<<ca<<":" <<endl;
        bool flag = false;
        for (int i = 0; i < 1<<(R*C); ++ i) {
            buildgraph(i);
            if (getans()) {
                out(i);
                flag = true;
                break;
            }
        }
        if (!flag) cout<<"IMPOSSIBLE"<<endl; 
    }
    return 0;
}
