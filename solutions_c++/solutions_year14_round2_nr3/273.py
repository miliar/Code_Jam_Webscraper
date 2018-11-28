#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <cstring>
#include <stack>
using namespace std;

#define N 102

int n, m;
map<int, int> zip;
int code[N], id[N];
char buffer[N * 50];
bool way[N][N];

void init() {
    zip.clear();
    memset(way, 0, sizeof(way));
}

void read() {
    for (int i = 0; i < n; i++) {
        scanf("%d", &code[i]);
        zip[code[i]] = i;
    }
    int u , v;
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &u, &v);
        u--, v--;
        way[u][v] = true;
        way[v][u] = true;
    }
}

bool judge() {
    int stk[N], top = 0;
    int u, v;
    for (int i = 0; i < n; i++) {
        if (top == 0)
            stk[top++] = id[i];
        else {
            while (top && !way[stk[top - 1]][id[i]])
                top--;
            if (top == 0)
                return false;
            stk[top++] = id[i];
        }
    }
    return true;
}

void solve() {
    sort(code, code + n);
    do {
        for (int i = 0; i < n; i++)
            id[i] = zip[code[i]];
        if (judge()) {
            for (int i = 0; i < n; i++)
                sprintf(buffer + i * 5, "%d", code[i]);
            buffer[5 * n] = '\0';
            break;
        }
    } while (next_permutation(code, code + n));
}

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%d%d", &n, &m);
        init();
        read();
        solve();
        printf("Case #%d: %s\n", i, buffer);
    }
    return 0;
}
