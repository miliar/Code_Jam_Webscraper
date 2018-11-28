#include <iostream>
#include <iomanip>
#include <vector>
#include <limits>
using namespace std;
// code from: github:t3nsor/codebook.git/simplex.cpp
//
// Two-phase simplex algorithm for solving linear programs of the form
//
//     maximize     c^T x
//     subject to   Ax <= b
//                  x >= 0
//
// INPUT: A -- an m x n matrix
//        b -- an m-dimensional vector
//        c -- an n-dimensional vector
//        x -- a vector where the optimal solution will be stored
//
// OUTPUT: value of the optimal solution (infinity if unbounded
//         above, nan if infeasible)
//
// To use this code, create an LPSolver object with A, b, and c as
// arguments.  Then, call Solve(x).

typedef long double DOUBLE;
#define double DOUBLE
typedef vector<DOUBLE> VD;
typedef vector<VD> VVD;
typedef vector<int> VI;

const DOUBLE EPS = 1e-14;

struct LPSolver {
  int m, n;
  VI B, N;
  VVD D;

  LPSolver(const VVD &A, const VD &b, const VD &c) : 
    m(b.size()), n(c.size()), N(n+1), B(m), D(m+2, VD(n+2)) {
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) D[i][j] = A[i][j];
    for (int i = 0; i < m; i++) { B[i] = n+i; D[i][n] = -1; D[i][n+1] = b[i]; }
    for (int j = 0; j < n; j++) { N[j] = j; D[m][j] = -c[j]; }
    N[n] = -1; D[m+1][n] = 1;
  }
           
  void Pivot(int r, int s) {
    for (int i = 0; i < m+2; i++) if (i != r)
      for (int j = 0; j < n+2; j++) if (j != s)
        D[i][j] -= D[r][j] * D[i][s] / D[r][s];
    for (int j = 0; j < n+2; j++) if (j != s) D[r][j] /= D[r][s];
    for (int i = 0; i < m+2; i++) if (i != r) D[i][s] /= -D[r][s];
    D[r][s] = 1.0 / D[r][s];
    swap(B[r], N[s]);
  }

  bool Simplex(int phase) {
    int x = phase == 1 ? m+1 : m;
    while (true) {
      int s = -1;
      for (int j = 0; j <= n; j++) {
        if (phase == 2 && N[j] == -1) continue;
        if (s == -1 || D[x][j] < D[x][s] || D[x][j] == D[x][s] && N[j] < N[s]) s = j;
      }
      if (D[x][s] >= -EPS) return true;
      int r = -1;
      for (int i = 0; i < m; i++) {
        if (D[i][s] <= 0) continue;
        if (r == -1 || D[i][n+1] / D[i][s] < D[r][n+1] / D[r][s] ||
            D[i][n+1] / D[i][s] == D[r][n+1] / D[r][s] && B[i] < B[r]) r = i;
      }
      if (r == -1) return false;
      Pivot(r, s);
    }
  }

  DOUBLE Solve(VD &x) {
    int r = 0;
    for (int i = 1; i < m; i++) if (D[i][n+1] < D[r][n+1]) r = i;
    if (D[r][n+1] <= -EPS) {
      Pivot(r, n);
      if (!Simplex(1) || D[m+1][n+1] < -EPS) return -numeric_limits<DOUBLE>::infinity();
      for (int i = 0; i < m; i++) if (B[i] == -1) {
        int s = -1;
        for (int j = 0; j <= n; j++) 
          if (s == -1 || D[i][j] < D[i][s] || D[i][j] == D[i][s] && N[j] < N[s]) s = j;
        Pivot(i, s);
      }
    }
    if (!Simplex(2)) return numeric_limits<DOUBLE>::infinity();
    x = VD(n);
    for (int i = 0; i < m; i++) if (B[i] < n) x[B[i]] = D[i][n+1];
    return D[m][n+1];
  }
};

