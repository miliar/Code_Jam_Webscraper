/*
	Time : 0552Z 20160409
	Task : Codejam 16 QR A
	Tags : idiot
	Stat : AC
*/
#include <bits/stdc++.h>

#define fi first
#define se second
#define fo(i,a,b) for (int i = a; i <= b; i ++)
#define fd(i,a,b) for (int i = a; i >= b; i --)
#define fe(i,x,y) for (int i = x, y = lnk[i]; i; i = nxt[i], y = lnk[i])
#define mkp make_pair
#define pb push_back
#define Fill(x,y) memset(x,y,sizeof(x))
#define Cpy(x,y) memcpy(x,y,sizeof(x))
#define Bit(x,y) ((((x) >> (y)) & 1))
#define mit map<int,SI>::iterator
#define sit SI::iterator

using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef pair <double, double> PD;
typedef pair <LL, LL> PLI;
typedef pair <PD, int> PDI;
typedef pair <int, int> PI;
typedef pair <int, PI> PII;
typedef pair <PI, PI> PIII;
typedef set <PI> SI;
typedef vector <int> VI;
typedef vector <PI> VII;
 
int Read()
{
    char c; while (c = getchar(), (c != '-') && (c < '0' || c > '9'));
    bool neg = (c == '-'); LL ret = (neg ? 0 : c - 48);
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
    return neg ? -ret : ret;
}

const int MAXN = 1<<12;

char ans[MAXN+2], best[MAXN+2];
int N, R, P, S, cnt;
int f[12][MAXN][MAXN];

/*bool DFS(int l, int r, int avoid)
{
    
}*/

void DFS(int n, int r, int p)
{
    if (f[n][r][p] >= 0) return;
    f[n][r][p] = 0;
    int s = (1 << (n + 1)) - r - p;
    if ((r > (1 << n)) || (p > (1 << n)) || ((r + p) < (1 << n))) return;
    if (!n)
    {
        if (r) f[n][r][p] = p ? 2 : 1;
            else f[n][r][p] = 4;
        return;
    }
/*    for (int i = 0; i <= min(r, 1 << (n - 1)); i ++)
        for (int j = max(0, 1 << (n - 1) - i - s); j <= min(p, 1 << (n - 1)) && i + j <= (1 << n); j ++)*/
    for (int j = min(p, 1 << n); j >= 0; j --)
        for (int i = min(r, (1 << n) - j); i >= 0 && i + j + s >= (1 << n); i --)
            DFS(n - 1, i, j);
    for (int j = min(p, 1 << n); j >= 0; j --)
        for (int i = min(r, (1 << n) - j); i >= 0 && i + j + s >= (1 << n); i --)
            if (f[n - 1][i][j] >= 0 && f[n - 1][r - i][p - j] >= 0)
            {
                if (Bit(f[n - 1][i][j], 0) && Bit(f[n - 1][r - i][p - j], 2)) f[n][r][p] |= 1;
                if (Bit(f[n - 1][i][j], 0) && Bit(f[n - 1][r - i][p - j], 1)) f[n][r][p] |= 2;
                if (Bit(f[n - 1][i][j], 1) && Bit(f[n - 1][r - i][p - j], 2)) f[n][r][p] |= 4;
                if (f[n][r][p] == 7) return;
            }
}

void DFS2(int n, int r, int p, int b)
{
    if (!n)
    {
        ans[cnt ++] = (p ? 'P' : 'R');
        ans[cnt ++] = (p && r ? 'R' : 'S');
        return;
    }
    int x = b, y = (b + 2) % 3, s = (1 << (n + 1)) - r - p;
    for (int j = min(p, 1 << n); j >= 0; j --)
        for (int i = min(r, (1 << n) - j); i >= 0 && i + j + s >= (1 << n); i --)
            if (f[n - 1][i][j] >= 0 && f[n - 1][r - i][p - j] >= 0)
            {
                if (Bit(f[n - 1][i][j], x) && Bit(f[n - 1][r - i][p - j], y))
                {
                    DFS2(n - 1, i, j, x);
                    DFS2(n - 1, r - i, p - j, y);
                    return;
                }
                if (Bit(f[n - 1][i][j], y) && Bit(f[n - 1][r - i][p - j], x))
                {
                    DFS2(n - 1, i, j, y);
                    DFS2(n - 1, r - i, p - j, x);
                    return;
                }
            }
}

bool cmp(char* x, char* y)
{
    fo (i, 0, (1 << N) - 1)
    {
        if (x[i] > y[i]) return 1;
        if (x[i] < y[i]) return 0;
    }
    return 0;
}

int main()
{
    freopen("A.in", "r", stdin), freopen("A.out", "w", stdout);
    int T = Read();
    Fill(f, -1);
    for (int ca = 1; ca <= T; ca ++)
    {
        scanf("%d%d%d%d", &N, &R, &P, &S); printf("Case #%d: ", ca);
        if (R>(1<<(N-1))||P>(1<<(N-1))||S>(1<<(N-1))) { puts("IMPOSSIBLE"); continue; }
        
        /*if (!DFS(0, (1<<N)-1, -1)) puts("IMPOSSIBLE");
        else
        {
            fo (i, 0, (1<<N)-1) putchar(b[a[i]]);
            puts("");
        }*/
        //Fill(f, -1);
        DFS(N-1, R, P);
        if (!f[N-1][R][P]) { puts("IMPOSSIBLE"); continue; }
        best[0] = 'Z';
        fo (i, 0, 2) if (Bit(f[N-1][R][P], i))
        {
            cnt = 0, DFS2(N - 1, R, P, i), ans[(1<<N)] = 0;
            if (cmp(best, ans)) Cpy(best, ans);
        }
        printf("%s\n", best);
        //puts("");
    }
    
    return 0;
}