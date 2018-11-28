#include <stdio.h>
#include <string>
#include <iostream>
#include <stack>
using namespace std;
char s[1005];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, Sm, c = 0;
    scanf("%d", &T);
    while (T--) {
        int sum = 0, ans = 0;
        scanf("%d%s", &Sm, s);
        for (int i = 0; i <= Sm; ++i) {
            if (i > sum) {
                int tmp = i - sum;
                sum += tmp;
                ans += tmp;
            }
            sum += (s[i] - '0');
        }
        printf("Case #%d: %d\n", ++c, ans);
    }
    return 0;
}
/*#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long LL;
const int MaxN = 5010;
const double EInf = 1e50;

struct tNode {
    double x, y;
    tNode(){}
};

bool Use[MaxN];
int N, W, R, Vs, Vt;
double F[MaxN];
tNode A[MaxN];

double sqr(double x) {return (x * x); }

double Dis_vs(int i) {return sqr(min(A[i].x - 1, W - A[i].y)); }

double Dis_vt(int i) {return sqr(min(A[i].y - 1, R - A[i].x)); }

double Dis(int u, int v) {return (sqr(A[u].x - A[v].x) + sqr(A[u].y - A[v].y)) / 4.0; }

int main() {
    freopen("a.txt", "r", stdin);
  //  freopen("dis.out", "w", stdout);
  while(~scanf("%d%d%d",&N,&R,&W)){
    Vs=N+1;Vt=N+2;
    for(int i=1;i<=N;i++)scanf("%lf%lf",&A[i].x,&A[i].y);
    for(int i=1;i<=Vt;i++){F[i]=EInf;Use[i]=false;}F[Vs]=0;

    for(int i=1;i<=Vt;i++){
        int u=0;
        double Min=EInf;
        for (int j=1;j<=Vt;j++){
            if ((!Use[j])&&(Min>F[j])){
                Min = F[j];
                u = j;
            }
        }
        if (u==0)break;
        Use[u]=true;
        if(u==Vt)break;
        if(u==Vs){
            for(int j=1;j<=N;j++)if(Dis_vs(j)<=F[j])F[j]=Dis_vs(j);
        }else{
            for(int j=1;j<=N;j++){
                F[j] = min(F[j], max(F[u], Dis(u, j)));
            }
            F[Vt] = min(F[Vt], max(F[u], Dis_vt(u)));
        }
    }
    printf("%.2f\n", sqrt(F[Vt]));}
    return 0;
}*/
/*double dp[5005][5005];
int main() {
    int n, k;
    dp[1][1] = 1;
    for (int i = 2; i <= 5000; ++i) {
        dp[i][1] = dp[i - 1][1] + 1.0/i;
    }
    for (int i = 2; i <= 4999; ++i) {
        dp[i][i] = dp[i - 1][i - 1] * 1.0/i;
        for (int j = i + 1; j <= 5000; ++j) {
            dp[j][i] = dp[j - 1][i - 1]/j + dp[j - 1][i];
        }
    }
    while (scanf("%d%d", &n, &k) != EOF) {
        if(k == 1) {
            printf("%.4f\n", 1.0/n);
        }
        else {
            double ans = 0;
            while (k) {
                ans += (dp[n][k] - dp[n - 1][k]);
                --k;
            }
            printf("%.4f\n", ans);
        }
    }
    return 0;
}*/
/*#include <stdio.h>
#include <string.h>
char mt[52][52];
int dx[] = {1, 0, 0, -1};
int dy[] = {0, 1, -1, 0};
int flag[52][52], cnt;
int dir[125];
void go(const int x, const int y) {
    flag[x][y] = 1, ++cnt;
    int xx, yy;
    for (int i = 0; i < 4; ++i) {
        if (dir[mt[x][y]] & (1 << i)) {
            xx = x + dx[i];
            yy = y + dy[i];
            if (mt[xx][yy] != '#' && flag[xx][yy] == -1) go(xx, yy);
        }
    }
}
void go2(const int x, const int y) {
    flag[x][y] = 2, --cnt;
    int xx, yy;
    for (int i = 0; i < 4; ++i) {
        xx = x + dx[i];
        yy = y + dy[i];
        if (flag[xx][yy] == 1 && (dir[mt[xx][yy]] & (1 << (3 - i)))) go2(xx, yy);
    }
}
int main(){
    dir['.'] = 1, dir['+'] = 15, dir['-'] = 6, dir['|'] = 9;
    //freopen("a.txt", "r", stdin);
    int r, c, rr, cc;
    int sx, sy, tx, ty;
    scanf("%d%d", &r, &c);
    for (int i = 1; i <= r; ++i) {
        scanf("%s", mt[i] + 1);
        for (int j = 1; j <= c; ++j)
            if (mt[i][j] == 'S') sx = i, sy = j;
            else if (mt[i][j] == 'T') tx = i, ty = j;
    }
    rr = r + 1, cc = c + 1;
    for (int i = 0; i <= cc; ++i)
        mt[0][i] = mt[rr][i] = '#';
    for (int i = 1; i <= r; ++i)
        mt[i][0] = mt[i][cc] = '#';
    memset(flag, -1, sizeof(flag));
    mt[sx][sy] = '+', mt[tx][ty] = '+';
    cnt = 0;
    go(sx, sy);
    if (flag[tx][ty] == -1) {
        puts("I'm stuck!");
    }
    else {
        go2(tx, ty);
        printf("%d\n", cnt);
    }
    return 0;
}*/
/*#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <list>
using namespace std;
long long f[2000][3][2];
/// f[seq_k to place][0: to place 0 , 1: ethier 0 or 1, 2 : must be 1][3 is placed ?1 : 0]
int dp(int n, int p1, int p3)
{
    long long &now = f[n][p1][p3];
    if (now != -1)
    return now;
    if (n == 0)
    {
        if (p1 == 2 && p3 == 1)
        {
            now = 1;
        }else
        {
            now = 0;
        }
            return now;
    }
    now = 0;
    if (p1 == 0)
    {
        now += dp(n-1, 1, p3); /// go 0
    }else if (p1 == 1)
    {
        now += dp(n-1, 1, p3); /// go 0now += dp(n-1, 2, p3); // go 1
    }else /// p1 == 2
    {
        now += dp(n-1, 2, p3); /// go 1
    }
    if (p3 == 0)
    {
        now += dp(n-1, p1, p3); /// go 2;
        now += dp(n-1, p1, 1); /// go 3;
    }else
    {
        now += dp(n-1, p1, 1); /// go 3;
    }
        now %= 1000000007;
    }
int main()
{
    int n;
    cin >> n;
    memset(f, -1, sizeof(f));
    int ans = dp(n - 1, 0, 0); /// seq[n] is 2
    cout << ans << endl;
    return 0;
}*/
