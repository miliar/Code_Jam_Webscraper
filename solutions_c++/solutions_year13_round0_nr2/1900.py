#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "vector"
#include "queue"
#include "stack"
#include "cmath"
#include "string"
#include "cctype"
#include "map"
#include "iomanip"
#include "set"
#include "utility"
using namespace std;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
const int inf = 1 << 29;
const double dinf = 1e30;
const ll linf = 1LL << 55;

const int N = 111;
int a[N][N];
int row[N], col[N];
int n, m;
bool solve() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] < row[i] && a[i][j] < col[j]) return false;
        }
    }
    return true;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> m;
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> a[i][j];
                row[i] = max(row[i], a[i][j]);
                col[j] = max(col[j], a[i][j]);
            }
        }
        printf("Case #%d: ", Case++);
        puts(solve() ? "YES" : "NO");
    }
    return 0;
}
