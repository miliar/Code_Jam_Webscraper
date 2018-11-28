#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#define mp make_pair
using namespace std;

int dx[8] = {0, 1, 0, -1, 1, 1, -1, -1};
int dy[8] = {1, 0, -1, 0, 1, -1, 1, -1};

class node{
public:
    int x, y, dis;
    node(int _x, int _y, int _d) {
        x = _x;
        y = _y;
        dis = _d;
    }
    friend bool operator < (const node &a, const node &b) {
        return a.dis > b.dis;
    }
};

void solve() {
    map<int, int> M;
    int n, W, H;
    cin >> W >> H >> n;
    vector< pair< pair<int, int>, pair<int, int> > > a(n + 1);
    for (int i = 0; i < n; i++) {
        int t1, t2, t3, t4;
        cin >> t2 >> t1 >> t4 >> t3;
        t3 += 1; t4 += 1;
        M[t1] = 0;
        M[t3] = 0;
        a[i] = mp(mp(t1, t2), mp(t3, t4));
    }
    
    /*
    H = 0;
    for (map<int, int> :: iterator ii = M.begin(); ii != M.end(); ii++) {
        ii->second = H++;
    }
    
    for (int i = 0; i < n; i++) {
        a[i].first.first = M[a[i].first.first];
        a[i].second.first = M[a[i].second.first];
    }
    */
    vector< vector<int> > G(H + 1);
    vector< vector<bool> > B(H + 1);
    
    for (int i = 0; i < H; i++) {
        G[i].resize(W + 1, 1000000000);
        B[i].resize(W + 1, 1);
    }

    for (int i = 0; i < n; i++) {
        for (int x = a[i].first.first; x < a[i].second.first; x++)
            for (int y = a[i].first.second; y < a[i].second.second; y++) {
                if (x >= H)
                    cout << "Warning 1!" << endl;
                if (y >= W)
                    cout << "Warning 2!" << endl;
                B[x][y] = 0;
            }
    }
    //cout << "checked" << endl;
    
    priority_queue<node> Q;
    for (int x = 0; x < H; x++) {
        G[x][0] = B[x][0];
        Q.push(node(x, 0, G[x][0]));
    }
    while (!Q.empty()) {
        node now = Q.top();
        Q.pop();
        if (G[now.x][now.y] != now.dis) continue;
        for (int dir = 0; dir < 8; dir++) {
            node tt = now;
            tt.x += dx[dir];
            tt.y += dy[dir];
            if (tt.x < 0 || tt.y < 0 || tt.x >= H || tt.y >= W) 
                continue;
            if (G[tt.x][tt.y] > now.dis + B[tt.x][tt.y]) {
                tt.dis = G[tt.x][tt.y] = now.dis + B[tt.x][tt.y];
                Q.push(tt);
            }
        }
    }
    int ans = 1000000000;
    for (int i = 0; i < H; i++)
        ans = min(ans, G[i][W - 1]);
    cout << (ans == 1000000000 ? 0 : ans) << endl;
    //cout << "Checked" << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        solve();
    }
}