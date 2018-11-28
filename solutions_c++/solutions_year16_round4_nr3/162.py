#include <cstdio>
#include <cstring>
#define rep(i,s,t) for (int i=(s); i<=(t); ++i)
#define dep(i,t,s) for (int i=(t); i>=(s); --i)

const int maxn = 510;

int n,m,inp[maxn][maxn];
char pp[maxn][maxn];
int xi[maxn],yi[maxn];

template<class T>
inline void get(T &n) {
    char c = getchar();
    while (c!='-' && (c<'0' || c>'9')) c = getchar();
    n = 0; T s = 1; if (c=='-') s = -1,c = getchar();
    while (c>='0' && c<='9') n*=10,n+=c-'0',c=getchar();
    n *= s;
}

int judge(int u, int v, int lat, int las) {
    while (inp[lat][las] == 0) {
        int tmp0, tmp1;
        if (pp[lat][las] == '/') {
            if (lat == u + 1) tmp0 = lat,tmp1 = las - 1;
            else if (lat == u - 1) tmp0 = lat,tmp1 = las + 1;
            else if (las == v + 1) tmp0 = lat - 1,tmp1 = las;
            else if (las == v - 1) tmp0 = lat + 1,tmp1 = las;
        }
        else {
            if (lat == u + 1) tmp0 = lat,tmp1 = las + 1;
            else if (lat == u - 1) tmp0 = lat,tmp1 = las - 1;
            else if (las == v + 1) tmp0 = lat + 1,tmp1 = las;
            else if (las == v - 1) tmp0 = lat - 1,tmp1 = las;
        }
        u = lat; v = las; lat = tmp0; las = tmp1;
    }
    return inp[lat][las];
}

bool legal()
{
    rep(i,1,m) {
        int x = inp[0][i], y = judge(0,i,1,i);
        if (x != y) return false;
    }
    rep(i,1,m) {
        int x = inp[n + 1][i],y = judge(n + 1, i, n, i);
        if (x != y) return false;
    }
    rep(i,1,n) {
        int x = inp[i][0],y = judge(i, 0, i, 1);
        if (x != y) return false;
    }
    rep(i,1,n) {
        int x = inp[i][m + 1],y = judge(i, m + 1, i, m);
        if (x != y) return false;
    }
    return true;
}


bool gao(int u, int v) {
    if (u > n) {
        if (legal()) {
            rep(i,1,n) {
                rep(j,1,m) printf("%c", pp[i][j]);
                puts("");
            }
            return true;
        }
        return false;
    }
    int uu, vv;
    if (v == m) uu = u + 1,vv = 1;
    else uu = u,vv = v + 1;
    pp[u][v] = '\\';
    if (gao(uu,vv)) return true;
    pp[u][v] = '/';
    return gao(uu, vv);
}

int main() {    
    int Test;
    get(Test);
    rep(Ti,1,Test) {
        memset(inp, 0, sizeof(inp));
        get(n); get(m);
        int id = 0;
        rep(i,1,m) xi[++id] = 0,yi[id] = i;
        rep(i,1,n) xi[++id] = i,yi[id] = m + 1;
        dep(i,m,1) xi[++id] = n+1,yi[id] = i;
        dep(i,n,1) xi[++id] = i,yi[id] = 0;
        id = 0;
        rep(i,1,n+m) {
            int tx, ty;
            get(tx); get(ty);
            inp[xi[tx]][yi[tx]] = ++id;
            inp[xi[ty]][yi[ty]] = id;
        }
        printf("Case #%d:\n", Ti);
        if (!gao(1,1)) printf("IMPOSSIBLE\n");
    }
    return 0;
}
