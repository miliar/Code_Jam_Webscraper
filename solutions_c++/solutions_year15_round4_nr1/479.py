#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()

#ifdef KAZAR
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a, b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}

typedef long long ll;
typedef pair<int, int> ii;

const int inf = 1e9 + 143;
const ll longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int N = 111;

const int dx[] = {-1, +1, 0, 0};
const int dy[] = {0, 0, -1, +1};

int id[1024];

int row[N], col[N];
char s[N][N];

void solve(){
    int n = read();
    int m = read();
    for(int i = 1; i <= n; i++){
        scanf(" %s", s[i] + 1);
    }
    memset(row, 0, sizeof row);
    memset(col, 0, sizeof col);
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(s[i][j] != '.'){
                row[i]++;
                col[j]++;
            }
        }
    }
    auto inside = [&](int x,int y){
        return x >= 1 && x <= n && y >= 1 && y <= m;
    };
    int res = 0;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(s[i][j] != '.'){
                int dx = ::dx[id[s[i][j]]];
                int dy = ::dy[id[s[i][j]]];
                int x = i + dx;
                int y = j + dy;
                bool hit = false;
                while(inside(x, y)){
                    if(s[x][y] != '.'){
                        hit = true;
                        break;
                    }
                    x += dx;
                    y += dy;
                }
                if(!hit){
                    if(row[i] == 1 && col[j] == 1){
                        puts("IMPOSSIBLE");
                        return;
                    }
                    ++res;
                }
            }
        }
    }
    printf("%d\n", res);
}

int main(){

#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    //freopen("error","w",stderr);
#endif

    id['<'] = 2;
    id['^'] = 0;
    id['>'] = 3;
    id['v'] = 1;

    int t = read();

    for(int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        solve();
        eprintf("test = %d\n", i);
    }

    return 0;
}
