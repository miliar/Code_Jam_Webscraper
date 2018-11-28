#include <bits/stdc++.h>

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define in(x) int (x); input((x));
#define x first
#define y second
typedef int itn;

#define next next12345
#define prev prev12345
#define left lefdsf232
#define right rig43783
#define x1 x12345
#define y1 y12345

using namespace std;

template<typename T>
T gcd(T x, T y) {
    while (y > 0) {
        x %= y;
        swap(x, y);
    }
    return x;
}

template<class _T>
inline _T sqr(const _T &x) {
    return x * x;
}

template<class _T>
inline string tostr(const _T &a) {
    ostringstream os("");
    os << a;
    return os.str();
}

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
const long double PI = 3.1415926535897932384626433832795L;

template<typename T>
inline void input(T &a) {
    static int ed;
    a = 0;
    while (!isdigit(ed = getchar()) && ed != '-') { }
    char neg = 0;
    if (ed == '-') {
        neg = 1;
        ed = getchar();
    }
    while (isdigit(ed)) {
        a = 10 * a + ed - '0';
        ed = getchar();
    }
    if (neg) a = -a;
}

template<typename T = int>
inline T nxt() {
    T res;
    input(res);
    return res;
}

mt19937 generator;


int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

char t[] = {'^', 'v', '<', '>'};

struct solution {
    int test;
    int n, m;
    vector <string> s;

    int ans;

    void read() {
        n = nxt(), m = nxt();
        s.resize(n);

        for (int i = 0; i < n; ++i) {
            cin >> s[i];
        }
    }
    void print() {
        cout << "Case #" << test << ": ";
        if (ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }


    bool check(int x, int y, int dir) {
        do {
            x += dx[dir];
            y += dy[dir];
        } while (x >= 0 && x < n && y >= 0 && y < m && s[x][y] == '.');
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        } else {
            return false;
        }
    }

    void solve() {
        ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                for (int k = 0; k < 4; ++k) {
                    if (s[i][j] == t[k]) {
                        if (check(i, j, k)) {
                            continue;
                        }
                        char ok = false;
                        for (int l = 0; l < 4; ++l) {
                            ok |= check(i, j, l);
                        }
                        if (!ok) {
                            ans = -1;
                            return;
                        } else {
                            ++ans;
                        }
                    }
                }
            }
        }
    }
} * solutions;

void solve(int test) {
    solutions[test].solve();
}



int main() {
    //#define int long
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
#define fname "race"
    //freopen(fname".in", "r", stdin);
    //freopen(fname".out", "w", stdout);
#endif

    int tests = nxt();

    solutions = new solution[tests];

    for (int i = 0; i < tests; ++i) {
        solutions[i].test = i + 1;
        solutions[i].read();
    }

    thread threads[tests];

    for (int i = 0; i < tests; ++i) {
        threads[i] = thread(solve, i);
    }

    for (int i = 0; i < tests; ++i) {
        threads[i].join();
        solutions[i].print();
    }


#ifdef LOCAL
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC * 1000 << " ms." << endl;
#endif
    return 0;
} 