#include <bits/stdc++.h>
using namespace std;

const int MAXM = 400;
const int MAXN = 400;
int n, m;

const double EPS = 1e-12;

double A[MAXM][MAXN];
int basis[MAXM], out[MAXN];
double r[MAXN], c[MAXN];
double V, X, sumR;
double XX[MAXN];

void pivot(int m, int n, int a, int b) {
   int i,j;
   for (i=0;i<=m;i++) if (i!=a) for (j=0;j<=n;j++) if (j!=b) {
      A[i][j] -= A[a][j] * A[i][b] / A[a][b];
   }
   for (j=0;j<=n;j++) if (j!=b) A[a][j] /= A[a][b];
   for (i=0;i<=m;i++) if (i!=a) A[i][b] = -A[i][b]/A[a][b];
   A[a][b] = 1/A[a][b];

   i = basis[a];
   basis[a] = out[b];
   out[b] = i;
}


bool simplex(int m, int n, double C[][MAXN], double X[]) {
   int i,j,ii,jj;  // i,ii are row indexes; j,jj are column indexes
   for (i=1;i<=m;i++) for (j=0;j<=n;j++) A[i][j] = C[i][j];
   for (j=0;j<=n;j++) A[0][j] = -C[0][j];
   for (i=0;i<=m;i++) basis[i] = -i;
   for (j=0;j<=n;j++) out[j] = j;

   for(;;) {
      for (i=ii=1;i<=m;i++) {
         if (A[i][n]<A[ii][n]
                 || (A[i][n]==A[ii][n] && basis[i]<basis[ii]))
             ii=i;
      }
      if (A[ii][n] >= -EPS) break;
      for (j=jj=0;j<n;j++) 
         if (A[ii][j]<A[ii][jj]-EPS
                 || (A[ii][j]<A[ii][jj]-EPS && out[i]<out[j]))
             jj=j;
      if (A[ii][jj] >= -EPS) return false;
      pivot(m,n,ii,jj);
   }
   return true;
}

bool ok(double mid) {
    memset(A, 0, sizeof(A));
    for (int i = 0; i < n; i++) {
        A[0][i] = 1.0;
    }
    for (int i = 1; i <= m; i++) {
        if (i <= n * 2) {
            int id = (i - 1) / 2;
            A[i][id] = 1.0;
            A[i][n] = mid;
            A[i + 1][id] = -1.0;
            A[i + 1][n] = 0.0;
            i++;
        } else {
            for (int j = 0; j < n; j++) {
                A[i][j] = r[j];
            }
            A[i][n] = V;
            i++;
            for (int j = 0; j < n; j++) {
                A[i][j] = -r[j];
            }
            A[i][n] = -V;
            i++;
            for (int j = 0; j < n; j++) {
                A[i][j] = c[j] * r[j] - r[j] * X;
            }
            A[i][n] = 0;
            i++;
            for (int j = 0; j < n; j++) {
                A[i][j] = -c[j] * r[j] + r[j] * X;
            }
            A[i][n] = 0;
            break;
        }
    }
    
    return simplex(m, n, A, XX);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int nn;
        scanf("%d", &nn);
        scanf("%lf%lf", &V, &X);
        sumR = 0;
        for (int i = 0; i < nn; i++) {
            scanf("%lf%lf", &r[i], &c[i]);
            sumR += r[i];
        }
        n = nn;
        m = 4 + n * 2;
        double L = 0.0;
        double R = 1e10;
        for (int i = 0; i < 100; i++) {
            double mid = (L + R) / 2.0;
            if (ok(mid)) {
                R = mid;
            } else {
                L = mid;
            }
        }
        if (R > 1e9) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        } else {
            printf("Case #%d: %.10f\n", cas, R);
            fprintf(stderr, "%.10f\n", R);
        }
    }  
    return 0;
}