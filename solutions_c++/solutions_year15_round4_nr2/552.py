// 改进单纯性法的实现
// 参考：http://en.wikipedia.org/wiki/Simplex_algorithm
// 输入矩阵a描述线性规划的标准形式。a为m+1行n+1列，其中行0~m-1为不等式，行m为目标函数（最大化）。列0~n-1为变量0~n-1的系数，列n为常数项
// 第i个约束为a[i][0]*x[0] + a[i][1]*x[1] + ... <= a[i][n]
// 目标为max(a[m][0]*x[0] + a[m][1]*x[1] + ... + a[m][n-1]*x[n-1] - a[m][n])
// 注意：变量均有非负约束x[i] >= 0
#include<cstdio>
#include<iostream>
#include<map>
#include<vector>
#include<queue>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
const int maxm = 505;
const int maxn = 505;
const double INF = 1e100;
const double eps = 1e-10;
int n,m;
long double a[maxm][maxn];
int B[maxm], N[maxn];
void pivot(int r, int c) {
swap(N[c], B[r]);
a[r][c] = 1 / a[r][c];
for(int j = 0; j <= n; j++) if(j != c) a[r][j] *= a[r][c];
for(int i = 0; i <= m; i++) if(i != r) {
    for(int j = 0; j <= n; j++) if(j != c) a[i][j] -= a[i][c] * a[r][j];
    a[i][c] = -a[i][c] * a[r][c];
}
}
bool feasible()
{
    for(;;)
    {
        int r, c;
        double p = INF;
        for(int i = 0; i < m; i++) if(a[i][n] < p) p = a[r = i][n];
        if(p > -eps) return true;
        p = 0;
        for(int i = 0; i < n; i++) if(a[r][i] < p) p = a[r][c = i];
        if(p > -eps) return false;
        p = a[r][n] / a[r][c];
        for(int i = r+1; i < m; i++) if(a[i][c] > eps) {
        double v = a[i][n] / a[i][c];
        if(v < p) { r = i; p = v; }
    }
    pivot(r, c);
}
}
double ret;
int simplex(int n, int m, double x[maxn])
{
    for(int i = 0; i < n; i++) N[i] = i;
    for(int i = 0; i < m; i++) B[i] = n+i;
    if(!feasible()) return 0;
    for(;;) {
      int r, c;
      double p = 0;
      for(int i = 0; i < n; i++) if(a[m][i] > p) p = a[m][c = i];
      if(p < eps) {
        for(int i = 0; i < n; i++) if(N[i] < n) x[N[i]] = 0;
        for(int i = 0; i < m; i++) if(B[i] < n) x[B[i]] = a[i][n];
        ret = -a[m][n];
        return 1;
      }
      p = INF;
      for(int i = 0; i < m; i++) if(a[i][c] > eps) {
        double v = a[i][n] / a[i][c];
        if(v < p) { r = i; p = v; }
      }
      if(p == INF) return -1;
      pivot(r, c);
    }
}
double r[105],c[105];
double yy[105];
main()
{
    freopen("B-small-attempt0 (2).in","r",stdin);
    freopen("B-small-attempt0 (2).out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int nn;
        double v,x;
        scanf("%d%lf%lf",&nn,&v,&x);
        for(int i=1;i<=nn;i++)
        scanf("%lf%lf",&r[i],&c[i]);
        double ans=1000000000;
        for(int i=1;i<=nn;i++)
        {
            memset(a,0,sizeof(a));
            for(int j=0;j<nn;j++)
            {
                a[0][j]=r[j+1];
                a[1][j]=-r[j+1];
            }
            a[0][nn]=v;
            a[1][nn]=-v;
            for(int j=0;j<nn;j++)
            {
                a[2][j]=r[j+1]*c[j+1];
                a[3][j]=-r[j+1]*c[j+1];
            }
            a[2][nn]=x*v;
            a[3][nn]=-x*v;
            int now=4;
            for(int j=1;j<=nn;j++) if(i!=j)
            {
                a[now][i-1]=-1;
                a[now][j-1]=1;
                now++;
            }
            a[now][i-1]=-1;
            n=nn;
            m=now;
            int re=simplex(n,m,yy);
            ret=-ret;
            //cout<<re<<"==="<<ret<<endl;
            if(re==1)
            ans=min(ans,ret);
        }
        printf("Case #%d: ",++cas);
        if(ans>=10000000) puts("IMPOSSIBLE");
        else printf("%.6f\n",ans);

    }
}
