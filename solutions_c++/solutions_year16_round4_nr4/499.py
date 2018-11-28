#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
using namespace std;

typedef long long LL;
#define CLR(a,b) memset(a,b,sizeof(a))
const int N = (1<<16)+5;
bool ok[5][N];
int a,b,c,d;
int used[4];
int order[4];
int mat[4][4];

bool dfs(int p, int n) {
    if (p == n) return true;
    int man = order[p];
    bool found = false;
    for (int op = 0; op < n; ++op) {
        if (mat[man][op] && !used[op]) {
            found = true;
            used[op] = true;
            if (!dfs(p + 1, n)) {
                return false;
            }
            used[op] = false;
        }
    }
    return found;
}
void pre() {
    CLR(ok, 0);
    for (int i = 1; i <= 4; ++i) {
        for(int j = 0; j < (1<<(i*i)); ++j) {
            for (int ii = 0; ii < i; ++ii) {
                for (int jj = 0; jj < i; ++jj) {
                    mat[ii][jj] = ((j>>(ii * i + jj)) & 1);
                }
            }
            ok[i][j] = true;
            for (int k = 0; k < i; ++k) {
                order[k] = k;
            }
            do {
                CLR(used, 0);
                if (!dfs(0, i)) {
                    ok[i][j] = false;
                    break;
                }
            }while (next_permutation(order, order + i));
        }
    }
}
int n;
int state;
char buff[100];
void solve() {
    /*
    for (int i = 0; i < (1<<4); ++i) {
        cout << i << " " << ok[2][i] << endl;
    }
     */
    int ans = 16;
    for (int i = 0; i < (1<<(n*n)); ++i) {
        if ((i & state) != state) continue;
        //cout << i << endl;
        if (ok[n][i]) {
            int cnt = 0;
            //cout << i << " " << state << endl;
            int diff = (i ^ state);
            //cout << diff << endl;
            for (int k = 0; k < n * n; ++k) {
                if (1 & (diff >> k)) cnt ++;
            }
            ans = min(ans, cnt);
        }
    }
    printf("%d\n", ans);
}
int main()
{
    pre();
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++cas);
        scanf("%d", &n);
        state = 0;
        for (int i =0; i < n; ++i) {
            scanf("%s", buff);
            for (int j = 0; j < n; ++j) {
                mat[i][j] = buff[j]-'0';
                state |= mat[i][j] * (1 << (i * n + j));
            }
        }
        //cout << state << endl;
        solve();
    }
    return 0;
}