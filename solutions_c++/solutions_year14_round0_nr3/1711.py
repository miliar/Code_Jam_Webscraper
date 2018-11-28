#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <cassert>
#if __cplusplus > 201103L
#include <initializer_list>
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#ifdef LOCAL
#define DEBUG
#endif

#define oo 0x3F3F3F3F
#define fst first
#define snd second
#define PB push_back
#define SZ(x) (int)((x).size())
#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for (int _end_ = (b), i = (a); i <= _end_; ++i)
#define ROF(i, a, b) for (int _end_ = (b), i = (a); i >= _end_; --i)

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

int64 fpm(int64 b, int64 e, int64 m) { int64 t = 1; for (; e; e >>= 1, b = b * b % m) e & 1 ? t = t * b % m : 0; return t; }
template<class T> inline bool chkmin(T &a, T b) {return a > b ? a = b, true : false;}
template<class T> inline bool chkmax(T &a, T b) {return a < b ? a = b, true : false;}
template<class T> inline T sqr(T x) {return x * x;}
template <typename T> T gcd(T x, T y) {for (T t; x; ) t = x, x = y % x, y = t; return y; }

template<class edge> struct Graph {
    vector<vector<edge> > adj;
    Graph(int n) {adj.clear(); adj.resize(n + 5);}
    Graph() {adj.clear(); }
    void resize(int n) {adj.resize(n + 5); }
    void add(int s, edge e){adj[s].push_back(e);}
    void del(int s, edge e) {adj[s].erase(find(iter(adj[s]), e)); }
    vector<edge>& operator [](int t) {return adj[t];}
};

int n, m, k;
char ans[55][55], txt[20][20];
int ufs[30], t[7][7];
pair<int, int> f[10][10][200];

int find(int x) {
    return ufs[x] ? ufs[x] = find(ufs[x]) : x;
}

void update() {
    int w = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j)
            if (txt[i][j] == '.') {
                t[i][j] = 0;
                for (int x = i - 1; x <= i + 1; ++x)
                    for (int y = j - 1; y <= j + 1; ++y)
                        if (1 <= x && x <= n && 1 <= y && y <= m)
                            t[i][j] += txt[x][y] == '*';
                w += t[i][j] == 0;
            } else
                t[i][j] = -1;
    }

    memset(ufs, 0, sizeof(ufs));
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) {
            if (t[i][j] == 0) {
                for (int x = i - 1; x <= i + 1; ++x)
                    for (int y = j - 1; y <= j + 1; ++y)
                        if (1 <= x && x <= n && 1 <= y && y <= m && t[x][y] == 0) {
                            int va = i * m + j - m, vb = x * m + y - m;
                            if (find(va) != find(vb))
                                ufs[find(va)] = find(vb), --w;
                        }
            }
        }
    if (w > 1) return ;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) {
            if (t[i][j] > 0) {
                int k = 0;
                for (int x = i - 1; x <= i + 1; ++x)
                    for (int y = j - 1; y <= j + 1; ++y)
                        if (1 <= x && x <= n && 1 <= y && y <= m) {
                            k += t[x][y] == 0;
                        }
                if (k == 0) return ;
            }
        }

    int s = 0, k = 0, c;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) {
            s |= (txt[i][j] == '*') << (i * m + j - m);
            k += txt[i][j] == '*';
            if (t[i][j] == 0) c = i * m + j - m;
        }
    f[n][m][k] = make_pair(s, c);
}

void search(int x, int y) {
    if (y > m) return search(x + 1, 1);
    if (x > n) {
        update();
        return ;
    }
    txt[x][y] = '.', search(x, y + 1);
    txt[x][y] = '*', search(x, y + 1);
}

int main(int argc, char **argv) {
#ifdef LOCAL
    freopen("C-small-attempt2.in" , "r", stdin);
    freopen("C.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);

    for (n = 1; n <= 5; ++n)
        for (m = 1; m <= 5; ++m) {
            cerr << "searching: " << n << " " << m << endl;
            search(1, 1);
            // for (int i = 1; i <= n * m; ++i) {
            //     cout << n << " " << m << " " << i << " " << f[n][m][i].fst << " " << f[n][m][i].snd << endl;
            // }
        }
    
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        cout << "Case #" << tc << ": " << endl;
        
        int R, C, M;
        cin >> R >> C >> M;
        
        if (M == R * C - 1) {
            for (int i = 1; i <= R; ++i) {
                for (int j = 1; j <= C; ++j) {
                    cout << (i == 1 && j == 1 ? 'c' : '*');
                }
                cout << endl;
            }
        } else if (f[R][C][M].snd) {
            int c = f[R][C][M].snd, s = f[R][C][M].fst;
            for (int i = 1; i <= R; ++i) {
                for (int j = 1; j <= C; ++j) {
                    char ch = s >> (i * C - C + j) & 1 ? '*' : '.';
                    if (i * C - C + j == c) ch = 'c';
                    cout << ch;
                }
                cout << endl;
            }
        } else {
            cout << "Impossible" << endl;
        }
        
        // if (M == R * C - 1) {
        //     for (int i = 1; i <= R; ++i) {
        //         for (int j = 1; j <= C; ++j) {
        //             cout << (i == 1 && j == 1 ? 'c' : '*');
        //         }
        //         cout << endl;
        //     }
        // } else {
        //     memset(ans, '*', sizeof(ans));
        //     int t = R * C - M;
        //     for (int i = 1; i <= R || i <= C; ++i) {
        //         for (int j = 1; j < i && t && j <= C && i <= R; ++j) {
        //             ans[i][j] = '.';
        //             --t;
        //         }
        //         for (int j = 1; j <= i && t && j <= R; ++j) {
        //             ans[j][i] = '.';
        //             --t;
        //         }
        //     }

        //     if ((R > 1 && ans[2][1] == '*') || (C > 1 && ans[1][2] == '*') || (R > 1 && C > 1 && ans[2][2] == '*')) {
                
        //     } else  {
        //         ans[1][1] = 'c';
        //         for (int i = 1; i <= R; ++i) {
        //             ans[i][C + 1] = '\0';
        //             cout << (ans[i] + 1) << endl;
        //         }
        //     }
            
        // }
    }


    return 0; 
}



