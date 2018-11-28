#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <utility>
#include <iomanip>
using namespace std;

const int MAX_CONSTRAINTS = 200;
const int MAX_VARS = 200;
const int MAXM = MAX_CONSTRAINTS + 1;
const int MAXN = MAX_VARS + 1;

const long double EPS = 1e-10;
const long double INF = 1.0/0.0;

long double A[MAXM][MAXN];
int basis[MAXM], out[MAXN];

void pivot(int m, int n, int a, int b)
{
  int i, j;
  for (i = 0; i <= m; i++)
    if (i != a)
      for (j = 0; j <= n; j++)
        if (j != b)
          A[i][j] -= A[a][j] * A[i][b] / A[a][b];
  for (j = 0; j <= n; j++)
    if (j != b) A[a][j] /= A[a][b];
  for (i = 0; i <= m; i++)
    if (i != a) A[i][b] = -A[i][b] / A[a][b];
  A[a][b] = 1 / A[a][b];
  swap(basis[a], out[b]);
}

bool neg;

long double simplex(int m, int n, long double C[][MAXN], long double X[])
{
  int i, j, ii, jj;
  for (i = 1; i <= m; i++)
    copy(C[i], C[i]+n+1, A[i]);
  for (j = 0; j <= n; j++)
    A[0][j] = -C[0][j];
  for (i = 0; i <= m; i++)
    basis[i] = -i;
  for (j = 0; j <= n; j++)
    out[j] = j;
  for (;;) {
    for (i = ii = 1; i <= m; i++)
      if (A[i][n] < A[ii][n] || (A[i][n] == A[ii][n] && basis[i] < basis[ii]))
        ii = i;
    if (A[ii][n] >= -EPS) break;
    for (j = jj = 0; j < n; j++)
      if (A[ii][j] < A[ii][jj] - EPS ||
          (A[ii][j] < A[ii][jj] - EPS && out[i] < out[j]))
        jj = j;
    if (A[ii][jj] >= -EPS) { neg = true; return -INF; }
    pivot(m, n, ii, jj);
  }
  for (;;) {
    for (j = jj = 0; j < n; j++)
      if (A[0][j] < A[0][jj] || (A[0][j] == A[0][jj] && out[j] < out[jj]))
        jj = j;
    if (A[0][jj] > -EPS) break;
    for (i=1, ii=0; i <= m; i++)
      if ((A[i][jj]>EPS) &&
          (!ii || (A[i][n]/A[i][jj] < A[ii][n]/A[ii][jj]-EPS) ||
           ((A[i][n]/A[i][jj] < A[ii][n]/A[ii][jj]+EPS) &&
            (basis[i] < basis[ii]))))
        ii = i;
    if (A[ii][jj] <= EPS) return INF;
    pivot(m, n, ii, jj);
  }
  fill(X, X+n, 0);
  for (i = 1; i <= m; i++)
    if (basis[i] >= 0)
      X[basis[i]] = A[i][n];
  return A[0][n];
}


bool eq(long double x,long double y){
  return fabs(x-y) < 1e-8;
}

void do_case(){
  int N;
  cin >> N;
  
  const int MAX_N = 130;
  
  long double C[MAX_N],X,V,R[MAX_N];
  cin >> V >> X;
  //cout << "**" << endl;
  //cout << V << " " << X << endl;
  
  long double mini = 0,maxi = 0;
  
  for(int i=0;i<N;i++){
    cin >> R[i] >> C[i];
    //cout << R[i] << " " << C[i] << endl;
    if(i == 0){
      mini = C[i]; maxi = C[i];
    }
    mini = min(mini,C[i]);
    maxi = max(maxi,C[i]);
  }
  
  if(!(mini-EPS <= X && X <= maxi+EPS)){
    //cout << X << " " << maxi+EPS << endl;
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  
  int m = N+3;
  int n = N;
  
  long double best = -INF;
  bool changed = false;
  
  long double AA[MAXM][MAXN];
  for(int i=0;i<=m;i++)
    for(int j=0;j<=n;j++)
      AA[i][j] = 0;
  
  AA[0][0] = -1;
  
  for(int i=1;i<N;i++){
    AA[i][0] = -1;
    AA[i][i] = 1;
    AA[i][N] = EPS;
  }
  
  for(int I=0;I<N;I++){
    swap(R[I],R[0]);
    swap(C[I],C[0]);
    
    for(int j=0;j<N;j++){
      AA[N][j] = R[j]*C[j];
      AA[N+1][j] = -R[j]*C[j];
    }
    AA[N][N] = X*V;
    AA[N+1][N] = -X*V;
    
    for(int j=0;j<N;j++){
      AA[N+2][j] = R[j];
      AA[N+3][j] = -R[j];
    }
    AA[N+2][N] = V;
    AA[N+3][N] = -V;
    
    long double XX[MAXN];
    
    neg = false;
    long double tmp = simplex(m,n,AA,XX);
    
    /*
    cout << tmp << " : ";
    
    for(int i=0;i<n;i++)
      cout << XX[i] << " ";
    cout << endl;
    
    long double val = 0;
    for(int i=0;i<n;i++)
      val += XX[i]*R[i]*C[i];
    cout << val << " " << X*V << endl;
    
    val = 0;
    for(int i=0;i<n;i++)
      val += XX[i]*R[i];
    cout << val << " " << V << endl;;
    */
    
    if(!neg && tmp > best){ changed = true; best = tmp; }
    
    swap(R[I],R[0]);
    swap(C[I],C[0]);
  }
  
  if(!changed){
    cout << "IMPOSSIBLE 2" << endl;
  } else {
    cout << -best << endl;
  }
}

int main(){
  cout << fixed << setprecision(9);
  int T,C=1;
  cin >> T;
  while(T--){
    cout << "Case #" << C++ << ": ";
    do_case();
  }
  return 0;
}
