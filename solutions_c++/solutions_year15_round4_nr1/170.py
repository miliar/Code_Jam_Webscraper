#define TASKNAME "text"

#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define sz(a) (int)a.size()
#define fst first
#define snd second
#define y1 osrughosduvgarligybakrybrogvba
#define y0 aosfigdalrowgyalsouvgrlvygalri                               
#define mp make_pair
#define pb push_back
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <bool> vb;
typedef vector <ll> vll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <int, ll> pil;
typedef vector <pii> vpii;

template <typename T>
T sqr(T x) {
    return x * x;
}

template <typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

const double EPS = 1e-9;
const int INF = 1e9;
const ll INFLONG = (ll)1e18;

const int maxn = 200;

char s[maxn][maxn];
char dir[] = {'>', '<', '^', 'v'};
int dx[] = {0, 0, -1, 1};
int dy[] = {1, -1, 0, 0};

int main()
{
    freopen(TASKNAME".in", "r", stdin);
    freopen(TASKNAME".out", "w", stdout);
    int testsCount;
    scanf("%d", &testsCount);
    for (int testNumber = 1; testNumber <= testsCount; ++testNumber) {
        printf("Case #%d: ", testNumber);
        int n, m;
        scanf("%d%d", &n, &m);
        vvi arrows(n);
        vvi arrows0(m);
        for (int i = 0; i < n; i++) {
            scanf("%s", s[i]);
            for (int j = 0; j < m; j++) {
                if (s[i][j] != '.') {
                    arrows[i].pb(j);
                    arrows0[j].pb(i);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            sort(all(arrows[i]));
        }
        for (int i = 0; i < m; i++) {
            sort(all(arrows0[i]));
        }
        int ans = 0;
        bool fail = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (s[i][j] == '.') continue;
                int it = find(dir, dir + 4, s[i][j]) - dir;
                int DX = dx[it];
                int DY = dy[it];
                bool ok = false;
                for (int x = i + DX, y = j + DY; x >= 0 && x < n && y >= 0 && y < m; x += DX, y += DY) {
                    if (s[x][y] != '.') {
                        ok = true;
                    }
                }
                if (!ok) {
                    if (arrows[i].size() > 1 || arrows0[j].size() > 1) {
                        ++ans;
                    } else {
                        fail = true;
                    }
                }
            }
        }
        if (fail) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }                       
    return 0;
}