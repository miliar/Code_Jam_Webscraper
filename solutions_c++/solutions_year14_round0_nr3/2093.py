#include<iostream>
#include<cassert>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<iterator>
#include<ctime>
#include<map>
#include<sstream>
#include<set>
#include<cctype>
#include<queue>
#include <memory.h>

using namespace std;

#define all(c) (c).begin(), (c).end()

template<typename T> inline string intToString(T x){ostringstream q;q << x;return q.str();}
template<typename T> inline T myPow(T x, T n, T MOD){T res = 1;while (n>0) {if (n & 1) {res = 1ll*res * x % MOD;}x = 1ll*x * x % MOD;n/=2;}return res;}
template<typename T> inline T gcd(T a, T b){a=abs(a);b=abs(b);while ((a>0) && (b>0)) {if (a>b)a%=b;else b%=a;}return a+b;}


typedef unsigned long long LLong;
typedef long double LDb;

const int MOD = 1000000007;

bool used[111][111];
char ans[111][111];
char w[111][111];
int need;
int n,m;
bool getAns;

int neig(int x, int y)
{
    int k = 0;
    k += w[x-1][y-1]=='*';
    k += w[x-1][y]=='*';
    k += w[x-1][y+1]=='*';
    k += w[x]  [y-1]=='*';
    k += w[x]  [y]=='*';
    k += w[x]  [y+1]=='*';
    k += w[x+1][y-1]=='*';
    k += w[x+1][y]=='*';
    k += w[x+1][y+1]=='*';
    return k;
}

void dfs(int x, int y)
{
    if (1<=x && x<=n && 1<=y && y<=m) {
        if (used[x][y])
            return;
        used[x][y] = true;
        if (neig(x,y) == 0) {
            dfs(x-1,y-1);
            dfs(x-1,y);
            dfs(x-1,y+1);
            dfs(x,y-1);
            dfs(x,y+1);
            dfs(x+1,y-1);
            dfs(x+1,y);
            dfs(x+1,y+1);
        }
    }
}

void check()
{
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            used[i][j] = false;
        }
    }
    bool flag = false;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (flag)
                break;
            if (neig(i,j) == 0) {
                dfs(i,j);
                flag = true;
                break;
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (w[i][j] == '.' && !used[i][j]) {
                return;
            }
        }
    }

    getAns = true;
    flag = false;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (flag)
                break;
            if (neig(i,j) == 0) {
                w[i][j] = 'c';
                flag = true;
                break;
            }
        }

    }


    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            ans[i][j] = w[i][j];
        }
    }

}

void rec(int x, int y) 
{
    if (getAns)
        return;
    if (x==n+1 && y==1) {
        if (need != 0)
            return;
        check();
        return;
    }
    int nx = x;
    int ny = y+1;
    if (ny>m) {
        nx = x+1;
        ny = 1;
    }
    if (need>0) {
        w[x][y] = '.';
        need--;
        rec(nx,ny);
        need++;
    }
    w[x][y] = '*';
    rec(nx,ny);
}

int main()
{
#ifdef m0stik
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
#else
    //    freopen("river.in","r",stdin);
    //freopen("river.out","w",stdout);
#endif
    int test;
    cin >> test;
    for (int tt = 0; tt < test; ++tt) {
        cout << "Case #" << tt+1 << ":" << endl;
        memset(w, 0, sizeof w);
        int q;
        cin >> n >> m >> q;
        need = n*m-q;
        if (need==1) {
            for (int i = 1 ; i <=n ;++i) 
            {
                for (int j = 1; j<=m; ++j) {
                    ans[i][j] = '*';
                }
            }
            ans[1][1]='c';
            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= m; ++j) {
                    cout << ans[i][j];
                }
                cout << endl;
            }
            continue;
        }
        getAns = false;
        rec(1,1);
        if (!getAns) {
            cout << "Impossible" << endl;
            continue;
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                cout << ans[i][j];
            }
            cout << endl;
        }
    }

    return 0;
} 