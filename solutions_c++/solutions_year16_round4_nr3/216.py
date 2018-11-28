#include <iostream>
#include <vector>

using namespace std;

char t[20][20];
int r,c;
int n;

int p[20][20][2];
vector<int> u;

void haku(int y, int x, int q) {
    if (p[y][x][q] == 1) return;
    p[y][x][q] = 1;
    if (y == 0 && q == 0) u.push_back(x+1);
    if (y == r-1 && q == 1) u.push_back(c+r+c-x);
    if (x == c-1 && q == 0 && t[y][x] == '\\') u.push_back(c+y+1);
    if (x == c-1 && q == 1 && t[y][x] == '/') u.push_back(c+y+1);
    if (x == 0 && q == 0 && t[y][x] == '/') u.push_back(c+r+c+r-y);
    if (x == 0 && q == 1 && t[y][x] == '\\') u.push_back(c+r+c+r-y);
    if (t[y][x] == '/' && q == 0) {
        if (y-1 >= 0) haku(y-1,x,1);
        if (x-1 >= 0) haku(y,x-1,t[y][x-1] == '/');
    }
    if (t[y][x] == '/' && q == 1) {
        if (y+1 < r) haku(y+1,x,0);
        if (x+1 < c) haku(y,x+1,t[y][x+1] == '\\');
    }
    if (t[y][x] == '\\' && q == 0) {
        if (y-1 >= 0) haku(y-1,x,1);
        if (x+1 < c) haku(y,x+1,t[y][x+1] == '\\');
    }
    if (t[y][x] == '\\' && q == 1) {
        if (y+1 < r) haku(y+1,x,0);
        if (x-1 >= 0) haku(y,x-1,t[y][x-1] == '/');
    }
}

int oo[100][100];

void solve(int x) {
    cin >> r >> c;
    n = r*c;
    vector<int> v;
    v.resize(2*(r+c));
    cout << "Case #" << x << ":\n";
    for (int i = 0; i < 2*(r+c); i++) cin >> v[i];
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            oo[i][j] = 0;
        }
    }
    for (int i = 0; i < 2*(r+c); i += 2) {
        oo[v[i]][v[i+1]] = 1;
        oo[v[i+1]][v[i]] = 1;
    }
    for (int i = 0; i < (1<<n); i++) {
        int w = 0;
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                if (i&(1<<w)) t[y][x] = '/';
                else t[y][x] = '\\';
                w++;
            }
        }
        int m = 0;
        int y = 0, x = 0;
        bool ok = true;
        for (int i = 0; i < 2*(r+c); i++) {
            u.clear();
            for (int y = 0; y < r; y++) {
                for (int x = 0; x < c; x++) {
                    p[y][x][0] = 0;
                    p[y][x][1] = 0;
                }
            }
            if (m == 0) haku(y,x,0);
            if (m == 1 && t[y][x] == '\\') haku(y,x,0);
            if (m == 1 && t[y][x] == '/') haku(y,x,1);
            if (m == 2) haku(y,x,1);
            if (m == 3 && t[y][x] == '\\') haku(y,x,1);
            if (m == 3 && t[y][x] == '/') haku(y,x,0);
            /*cout << y << " " << x << " " << m << " " << u.size() << "\n";
            for (int i = 0; i < u.size(); i++) {
                cout << u[i] << " ";
            }
            cout << "\n";*/
            if (u.size() == 2 && oo[u[0]][u[1]]) {
                ;
            } else {
                ok = false;
            }
            if (m == 0) x++;
            if (m == 1) y++;
            if (m == 2) x--;
            if (m == 3) y--;
            if (m == 0 && x == c) {x--; m = 1;}
            if (m == 1 && y == r) {y--; m = 2;}
            if (m == 2 && x == -1) {x++; m = 3;}
        }
        if (ok) {
            for (int y = 0; y < r; y++) {
                for (int x = 0; x < c; x++) {
                    cout << t[y][x];
                }
                cout << "\n";
            }
            return;
        }
    }
    cout << "IMPOSSIBLE\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
