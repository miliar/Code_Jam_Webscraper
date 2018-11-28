#include <vector>
#include<cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
#include <list>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef pair<string, int> PSI;
typedef pair<string, string> PSS;
typedef pair<PII, int> PIP;
void init() {}

bool dfs(int x, vector<int>& vst, vector<int>& mask, vector<vector<int>>& gg) {
    if (vst[x]) return true;
    mask[x] = 1;
    vst[x] = 1;
    for(auto y : gg[x]) {
        if (dfs(y, vst, mask, gg)) return true;
    }
    return false;
}
void solve(int ncase) {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for(int i = 0; i < n; i ++) {
        cin >> g[i];
    }
    vector<vector<int>> gg(n * m + 1);
    int ret = 0;
    vector<PII> need;
    for(int i = 0; i < n; i ++) {
        for(int j = 0; j < m; j ++) {
            if (g[i][j] != '.') {
                int x = 0, y = 0;
                if (g[i][j] == '>') x = 0, y = 1;
                if (g[i][j] == 'v') x = 1, y = 0;
                if (g[i][j] == '<') x = 0, y = -1;
                if (g[i][j] == '^') x = -1, y = 0;
                //cout << i <<" " << j << endl;
                for(int k = 1;; k ++) {
                    int x1 = k * x + i, y1 = k * y + j;
                    if (x1 < 0 || x1 >= n || y1 < 0 || y1 >= m) {
                        need.push_back(PII(i, j));
                        break;
                    }
                    if (g[x1][y1] != '.') {
                        //gg[i * m + j].push_back(x1 * m + y1);
                        //cout << " gg " << x1 << " " << y1 << endl;
                        break;
                    }
                }
            }
        }
    }
    cout << "Case #" << ncase << ": ";
    for(int i = 0; i < need.size(); i ++) {
        int x = need[i].first;
        int y = need[i].second;
        bool tmp = false;
        for(int j = 0; tmp == false && j < n; j ++) {
            if (j != x && g[j][y] != '.') {
                tmp = true;
                break;
            }
        }
        for(int j = 0; tmp == false && j < m; j ++) {
            if (j != y && g[x][j] != '.') {
                tmp = true;
                break;
            }
        }
        if (tmp == false) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << need.size() << endl;
}
int main() {
    //ios::sync_with_stdio(false);
    //cout << std::fixed << setprecision(16);
    init();
#ifdef _zzz_
    //freopen("in.txt", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T = 1;
    cin >> T;
    //scanf("%d", &T);
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
