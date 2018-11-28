#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long ll;

int M, N , R , C;
bool ok;
const int maxn = 11;
char mp[maxn][maxn];
bool used[maxn][maxn];
const int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
const int dir2[8][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

int lei(int x, int y) {
   int sum = 0;
   for (int i = 0; i < 8  ;i ++) {
        int nx = dir2[i][0] + x;
        int ny = dir2[i][1] + y;
        if (nx < 0 || nx >= R || ny <0 || ny >= C) continue;
        if (mp[nx][ny] == '*') sum++;
   }
   return sum;
}

int cnt(int x , int y) {
    used[x][y] = true;
    int sum = 1;
    int tt = lei(x, y);
    if (tt > 0) return sum;
    for (int i = 0; i < 8 ;i ++) {
        int nx = dir2[i][0] + x;
        int ny = dir2[i][1] + y;
        if (nx < 0 || nx >= R || ny <0 || ny >= C) continue;
        if (used[nx][ny] || mp[nx][ny] == '*') continue;
        sum += cnt(nx, ny);
    }
    return sum;
}

void check() {
    int exact = R*C - M;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (mp[i][j] == '*') continue;
            memset(used, false, sizeof(used));
            if (cnt(i, j) == exact) {
                ok = true;
                mp[i][j] = 'c';
                return ;
            }
        }
    }
}

void dfs(int pos, int last) {
    // cout << pos << "  " << last << endl;
    // getchar();
    if (ok || N - pos < last) return;
    if (pos == N) {
        check();
        return ;
    }
    int x = pos / C;
    int y = pos % C;
    if (last > 0) {
        mp[x][y] = '*';
        dfs(pos + 1, last - 1);
    }
    if (ok) return;
    mp[x][y] = '.';
    dfs(pos + 1, last);
}

void solve() {
    int  n;
    cin >> R >> C >> M;
    N = R*C;
    ok = false;
    dfs(0, M);
    if (ok) {
        for (int i = 0; i < R ; i++) {
            for (int j = 0; j < C; j++) {
                cout << mp[i][j];
            }
            cout << endl;
        }
    } else {
        cout << "Impossible" << endl;
    }
}

int main() {
    // freopen("/Users/KunWang/Downloads/C-small-attempt1.in", "r" , stdin);
    // freopen( "/Users/KunWang/Downloads/small.out",  "w",stdout);
    int T , cas = 0;
    cin >> T;
    while(T--) {
         cas ++;
         cout << "Case #"<<cas <<":" << endl;
         solve();
    }
    return 0;
}
