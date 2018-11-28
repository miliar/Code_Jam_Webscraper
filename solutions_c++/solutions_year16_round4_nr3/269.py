#include <cstdio>
#include <queue>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int r, c;
int n;
int m[512];
vector<pair<int,int>> a;

int b[128][128];

void read() {
    a.clear();
    scanf("%d%d", &r, &c);
    for (int i = 0; i < (r +c); i++) {
        int x, y;
        scanf("%d%d", &x, &y);
        m[x] = y;
        m[y] = x;
        a.push_back(make_pair(x, y));
    }
    n = 2 * r + 2 * c;
}

int between(int x, int y, int z) {
    if (x > y) swap(x, y);
    if (x < z && z < y) return 1;
    return 0;
}

int dist(int x, int y) {
    if (x > y) swap(x, y);
    return min(y - x, n - (y - x));
}

int typ(int x) {
    if (x <= c) return 0;
    if (x <= r + c) return 1;
    if (x <= 2*c + r) return 2;
    return 3;
}

void getc(int q, int &x, int &y) {
    if (q <= c) {
        x = 0;
        y = q;
        return ;
    }
    if (q <= r + c) {
        x = q - c;
        y = c + 1;
        return ;
    }
    if (q <= r + 2 * c) {
        x = r + 1;
        y = c - (q - r - c) + 1;
        return ;
    }

    x = r - (q - r - 2 * c) + 1;
    y = 0;
}

int cmp(pair<int, int> x, pair<int, int> y) {
    return dist(x.first, x.second) < dist(y.first, y.second);
}

pair<int, pair<int, int>>p[128][128][4];
int dd[128][128][4];
queue<pair<int, pair<int,int>>> q;

void psh (int x, int y, int d, int cc, int pq, int py, int pd = -1) {
    if (x < 1 || y < 1 || x > r ||  y > c) return ;
    if (b[x][y] == 1) {
        if (d == 2 || d == 3) return;
    }
    if (b[x][y] == 2) {
        if (d == 0 || d == 1) return;
    }
    if (dd[x][y][d] == -1) {
        q.push(make_pair(x, make_pair(y, d)));
        dd[x][y][d] = cc;
        p[x][y][d] = make_pair(pq, make_pair(py, pd));
    }
}

void setback(int x, int y, int d) {
    while(1) {
        //printf ("set   %d %d %d\n", x, y, d);
        if (b[x][y] == 0) {
            if (d == 0 || d == 1) b[x][y] = 1;
            else b[x][y] = 2;
        }
        if (p[x][y][d].first == -1) break;
        pair<int, pair<int,int>> e = p[x][y][d];
        x = e.first;
        y = e.second.first;
        d = e.second.second;
    }
}

int bfs(int x1, int y1, int x2, int y2) {
    while (!q.empty()) q.pop();
    memset(dd, -1, sizeof dd);
    memset(p, -1, sizeof p);

    if (x1 == 0) {
        psh(x1 + 1, y1, 2, 0, -1 , -1);
        psh(x1 + 1, y1, 0, 0, -1 , -1);
    }
    if (x1 == r + 1) {
        psh(x1 - 1, y1, 1, 0, -1 , -1);
        psh(x1 - 1, y1, 3, 0, -1 , -1);
    }
    if (y1 == 0) {
        psh (x1, y1 + 1, 0, 0, -1 ,-1);
        psh (x1, y1 + 1, 3, 0, -1 ,-1);
    } 
    if (y1 == c + 1) {
        psh (x1, y1 - 1, 2, 0, -1 , -1);
        psh (x1, y1 - 1, 1, 0, -1 , -1);
    }
    int set = 0;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second.first;
        int d = q.front().second.second;
        q.pop();

        //printf ("%d %d %d\n", x, y, d);

        if (x - 1 == x2 && y == y2) {
            if (d == 0 || d == 2) {
                setback(x, y, d);
                set = 1;
                break;
            }
        }
        if (x + 1 == x2  && y == y2) { 
            if (d == 1 || d == 3) {
                setback(x, y, d);
                set = 1;
                break;
            }
        }

        if (y - 1 == y2 && x == x2) {
            if (d == 0 || d == 3) {
                setback(x, y, d);
                set = 1;
                break;
            }
        }
        if (y + 1 == y2 && x == x2) {
            if (d == 2 || d == 1) {
                setback(x, y, d);
                set = 1;
                break;
            }
        }

        int cost = dd[x][y][d] + 1;

        if (d == 0) {
            psh (x - 1, y, 3, cost, x, y, d);
            psh (x - 1, y, 1, cost, x, y, d);

            psh (x, y - 1, 1, cost, x, y, d);
            psh (x, y - 1, 2, cost, x, y, d);
        }

        if (d == 1) {
            psh (x + 1, y, 2, cost, x, y, d);
            psh (x + 1, y, 0, cost, x, y, d);

            psh (x, y + 1, 0, cost, x, y, d);
            psh (x, y + 1, 3, cost, x, y, d);
        }
        if (d == 2) {
            psh (x - 1, y, 3, cost, x, y, d);
            psh (x - 1, y, 1, cost, x, y, d);

            psh (x, y + 1, 0, cost, x, y, d);
            psh (x, y + 1, 3, cost, x, y, d);
        }

        if (d == 3) {
            psh (x + 1, y, 2, cost, x, y, d);
            psh (x + 1, y, 0, cost, x, y, d);

            psh (x, y - 1, 1, cost, x, y, d);
            psh (x, y - 1, 2, cost, x, y, d);
        }

    }
    return set;
}

void solve() {
    for (int i = 0; i < (int)a.size(); i++) {
        for (int j = i + 1; j < (int)a.size();j ++) {
            if (between(a[i].first, a[i].second, a[j].first) ^ between(a[i].first, a[i].second, a[j].second)) {
                printf ("IMPOSSIBLE\n");
                return;
            }
        }
    }
    sort(a.begin(), a.end(), cmp);
    memset(b, 0, sizeof b);
    for (int i = 0; i < (int)a.size(); i++) {
        int q = a[i].first;
        int w = a[i].second;

        int x1, y1, x2, y2;
        getc(q, x1, y1);
        getc(w, x2, y2);

        //printf (" conn (%d - %d)   (%d, %d)   (%d, %d)\n", q, w, x1, y1, x2, y2);

        if (!bfs(x1, y1, x2, y2)) {
            printf ("IMPOSSIBLE\n");
            return ;
        }
        //break;
    }

    for (int i = 1; i <= r; i++) {
        for (int j = 1; j <= c; j++) {
            //printf ("%d", b[i][j]);
            printf ("%c", (b[i][j] == 1) ? '/' : '\\');
        }
        printf ("\n");
    }
}

int main() {
    int cases;

    scanf("%d", &cases);
    for (int i=1; i<=cases; i++) {
        read();
        printf("Case #%d:\n", i);
        solve();
    }
    return 0;
}

