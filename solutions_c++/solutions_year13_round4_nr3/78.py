#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cassert>

const char* input_file = "C-large.in";
//const char* input_file = "input.txt";

using namespace std;

const int maxn = 2048;

int a[maxn];
int b[maxn];
int n;

bool g[maxn][maxn];
bool v[maxn];

struct SmallList {
    int size;
    int id[maxn];
};

SmallList sl[maxn];

void dfs(int id) {
    v[id] = true;
    bool vec[maxn];
    memset(vec, 0, sizeof(vec));
    for (int i = 0; i < n; ++i) {
        if (g[id][i]) {
            if (!v[i]) dfs(i);
            for (int j = 0; j < sl[i].size; ++j)
                vec[sl[i].id[j]] = true;
            vec[i] = true;
        }
    }
    sl[id].size = 0;
    for (int i = 0; i < n; ++i)
        if (vec[i])
            sl[id].id[sl[id].size++] = i;
}


void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];
    memset(g, 0, sizeof(g));



    for (int i = 0; i < n; ++i) {
        bool find = false;
        for (int j = i - 1; j >= 0; --j) {
            if (!find && a[j] == a[i] - 1) {
                find = true;
                g[i][j] = true;
            }
            if (a[j] >= a[i]) {
                g[j][i] = true;
            }
        }

        bool findb = false;
        for (int j = i + 1; j < n; ++j) {
            if (!findb && b[j] == b[i] - 1) {
                findb = true;
                g[i][j] = true;
            }
            if (b[j] >= b[i]) {
                g[j][i] = true;
            }
        }
    }

   /* printf("\n graph \n");
    for  (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cout <<" " << g[i][j];
        cout << endl;
    }*/

    memset(v, 0, sizeof(v));

    for (int i = 0; i < n; ++i) {
        if (!v[i]) dfs(i);
        for (int j = 0; j < sl[i].size; ++j)
            assert(sl[i].id[j] != i);
    }

    bool used[maxn];
    int result[maxn];
    memset(used, 0, sizeof(used));
    for (int i = 0; i < n; ++i) {
        int leave = 0;
        for (int j = 0; j < sl[i].size; ++j)
            if (sl[i].id[j] > i) leave ++;
        int get = -1;
        for (int j = 0; j < n; ++j) {
            if (!used[j]) {
                if (leave == 0) {
                    get = j;
                    break;
                } else {
                    leave -= 1;
                }
            }
        }
        assert(get != -1);
        result[i] = get + 1;
        used[get] = true;
    }
    for (int i = 0; i < n; ++i)
        cout << " " << result[i];
}

int main() {
    freopen(input_file, "r", stdin);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ":";
        solve();
        cout << endl;
    }
    return 0;
}