template<class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
    out << '{';
    for (auto&& el: v) out << el << ",\n";
    out << "}";
    return out;
}
#define FR(i,a,b) \
  for (int i=(a);i<(b);i++)
#define FOR(i,n) FR(i,0,n)
#define FRE(i,a,b) FR(i,a,b+1)
#define FORE(i,n) FRE(i,0,n)
#define MP make_pair

#define MAXM 400   // leave one extra
#define MAXN 400   // leave one extra

double A[MAXM][MAXN];
int basis[MAXM], out[MAXN];

#define INF (1.0/0.0)

void pivot(int m, int n, int a, int b) {
  FORE(i,m) if (i-a) FORE(j,n) if (j-b)
    A[i][j] -= A[a][j]*A[i][b]/A[a][b];
  FORE(j,n) if (j-b) A[a][j] /= A[a][b];
  FORE(i,m) if (i-a) A[i][b] /=-A[a][b];
  A[a][b] = 1/A[a][b];
  swap(basis[a], out[b]);
}

template<typename T>
double simplex(int m, int n,
         T& C, double X[]) {
  int ii,jj;
  FRE(i,1,m) FORE(j,n) A[i][j]=C[i][j];
  FORE(j,n) A[0][j] = -C[0][j];
  FORE(i,m) basis[i] = -i;
  FORE(j,n) out[j] = j;

  for(;;) {
    ii=1; FRE(i,1,m)
      if (MP(A[i][n], basis[i])
        < MP(A[ii][n], basis[ii])) ii=i;
    if (A[ii][n] >= -EPS) break;
    jj=0; FOR(j,n)
      if (MP(A[ii][j], out[j])
        < MP(A[ii][jj], out[jj])) jj=j;
    if (A[ii][jj] >= -EPS) return -INF;
    pivot(m,n,ii,jj);
  }
   
  for(;;) {
    jj=0; FOR(j,n)
      if (MP(A[0][j], out[j])
        < MP(A[0][jj], out[jj])) jj=j;
    if (A[0][jj] > -EPS) break;
    ii=0; FRE(i,1,m)
      if (A[i][jj] > EPS && (!ii ||
       MP(A[i][n]*A[ii][jj], basis[i]) <
      MP(A[ii][n]*A[i][jj], basis[ii])))
        ii=i;
    if (A[ii][jj] <= EPS) return INF;
    pivot(m,n,ii,jj);
  }

  FOR(j,n) X[j] = 0;
  FRE(i,1,m) if (basis[i] >= 0)
    X[basis[i]] = A[i][n];
  return A[0][n];
}

void tc() {
    static int cas = 1;
    cout << "Case #" << cas++ << ": ";
    int N; DOUBLE V, X;
    cin >> N >> V >> X;
    VVD A; VD b; VD c(N+2); c[N] = -1;
    A.push_back(c);
    VD total(N+2), ntotal(N+2);
    VD temp(N+2), ntemp(N+2);
    for (int i = 0; i < N; ++i) {
        DOUBLE R, C;
        cin >> R >> C;
        total[i] = R;
        ntotal[i] = -R;
        temp[i] = C*R;
        ntemp[i] = -C*R;
        VD row(N+2);
        row[i] = 1;
        row[N] = -1;
        A.push_back(move(row));
    }
    total[N+1] = V+EPS;
    A.push_back(total);
    ntotal[N+1] = -V+EPS;
    A.push_back(ntotal);
    temp[N+1] = X*V+EPS;
    A.push_back(temp);
    ntemp[N+1] = -X*V+EPS;
    A.push_back(ntemp);
    VD r(N+1);
    double result = simplex(A.size()-1, N+1, A, r.data());
    if (result == result && result != 1.0/0.0 && result != -1.0/0.0) {
        cerr << setprecision(10) << r << endl;
        cout << fixed << setprecision(10) << -result << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int T; cin >> T; while (T--) tc();
}
