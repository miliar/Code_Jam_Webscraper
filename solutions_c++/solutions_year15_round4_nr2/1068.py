#include <bits/stdtr1c++.h>

using namespace std;

typedef long double ld;

const int MAXM = 110, MAXN = 105;
ld a[MAXM][MAXN], b[MAXN], INF = 1e98, EPS = 1e-13;

// Simon Lo's (TESTED)
//   Simplex algorithm on augmented matrix a of dimension (m+1)x(n+1)
//   first m rows describe constraints, last row describes objective function.
//   returns 1 if feasible, 0 if not feasible, -1 if unbounded
//   returns solution in b[] in original var order, max(f) in ret
//   form: maximize sum_j(a_mj*x_j)-a_mn s.t. sum_j(a_ij*x_j)<=a_in
//   in standard form.
//   To convert into standard form:
//   1. if exists equality constraint, then replace by both >= and <=
//   2. if variable x doesn't have nonnegativity constraint, then replace by
//      difference of 2 variables like x1-x2, where x1>=0, x2>=0
//   3. for a>=b constraints, convert to -a<=-b
//   4. turn minimizing condition into maximizing by multiplying -1 to obj.func.
//   note: watch out for -0.0 in the solution, algorithm may cycle
//   EPS = 1e-7 may give wrong answer, 1e-10 is better
//   On average, simplex is O( m * log n). If there are many equations and few
//   variables, its more efficient to use the dual:
//   normal: max c^T*x, s.t. Ax <= b <---> dual: min b^T*y, s.t. A^T*y >= c.
void pivot(int m,int n, ld a[MAXM][MAXN],
           int B[MAXM],int N[MAXN],int r,int c) {
  int i,j; swap(N[c], B[r]); a[r][c]=1/a[r][c];
  for(j=0;j<=n;j++) if(j!=c) a[r][j]*=a[r][c];
  for(i=0;i<=m;i++) if(i!=r) {
    for(j=0;j<=n;j++) if(j!=c) a[i][j]-=a[i][c]*a[r][j];
    a[i][c] = -a[i][c]*a[r][c]; } }
int feasible(int m,int n,ld a[MAXM][MAXN],int B[MAXM],int N[MAXN]) {
  int r,c,i; ld p,v;
  while(1) {
    for(p=INF,i=0; i<m; i++) if(a[i][n]<p) p=a[r=i][n];
    if(p>-EPS) return 1;
    for(p=0,i=0; i<n; i++) if(a[r][i]<p) p=a[r][c=i];
    if(p>-EPS) return 0;
    p = a[r][n]/a[r][c];
    for(i=r+1; i<m; i++) if(a[i][c]>EPS) {
      v = a[i][n]/a[i][c];
      if(v<p) r=i,p=v; }
    pivot(m,n,a,B,N,r,c); } }
int simplex(int m,int n,ld a[MAXM][MAXN],ld b[MAXN],ld& ret) {
  int B[MAXM],N[MAXN],r,c,i; ld p,v;
  for(i=0; i<n; i++) N[i]=i;
  for(i=0; i<m; i++) B[i]=n+i;
  if(!feasible(m,n,a,B,N)) return 0;
  while(1) {
    for(p=0,i=0; i<n; i++) if(a[m][i]>p) p=a[m][c=i];
    if(p<EPS) {
      for(i=0; i<n; i++) if(N[i]<n) b[N[i]]=0;
      for(i=0; i<m; i++) if(B[i]<n) b[B[i]]=a[i][n];
      ret = -a[m][n];
      return 1; }
    for(p=INF,i=0; i<m; i++) if(a[i][c]>EPS) {
      v = a[i][n]/a[i][c];
      if(v<p) p=v,r=i; }
    if(p==INF) return -1;
    pivot(m,n,a,B,N,r,c); } }
    
ld V[105], X[105];
int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
        
        int n; cin >> n;
        
        ld Vf, Xf; cin >> Vf >> Xf;
        for (int i = 0; i < n; i++) {
            cin >> V[i] >> X[i];
        }
        
        ld l = 0, r = 1e12;
        bool once = false;
        while (abs(r-l) > 1e-8) {
            memset(a, 0, sizeof a);
            memset(b, 0, sizeof b);
            int ncons = n+4, nvars = n;
            // sum Vi ti = V
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < n; j++) {
                    a[i][j] = (i > 0 ? -1 : 1) * V[j];
                }
                a[i][n] = (i > 0 ? -1 : 1) * Vf;
            }
            
            // sum Vi/Vf * Xi ti = X
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < n; j++) {
                    a[2+i][j] = (i > 0 ? -1 : 1) * V[j]*X[j]/Vf;
                }
                a[2+i][n] = (i > 0 ? -1 : 1) * Xf;
            }
            
            ld m = (l+r)/2;
            for (int i = 0; i < n; i++) {
                a[4+i][i] = 1;
                a[4+i][n] = m;
            }
            for (int i = 0; i < n; i++) {
                a[ncons][i] = 1;
            }
            
            ld ret;
            int res = simplex(ncons, nvars, a, b, ret);
            once = once || res;
            
            if (res) {
                r = m;
            } else {
                l = m;
            }
        }
        
        if ((l+r)/2 > 1e10) cout << "IMPOSSIBLE" << endl;
        else cout << fixed << setprecision(8) << (l+r)/2 << endl;
    }
	return 0;
}