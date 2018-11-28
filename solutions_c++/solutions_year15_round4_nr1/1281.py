#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define fs first
#define sc second
#define mp make_pair
#define eb emplace_back

#define next _next
#define prev _prev
#define hash _hash
#define rank _rank
#define left _left
#define right _right
#define all(s) s.begin(), s.end()

#ifdef DEBUG
#define dout(x) cerr << x
#else
#define dout(x)
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ll lINF = 1e18;
const double EPS = 1e-12;

#define PROBLEM "A"

template <class T>
void mout(T b, T e) {
#ifdef DEBUG
    for (T i = b; i != e; i++) {
        cout << *i << ' ';
    }
    cout << endl;
#endif
}

const int N = 200;

char g[N][N];
int left[N], right[N], up[N], down[N];

int main()
{
#ifdef DEBUG
	assert(freopen(PROBLEM".in", "r", stdin) != NULL);
	assert(freopen(PROBLEM".out", "w", stdout));
#else
//	assert(freopen(PROBLEM".in", "r", stdin) != NULL);
//	assert(freopen(PROBLEM".out", "w", stdout));
#endif

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        int r, c;
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                scanf(" %c", &g[i][j]);
            }
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j){
                if (g[i][j] != '.') {
                    left[i] = j;
                    break;
                }
            }
            for (int j = c - 1; j >= 0; --j) {
                if (g[i][j] != '.') {
                    right[i] = j;
                    break;
                }
            }
        }
        for (int j = 0; j < c; ++j) {
            for (int i = 0; i < r; ++i){
                if (g[i][j] != '.') {
                    up[j] = i;
                    break;
                }
            }
            for (int i = r - 1; i >= 0; --i) {
                if (g[i][j] != '.') {
                    down[j] = i;
                    break;
                }
            }
        }
        bool h = 1;
        int ans = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (g[i][j] == '.') continue;
                if (left[i] == j && right[i] == j && up[j] == i && down[j] == i) {
                    h = 0;
                    break;
                }
                if (g[i][j] == '<' && left[i] == j) ++ans;
                if (g[i][j] == '>' && right[i] == j) ++ans;
                if (g[i][j] == '^' && up[j] == i) ++ans;
                if (g[i][j] == 'v' && down[j] == i) ++ans;
            }
            if (h == 0) {
                break;
            }
        }
        printf("Case #%d: ", tt);
        if (h == 0) {
            printf("IMPOSSIBLE\n");
        }
        else {
            printf("%d\n", ans);
        }
    }
	return 0;
}


