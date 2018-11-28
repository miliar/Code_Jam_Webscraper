#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 

#define equal equalll
#define less lesss
const int N = 111;
const int INF = 1e9;
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, -1, 0, 1};

int n, m;
char s[N][N];

void read() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++)
        scanf("%s", s[i]);
}

bool check(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

void solve() {
    int ans = 0;
    map < char, int > q;
    q['v'] = 0;
    q['<'] = 1;
    q['^'] = 2;
    q['>'] = 3;

    bool flagI = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (s[i][j] == '.') continue;
            vector < int > tmp(4);
            int sum = 0;
            for (int k = 0; k < 4; k++) {
                int x = i;
                int y = j;
                //db2(x, y);
                for (;;) {
                    x += dx[k]; 
                    y += dy[k];
                    //db2(x, y);
                    if (!check(x, y)) {
                        tmp[k] = 1;
                        sum++;
                        break;
                    }
                    //cerr << "sdf\n";
                    if (s[x][y] != '.') break;
                }
            }
            //db(sum);
            if (tmp[q[s[i][j]]] == 1) {
                if (sum == 4) {
                    flagI = 1;
                }
                else
                    ans++;
            }

        }
    if (flagI)
        cout << "IMPOSSIBLE\n";
    else
        cout << ans << endl;
}

void printAns() {

}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
    //freopen("test.txt", "r", stdin);
    freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            printf("Case #%d: ", tt + 1);
            read();
            solve();
            printAns();
        }
    }
    else {
        stress();
    }

    return 0;
}

