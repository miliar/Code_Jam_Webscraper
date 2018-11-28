#include <algorithm>
#include <iostream>
#include <cstring>
#include <climits>
#include <limits>
#include <complex>
#include <cassert>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#include <set>

#define type(x) __typeof((x).begin())
#define foreach(it,x) for(__typeof(x.begin()) it = x.begin() ; it!=x.end() ; it++ )

#ifdef KAZAR
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a,b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}

const int inf = 1e9 + 143;
const long long longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int dx[8] = {1,1,-1,1,0,-1,0,-1};
const int dy[8] = {1,-1,1,0,1,0,-1,-1};

bool f[6][6][26];
bool a[123][123];
bool used[123][123];
bool g[6][6][26][6][6];
int st[6][6][26][2];

int sz;
int n, m;

void go(int x,int y){
    used[x][y] = 1;
    sz++;
    bool can = true;
    for(int i = 0; i < 8; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 1 && nx <= n && ny >= 1 && ny <= m && a[nx][ny]){
            can = false;
        }
    }
    if(can){
        for(int i = 0; i < 8; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 1 && nx <= n && ny >= 1 && ny <= m && !used[nx][ny]){
                go(nx, ny);
            }
        }
    }
}

int main(){

#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    freopen("error","w",stderr);
#endif

    for(n = 1; n <= 5; n++)
        for(m = 1; m <= 5; m++){
            eprintf("NOW %d %d\n",n,m);
            for(int mask = 0; mask < (1 << (n * m)); mask++){
                int x = mask, c = 0;
                while(x){
                    x -= x & -x;
                    c++;
                }
                if(f[n][m][c])
                    continue;
                x = mask;
                memset(a, 0, sizeof a);
                for(int i = 1; i <= n; i++){
                    for(int j = 1; j <= m; j++){
                        a[i][j] = x & 1;
                        x >>= 1;
                    }
                }
                sz = 0;
                memset(used, 0, sizeof used);
                for(int x = 1; x <= n; x++){
                    for(int y = 1; y <= m; y++){
                        if(a[x][y] == 0){
                            bool can = true;
                            for(int i = 0; i < 8; i++){
                                int nx = x + dx[i];
                                int ny = y + dy[i];
                                if(nx >= 1 && nx <= n && ny >= 1 && ny <= m && a[nx][ny]){
                                    can = false;
                                }
                            }
                            if(can){
                                st[n][m][c][0] = x;
                                st[n][m][c][1] = y;
                                go(x, y);
                                goto END;
                            }
                        }
                    }
                }
                END:
                if(sz == n * m - c){
                    f[n][m][c] = 1;
                    for(int i = 1; i <= n; i++){
                        for(int j = 1; j <= m; j++){
                            g[n][m][c][i][j] = a[i][j];
                        }
                    }
                }
            }
    }

    int tc = read();
    for(int it = 1; it <= tc; it++){
        printf("Case #%d:\n",it);
        int nn = read(), mm = read(), k = read();
        if(nn * mm - 1 == k){
            for(int i = 1; i <= nn; ++i){
                for(int j = 1; j <= mm; j++){
                    if(i == 1 && j == 1) printf("c");
                    else printf("*");
                }
                printf("\n");
            }
        }else if(!f[nn][mm][k]){
            printf("Impossible\n");
        }else{
            for(int i = 1; i <= nn; i++){
                for(int j = 1; j <= mm; j++){
                    if(i == st[nn][mm][k][0] && j == st[nn][mm][k][1]){
                        printf("c");
                    }else{
                        if(g[nn][mm][k][i][j]){
                            printf("*");
                        }else{
                            printf(".");
                        }
                    }
                }
                printf("\n");
            }
        }
    }

    return 0;
}
