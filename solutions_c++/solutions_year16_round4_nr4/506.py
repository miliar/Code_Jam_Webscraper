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

const int MAXN = 25;

pair <int, int> e[MAXN*MAXN];
char g[MAXN+2][MAXN+2], a[MAXN+2][MAXN+2];
int N, m, ans, id, c1, c2, c3, v1[MAXN], v2[MAXN];

void DFS1(int);

void DFS2(int x)
{
    v2[x] = id, ++ c2;
    fo (i, 1, N) if (a[i][x] == '1' && v1[i] < id) DFS1(i);
}

void DFS1(int x)
{
    v1[x] = id, ++ c1;
    fo (i, 1, N) if (a[x][i] == '1')
    {
        ++ c3;
        if (v2[i] < id) DFS2(i);
    }
}


int main()
{
    freopen("D.in", "r", stdin), freopen("D.out", "w", stdout);
    int T = Read();
    fo (ca, 1, T)
    {
        scanf("%d", &N);
        fo (i, 1, N) scanf("%s", g[i]+1);
        
        m = 0;
        fo (i, 1, N)
            fo (j, 1, N) if (g[i][j] == '0')
                e[m ++] = mkp(i, j);
        ans = m;
        fo (mask, 0, (1 << m) - 1)
        {
            Cpy(a, g); int cur = 0;
            fo (i, 0, m - 1) if (Bit(mask, i))
                a[e[i].first][e[i].second] = '1', cur ++;
            if (cur >= ans) continue;
            ++ id;
            bool chk = 1;
            fo (i, 1, N) if (v1[i] < id)
            {
                c1 = 0, c2 = 0, c3 = 0, DFS1(i);
                if (c1 != c2 || c3 != c1 * c1) { chk = 0; break; }
            }
            if (chk) ans = cur;
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}